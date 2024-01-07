import os
import subprocess

def process_spine_atlas(spine_exe_path, input_atlas):
    output_images_dir = os.path.join(os.path.dirname(input_atlas), 'image')
    
    command = [
        spine_exe_path,
        '-u', 'latest',
        '-i', os.path.dirname(input_atlas),
        '-o', output_images_dir,
        '-c', input_atlas
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f'Processed: {input_atlas}')
        print('-' * 40)  # 添加分隔符
    except subprocess.CalledProcessError as e:
        print(f'Error processing {input_atlas}: {e}')
        print(f'Command output: {e.output}')
        print('-' * 40)  # 添加分隔符

# 获取当前脚本所在目录
script_directory = os.path.dirname(__file__)

# 替换成你的 Spine 编辑器的实际路径
spine_exe_path = r'C:\Program Files\Spine\Spine.exe'

# 获取直接子目录
subdirectories = [d for d in os.listdir(script_directory) if os.path.isdir(os.path.join(script_directory, d))]

# 遍历直接子目录
for subdir in subdirectories:
    subdir_path = os.path.join(script_directory, subdir)

    found_atlas = False
    for file in os.listdir(subdir_path):
        # 找到所有以 ".atlas" 结尾的文件
        if file.endswith(".atlas"):
            found_atlas = True
            # 构建完整路径
            atlas_path = os.path.join(subdir_path, file)
            # 调用处理函数
            process_spine_atlas(spine_exe_path, atlas_path)
    
    if not found_atlas:
        print(f'No ".atlas" files found in the directory: {subdir_path}.')

input("处理完成，按 Enter 键退出")
