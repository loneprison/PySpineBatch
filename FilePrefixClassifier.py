import os
import shutil
import re

def organize_files_by_prefix(directory):
    # 获取目录下所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(".png")]

    # 创建一个字典，用于存储文件夹路径
    folder_paths = {}

    for file in files:
        # 使用下划线分割文件名
        parts = os.path.splitext(file)[0].split('_')

        if parts:
            # 取第一组字符串作为文件夹名
            prefix = parts[0]

            # 忽略文件名中的 "#" 和数字部分
            prefix = re.sub(r'\s*#(\d+)', '', prefix)

            # 构建文件夹路径
            folder_path = os.path.join(directory, "NonSpineFiles", prefix)

            # 检查文件夹是否存在，如果不存在则创建
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # 将文件移动到对应的文件夹
            src_path = os.path.join(directory, file)
            dest_path = os.path.join(folder_path, file)
            print(f"移动文件: {src_path} -> {dest_path}")
            shutil.move(src_path, dest_path)

            # 存储文件夹路径
            folder_paths[prefix] = folder_path

    return folder_paths

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # 执行文件整理
    folder_paths = organize_files_by_prefix(current_directory)

    # 打印整理结果
    print("文件整理完成，以下是文件夹路径:")
    for prefix, folder_path in folder_paths.items():
        print(f"{prefix}: {folder_path}")

    # 添加此行以等待用户输入
    input("按下 Enter 键继续...")
