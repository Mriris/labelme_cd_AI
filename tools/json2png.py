import numpy as np
import cv2
import json
import os
import re

# 指定要读取 JSON 文件的文件夹和输出结果的文件夹
input_folder = r'C:\0Program\Datasets\241120\Compare\Datas\mask'  # json文件夹路径
output_folder = r'C:\0Program\Datasets\241120\Compare\Datas\mask'  # 输出文件夹路径

# 检查输出文件夹是否存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 存储异常的 JSON 文件及其异常原因
exception_files = []

# 遍历文件夹内所有的 JSON 文件
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        json_path = os.path.join(input_folder, filename)

        # 从文件中读取 JSON 数据
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)

                # 获取图像的高度和宽度
                height = data.get('imageHeight', 0)
                width = data.get('imageWidth', 0)

                # 如果高度、宽度为空或为0，则标记异常文件
                if height == 0 or width == 0:
                    exception_files.append((filename, "图像高度或宽度为0"))
                    continue

                # 检查是否包含有效的 'shapes' 字段和至少一个多边形
                if 'shapes' not in data or len(data['shapes']) == 0:
                    exception_files.append((filename, "'shapes' 字段为空或缺失"))
                    continue

                # 创建一个黑色背景的图像
                image = np.zeros((width, height), dtype=np.uint8)

                # 遍历所有的多边形，并绘制白色区域
                for shape in data['shapes']:
                    points = np.array(shape['points'], dtype=np.int32)
                    # 如果points中坐标为浮点型，转换为整型
                    points = points.reshape((-1, 1, 2))
                    # 绘制多边形
                    cv2.fillPoly(image, [points], 255)

                # 获取 JSON 文件名
                json_filename = os.path.basename(json_path)

                # 检查是否以 "_字母.json" 结尾，使用正则表达式匹配
                if re.match(r".*_[a-zA-Z]\.json$", json_filename):
                    # 匹配成功，提取 "_" 之前的部分并将字母改为 "E"
                    base_name = json_filename.rsplit('_', 1)[0]
                    image_name = base_name + '_E.png'
                else:
                    # 不匹配，基于 JSON 文件名生成输出文件名
                    base_name = os.path.splitext(json_filename)[0]
                    image_name = base_name + '_E.png'

                # 拼接保存的图像路径
                output_image_path = os.path.join(output_folder, image_name)

                # 保存图像
                cv2.imwrite(output_image_path, image)

                # 输出提示
                print(f'图像 {json_filename} 已保存为 {output_image_path}')

            except json.JSONDecodeError as e:
                # JSON 解析错误
                exception_files.append((filename, f"JSON解析错误: {e}"))
                print(f'处理文件 {filename} 时发生错误: {e}')
            except KeyError as e:
                # 如果某个键值缺失
                exception_files.append((filename, f"缺少必需的键: {e}"))
                print(f'处理文件 {filename} 时发生错误: {e}')
            except Exception as e:
                # 其他未知错误
                exception_files.append((filename, f"未知错误: {e}"))
                print(f'处理文件 {filename} 时发生错误: {e}')

# 输出异常文件列表及其异常原因
if exception_files:
    print("\n以下 JSON 文件存在异常：")
    for file, reason in exception_files:
        print(f"{file} - 原因: {reason}")
else:
    print("\n所有 JSON 文件处理成功！")
