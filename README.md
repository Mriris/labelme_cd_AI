
# LabelMe-CDwithAI

## 基于Python的图像多边形标注工具

[![PyPI Version](https://img.shields.io/pypi/v/labelme.svg)](https://pypi.python.org/pypi/labelme)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/labelme.svg)](https://pypi.org/project/labelme)
[![CI Badge](https://github.com/wkentaro/labelme/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/Mriris/labelme_cd_AI/actions)

[安装](#installation) | [使用](#usage) | [示例](#examples)

---

![LabelMe](examples/change_detective/.readme/annotation.png)

## 描述

LabelMe 是一个图形图像标注工具，灵感来自 <https://github.com/wkentaro/labelme>。  
使用 Python 编写，Qt 作为图形界面。

[//]: # (![VOC数据集示例]&#40;examples/instance_segmentation/data_dataset_voc/JPEGImages/2011_000006.jpg&#41; )

[//]: # (![VOC数据集标注]&#40;examples/instance_segmentation/data_dataset_voc/SegmentationClass/2011_000006.png&#41; )

[//]: # (![VOC分割结果]&#40;examples/instance_segmentation/data_dataset_voc/SegmentationClassVisualization/2011_000006.jpg&#41; )

[//]: # (![VOC对象分割]&#40;examples/instance_segmentation/data_dataset_voc/SegmentationObject/2011_000006.png&#41;)

[//]: # (![VOC对象分割结果]&#40;examples/instance_segmentation/data_dataset_voc/SegmentationObjectVisualization/2011_000006.jpg&#41;)

[//]: # (<i>VOC数据集实例分割示例。</i>)

## 功能

- [x] 双图像显示和标注。
- [x] 支持多种图像标注：多边形、矩形、圆形、直线和点。([教程](examples/tutorial))
- [x] 图像分类和清理的标志注释。 ([#166](https://github.com/wkentaro/labelme/pull/166))
- [x] GUI自定义（预定义标签/标志、自动保存、标签验证等）。 ([#144](https://github.com/wkentaro/labelme/pull/144))
- [ ] 导出VOC格式的数据集用于语义/实例分割。 ([语义分割](examples/semantic_segmentation), [实例分割](examples/instance_segmentation))
- [ ] 导出COCO格式的数据集用于实例分割。 ([实例分割](examples/instance_segmentation))
- [ ] 支持视频标注。 ([视频标注示例](examples/video_annotation))
## 安装

可以通过以下两种方式安装Labelme：

### 方式1：使用pip安装

更多详细信息请参考["使用pip安装Labelme"](https://www.labelme.io/docs/install-labelme-pip)。

```bash
pip install labelme
```

### 方式2：使用独立的可执行文件（最简单）

如果您希望获得无需安装任何依赖项（如Python和Qt）即可使用的便捷方式，可以下载["Labelme应用"](https://github.com/Mriris/labelme_cd_AI/releases/latest)的免安装可执行文件。


## 使用

运行 `labelme --help` 查看详细信息。  
所有标注都会保存为[JSON](http://www.json.org/)格式的文件。

```bash
labelme  # 打开GUI
```

[//]: # (# 教程（单图像示例）)

[//]: # (cd examples/tutorial)

[//]: # (labelme apc2016_obj3.jpg  # 指定图像文件)

[//]: # (labelme apc2016_obj3.jpg -O apc2016_obj3.json  # 保存后关闭窗口)

[//]: # (labelme apc2016_obj3.jpg --nodata  # 不包含图像数据，只保存相对路径)

[//]: # (labelme apc2016_obj3.jpg   --labels highland_6539_self_stick_notes,mead_index_cards,kong_air_dog_squeakair_tennis_ball  # 指定标签列表)

[//]: # ()
[//]: # (# 语义分割示例)

[//]: # (cd examples/semantic_segmentation)

[//]: # (labelme data_annotated/  # 打开目录，批量标注其中所有图像)

[//]: # (labelme data_annotated/ --labels labels.txt  # 使用文件指定标签列表)

[//]: # (```)

[//]: # (### 命令行参数)

[//]: # (- `--output` 用于指定标注保存的位置。如果指定位置以 .json 结尾，标注将保存为单个JSON文件。只能对一张图像进行标注。如果位置不以 .json 结尾，程序会将标注文件保存到该目录，文件名与图像文件名相对应。)

[//]: # (- 第一次运行 `labelme` 时，程序会在 `~/.labelmerc` 目录创建配置文件。可以编辑该文件，下次启动时会应用这些更改。如果您希望使用来自其他位置的配置文件，可以通过 `--config` 参数指定该文件。)

[//]: # (- 如果没有使用 `--nosortlabels` 参数，程序会按字母顺序列出标签。如果使用该参数，标签会按提供的顺序显示。)

[//]: # (- 标志（Flags）分配给整个图像。 [示例]&#40;examples/classification&#41;)

[//]: # (- 标签（Labels）分配给单个多边形。 [示例]&#40;examples/bbox_detection&#41;)

### FAQ

- **如何将JSON文件转换为numpy数组？** 请参考 [教程](examples/tutorial#convert-to-dataset)。
- **如何加载标签PNG文件？** 请参考 [教程](examples/tutorial#how-to-load-label-png-file)。
- **如何获取语义分割的标注？** 请参考 [语义分割](examples/semantic_segmentation)。
- **如何获取实例分割的标注？** 请参考 [实例分割](examples/instance_segmentation)。

## 双图同步标注

在本克隆仓库中，能够同时标注两张图像。`Labelme` 支持这一功能，通过加载和编辑多个图像来保持它们的标注同步。

### 使用方法

1. **同步标注模式**：
   - 打开两个图像进行标注。`Labelme` 会自动保持它们的标注同步。
   
2. **双图左右切换**：
   - 在界面右上角点击“切换图像”按钮或者按下~键，可以左右图像互换位置，快速触发便于查看变化。

3. **保存标注数据**：
   - 左边的图像标注会单独保存为JSON文件，加载时会优先加载左边图像，若无则右，以便后续分析时使用。


## 示例

* [变化检测](examples/change_detective)
* [图像分类](examples/classification)
* [边界框检测](examples/bbox_detection)
* [语义分割](examples/semantic_segmentation)
* [实例分割](examples/instance_segmentation)
* [视频标注](examples/video_annotation)

## 开发

```bash
git clone https://github.com/Mriris/labelme_cd2AI.git
cd labelme

## 安装anaconda3并安装labelme
#curl -L https://github.com/wkentaro/dotfiles/raw/main/local/bin/install_anaconda3.sh | bash -s .
#source .anaconda3/bin/activate
pip install -e .
```

### 构建独立可执行文件

以下是在macOS、Linux和Windows上构建独立可执行文件的方法：

```bash
# 设置conda
conda create --name labelme python=3.9
conda activate labelme

# 构建独立可执行文件
pip install .
pip install 'matplotlib<3.3'
pip install pyinstaller
pyinstaller labelme.spec
dist/labelme --version
```

[//]: # (### 如何贡献)

[//]: # ()
[//]: # (确保您的环境中通过以下测试：)

[//]: # ()
[//]: # (```bash)

[//]: # (pip install -r requirements-dev.txt)

[//]: # ()
[//]: # (ruff format --check  # `ruff format` 自动修复)

[//]: # (ruff check  # `ruff check --fix` 自动修复)

[//]: # (MPLBACKEND='agg' pytest -vsx tests/)

[//]: # (```)

## 鸣谢

本仓库是 [wkentaro/labelme](https://github.com/wkentaro/labelme) 的一个克隆仓库。
