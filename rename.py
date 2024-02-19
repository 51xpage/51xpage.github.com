import os
import re
bat_file_path = "rename_commands.bat"

def generate_rename_commands(folder_path):
    
    with open(bat_file_path, "a+", encoding="utf-8") as bat_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        title_match = re.search(r'^title: "(.*?)"', content, re.MULTILINE)
                        modified_match = re.search(r'^modified: (\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
                        
                        if title_match and modified_match:
                            title = title_match.group(1)
                            modified = modified_match.group(1)
                            # 替换特殊字符，确保文件名有效
                            new_file_name = f"{modified}-{title.replace(':', ' -')}.md"
                            new_file_name = new_file_name.replace('?', '').replace('"', '').replace('/', '-').replace('\\', '-').replace('|', '-').replace('*', '')
                            new_file_path = os.path.join(root, new_file_name)
                            # 写入重命名命令
                            bat_file.write(f'ren "{file_path}" "{new_file_name}"\n')
                            print(f"Command for renaming '{file}' to '{new_file_name}' added to {bat_file_path}")

def list_first_level_directories(folder_path):
    """
    打印指定文件夹下的第一级目录名称。
    :param folder_path: 需要遍历的文件夹路径
    """
    # 确保提供的路径是一个目录
    if not os.path.isdir(folder_path):
        print(f"提供的路径 {folder_path} 不是一个有效的目录。")
        return

    os.remove(bat_file_path)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print(f"开始处理 {item_path} ")
            generate_rename_commands(item_path)


if __name__ == "__main__":
    #folder_path = "_post"  # 指定Markdown文件夹路径
    root_path = ".\\_posts"
    list_first_level_directories(root_path)