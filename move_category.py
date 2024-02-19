import os
import re
import shutil

def move_md_files_to_categories(source_dir):
    # 正则表达式匹配 Front Matter 中的 categories 属性
    category_pattern = re.compile(r'^category:\s*(.*)$', re.MULTILINE)
    
    # 遍历 source_dir 目录下的所有文件
    for filename in os.listdir(source_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(source_dir, filename)
            
            # 读取文件内容
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 搜索 categories 属性
            match = category_pattern.search(content)
            if match:
                # 获取匹配的类别名称，去除可能的引号并去除首尾空格
                category_name = match.group(1).replace('"', '').replace("'", "").strip()
                category_dir = os.path.join(source_dir, category_name)
                
                # 如果目标目录不存在，则创建
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                
                # 构建新的文件路径
                new_filepath = os.path.join(category_dir, filename)
                
                # 移动文件
                shutil.move(filepath, new_filepath)
                print(f"Moved '{filename}' to '{category_dir}'")
            else:
                print(f"No 'categories' found in '{filename}'")

# 调用函数，'./_posts' 是包含 Markdown 文件的目录
move_md_files_to_categories('./_posts')
