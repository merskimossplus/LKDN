import os
import cv2

folders = [
    r'G:\BiShe\LKDN\datasets\BSD100\GTmod12',
    r'G:\BiShe\LKDN\datasets\BSD100\LRbicx2',
    r'G:\BiShe\LKDN\datasets\BSD100\LRbicx3',
    r'G:\BiShe\LKDN\datasets\BSD100\LRbicx4'
]

for folder in folders:
    print(f'\n📂 检查文件夹: {folder}')

    for i, name in enumerate(os.listdir(folder)):
        path = os.path.join(folder, name)

        if not os.path.isfile(path):
            continue

        img = cv2.imread(path)

        if img is None:
            print(f'❌ 读取失败: {name}')
            continue

        print(f'{name}: {img.shape}')

        # 只看前5张就够了
        if i >= 4:
            break