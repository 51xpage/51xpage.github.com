import os
import re
from pypinyin import pinyin, lazy_pinyin

# 遍历目录中的所有文件
def convert_filename_to_pinyin(posts_directory):
    for filename in os.listdir(posts_directory):
        if filename.endswith('.md'):  # 确保只处理 Markdown 文件
            # 解析文件名以区分日期部分和标题部分
            filepath = os.path.join(posts_directory, filename)  # 构建文件的完整路径
            print(f"filename:{filename}")
            parts = filename.split('-', 3)  # 分割前三个 '-'，假设日期格式为 YYYY-MM-DD
            if len(parts) < 4:
                print(f"Skipping {filename}, does not match expected format.")
                continue
            
            date_part = '-'.join(parts[:3])  # 日期部分
            title_part = parts[3]  # 中文标题部分
            
            # 将中文标题部分转换为拼音
            title_part = title_part.replace('【', '').replace('】', '').strip()
            pinyin_title = '-'.join(lazy_pinyin(title_part))

            # 读取文件内容并替换图片 URL
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 替换图片 URL
            new_content = content.replace('cdn.iaiuse.com', 'cdn.timetoeasy.com')
            
            # 如果文件内容有变动，写回文件
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated image URLs in {filename}")
            
            # 重命名文件
            new_filename = f"{date_part}-{pinyin_title}"
            os.rename(os.path.join(posts_directory, filename), os.path.join(posts_directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    folder_path = "_posts"  # 指定Markdown文件夹路径
    convert_filename_to_pinyin(folder_path)
