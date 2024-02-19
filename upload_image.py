import os
import re
import requests
import time

# 定义全局变量来追踪进度
total_files = 0
processed_files = 0
start_time = time.time()

# PicGo HTTP Server 地址
picgo_server = "http://127.0.0.1:36677/upload"

# 遍历指定文件夹中的所有Markdown文件
def process_markdown_files(folder_path):
    global total_files
    md_files = [os.path.join(root, file)
                for root, dirs, files in os.walk(folder_path)
                for file in files if file.endswith(".md")]
    total_files = len(md_files)
    
    for file_path in md_files:
        process_start_time = time.time()
        process_markdown_file(file_path)
        process_time = time.time() - process_start_time
        print(f"Processed {file_path} in {process_time:.2f} seconds.")
        
        global processed_files
        processed_files += 1
        elapsed_time = time.time() - start_time
        remaining_files = total_files - processed_files
        avg_time_per_file = elapsed_time / processed_files
        estimated_remaining_time = avg_time_per_file * remaining_files
        
        print(f"Processed {processed_files}/{total_files} files in {elapsed_time:.2f} seconds. Estimated remaining time: {estimated_remaining_time:.2f} seconds.")


# 处理单个Markdown文件
def process_markdown_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        print('开始处理:' + file_path)
        content = file.read()
        updated_content, images = extract_and_upload_images(content)
        if updated_content:  # 有进行图片替换，则更新文件内容
            file.seek(0)
            file.write(updated_content)
            file.truncate()
            print(f"Processed {file_path} with {len(images)} images uploaded.")

# 从Markdown内容中提取图片并上传，返回更新后的内容
def extract_and_upload_images(content):
    pattern = r"!\[.*?\]\((images/.*?)\)"
    pattern = r"!\[.*?\]\((\.\./\.\./images/.*?\.(?:png|jpg|jpeg|gif))\)"

    matches = re.findall(pattern, content)
    if not matches:
        return None, []

    for relative_image_path  in matches:
        #full_image_path = os.path.join(os.getcwd(), image_path)  # 假设图片相对当前脚本位置
        print('relative_image_path:' + relative_image_path)
        # 移除路径中的 `../../`
        relative_image_path_cleaned = relative_image_path .replace("../", "")
        # 计算图片的实际文件系统路径，这里使用正斜杠以确保与网络请求兼容
        full_image_path = os.path.abspath(os.path.join(os.getcwd(), relative_image_path_cleaned)).replace("\\", "/")
        #if os.path.exists(full_image_path):
        uploaded_url = upload_image_to_picgo(full_image_path)
        print('full_image_path:' + full_image_path)
        #uploaded_url = upload_image_to_picgo(full_image_path)
        if uploaded_url:
            content = content.replace(relative_image_path, uploaded_url)

    return content, matches

# 上传图片到PicGo
def upload_image_to_picgo(image_path):
    if not os.path.isfile(image_path):
        return None
    files = {'file': open(image_path, 'rb')}
    try:
        response = requests.post(picgo_server, files=files)
        response_json = response.json()
        # 检查上传是否成功
        if response.status_code == 200 and response_json.get('success'):
            # 提取第一个结果的 URL
            return response_json['result'][0]  # 假设我们总是关心第一个结果
        else:
            print(f"Upload failed for {image_path}. Response: {response_json}")
    except Exception as e:
        print(f"Error uploading {image_path}: {e}")
    finally:
        files['file'].close()  # 确保文件在上传后被正确关闭
    return None

def list_first_level_directories(folder_path):
    """
    打印指定文件夹下的第一级目录名称。
    :param folder_path: 需要遍历的文件夹路径
    """
    # 确保提供的路径是一个目录
    if not os.path.isdir(folder_path):
        print(f"提供的路径 {folder_path} 不是一个有效的目录。")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print(f"开始处理 {item_path} ")
            process_markdown_files(item_path)


if __name__ == "__main__":
    #folder_path = "_post"  # 指定Markdown文件夹路径
    root_path = ".\\_posts"
    list_first_level_directories(root_path)