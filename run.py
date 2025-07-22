import os
import json

# Thay bằng user/repo và thư mục thực tế của bạn
github_raw_base = "https://raw.githubusercontent.com/nganngane1223/animation-assets/main/frames/"

# Thư mục chứa ảnh
folder_path = "frames"
files = sorted(os.listdir(folder_path))

# Chỉ lấy file ảnh
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]

# Tạo danh sách full URL
image_urls = [github_raw_base + f for f in image_files]

# Ghi vào animation.json
with open("animation.json", "w") as f:
    json.dump(image_urls, f, indent=2)

print("✅ Created animation.json with", len(image_urls), "images.")
