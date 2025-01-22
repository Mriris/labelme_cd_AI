import os

# 要忽略的文件夹列表
IGNORE_FOLDERS = {
    '.git', '.idea', '.vscode', '.github', 'examples','tests'
}


def generate_file_index(directory):
    file_index = []
    for root, dirs, files in os.walk(directory):
        # 排除指定的文件夹
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), directory)
            file_index.append(file_path)

    return file_index


def save_index_to_file(file_index, output_file='index.txt'):
    with open(output_file, 'w') as f:
        for file in file_index:
            f.write(f"{file}\n")


if __name__ == '__main__':
    directory = '.'  # 当前目录
    file_index = generate_file_index(directory)
    save_index_to_file(file_index)
