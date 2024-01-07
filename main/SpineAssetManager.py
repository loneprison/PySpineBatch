import os
import re
import shutil

def get_file_names_in_directory(directory):
    file_names = []
    
    # 获取目录下所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    script_name = os.path.basename(__file__)
    # 提取文件名（包括后缀）并排除脚本文件自身
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        # 排除脚本文件自身
        if file_name + file_extension != script_name:
            # 添加文件名到列表
            file_names.append(file_name + file_extension)

    return file_names

def move_file(src_path, dest_path):
    try:
        # 移动文件
        shutil.move(src_path, dest_path)
        print(f"移动文件: {src_path} -> {dest_path}")
    except Exception as e:
        # 如果移动失败，输出异常信息
        print(f"移动文件时发生异常: {e}")

def find_png_files_with_numbered_suffix(skel_file_names, directory):
    # 在目录下找到所有 .png 文件
    png_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(".png")]

    for skel_name in skel_file_names:
        file_basename = skel_name.replace(".skel", "")

        # 构建正则表达式模式，匹配 .png 文件的命名模式
        pattern = re.compile(re.escape(file_basename) + r'\d*\.png$', re.IGNORECASE)

        # 在所有 .png 文件中查找符合模式的文件
        matching_png_files = [png_file for png_file in png_files if pattern.match(png_file)]

        # 输出符合条件的 .png 文件
        if matching_png_files:
            print(f"\n找到同名的 .png 文件:")
            for png_file in matching_png_files:
                print(png_file)
                src_path = os.path.join(directory, png_file)
                dest_path = os.path.join(os.path.join(directory, file_basename), png_file)
                move_file(src_path, dest_path)

def create_folders_for_skel_file_names(skel_file_names, directory):
    for skel_name in skel_file_names:
        folder_name = os.path.splitext(skel_name)[0]  # 去除后缀
        folder_path = os.path.join(directory, folder_name)
        
        # 检查文件夹是否存在，如果不存在则创建
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"创建文件夹: {folder_path}")
        else:
            print(f"文件夹已存在: {folder_path}")

def move_atlas_and_skel_files(skel_file_names, directory):
    for skel_name in skel_file_names:
        file_basename = skel_name.replace(".skel", "")
        
        # 移动 .atlas 文件
        atlas_file = file_basename + ".atlas"
        src_path = os.path.join(directory, atlas_file)
        dest_path = os.path.join(os.path.join(directory, file_basename), atlas_file)
        move_file(src_path, dest_path)

        # 移动 .skel 文件
        skel_file = skel_name
        src_path = os.path.join(directory, skel_file)
        dest_path = os.path.join(os.path.join(directory, file_basename), skel_file)
        move_file(src_path, dest_path)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_names = get_file_names_in_directory(current_directory)
    
    print("文件名:")
    for name in file_names:
        print(name)
    
    # 获取带有 ".skel" 后缀的文件名
    skel_file_names = [name for name in file_names if name.lower().endswith(".skel")]

    # 创建文件夹
    create_folders_for_skel_file_names(skel_file_names, current_directory)

    print("\n带有 .skel 后缀的文件名:")
    for name in skel_file_names:
        src_path = os.path.join(current_directory, name)
        dest_path = os.path.join(os.path.join(current_directory, name.replace(".skel", "")), name)
        move_file(src_path, dest_path)
        print(name)

    # 移动 .atlas 和 .skel 文件
    move_atlas_and_skel_files(skel_file_names, current_directory)

    # 筛选同名的 ".png" 文件
    find_png_files_with_numbered_suffix(skel_file_names, current_directory)
    
    # 添加此行以等待用户输入
    input("按下 Enter 键继续...")
