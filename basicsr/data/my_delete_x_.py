import os
import re

folder = r'G:\BiShe\LKDN\datasets\Urban100\LRbicx4'  # 改成你的路径

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if not os.path.isfile(old_path):
        continue

    # 去掉 x2 / x3 / x4（以及更通用 x数字）
    new_name = re.sub(r'x\d+', '', filename)

    new_path = os.path.join(folder, new_name)

    # 防止重名覆盖（一般不会，但保险）
    if old_path != new_path:
        print(f'{filename} -> {new_name}')
        os.rename(old_path, new_path)

print("重命名完成")