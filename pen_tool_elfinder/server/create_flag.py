# -*- coding: utf-8 -*-
import os
import random

def create_random_flag():
    
    directories = ["/tmp"]

    # Tạo tất cả các thư mục nếu chưa tồn tại
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Danh sách tên file và nội dung
    file_name_choices = [
        "THIS_IS_FLAG5742AB2.txt",
        "CAPTURE_THE_FLAG03468DQ1.txt"
    ]
    content_choices = [
        "U1VDRVNTXzI5QVEzOV9XRUxMX0RPTkU=",
        "VEhBTktfRk9SX0RPSU5HX0xBQlNfMTJIUzY0M1g="
    ]

    
    for i in range(2):
        target_dir = random.choice(directories)
        file_name = file_name_choices[i]
        content = content_choices[i]
        file_path = os.path.join(target_dir, file_name)

        # Nếu file đã tồn tại thì thêm hậu tố để tránh ghi đè
        counter = 1
        base_name, ext = os.path.splitext(file_name)
        while os.path.exists(file_path):
            file_name = f"{base_name}_{counter}{ext}"
            file_path = os.path.join(target_dir, file_name)
            counter += 1

        # Ghi nội dung vào file
        with open(file_path, "w") as f:
            f.write(content)

        print(f"Flag created at: {file_path} with content: {content}")

# Chạy hàm
if __name__ == "__main__":
    create_random_flag()

