import os
import shutil

def move_subfolders_and_remove_parent(src_directory, dest_directory, parent_folder):
    parent_folder_path = os.path.join(src_directory, parent_folder)
    dest_folder = os.path.join(dest_directory, parent_folder)

    # 移动所有直接子文件夹和文件到目标文件夹
    for subfolder in os.listdir(parent_folder_path):
        subfolder_path = os.path.join(parent_folder_path, subfolder)
        dest_subfolder = os.path.join(src_directory, os.path.basename(subfolder_path))

        if os.path.isdir(subfolder_path):
            shutil.move(subfolder_path, dest_subfolder)
            print(f"移动子文件夹: {subfolder_path} -> {dest_subfolder}")
        else:
            dest_file = os.path.join(src_directory, os.path.basename(subfolder_path))
            shutil.move(subfolder_path, dest_file)
            print(f"移动文件: {subfolder_path} -> {dest_file}")

    # 删除父文件夹
    shutil.rmtree(parent_folder_path)
    print(f"删除父文件夹: {parent_folder_path}")

if __name__ == "__main__":
    # 获取当前脚本所在目录
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # 处理脚本所在目录下的所有文件夹
    for folder in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder)
        if os.path.isdir(folder_path):
            move_subfolders_and_remove_parent(current_directory, current_directory, folder)

    # 添加此行以等待用户输入
    input("按下 Enter 键继续...")
