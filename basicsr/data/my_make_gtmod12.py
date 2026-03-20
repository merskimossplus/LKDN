import os
import cv2

src_dir = r'G:\BiShe\LKDN\datasets\Manga109\original'
dst_dir = r'G:\BiShe\LKDN\datasets\Manga109\GTmod12'

os.makedirs(dst_dir, exist_ok=True)

for name in os.listdir(src_dir):
    src_path = os.path.join(src_dir, name)

    if not os.path.isfile(src_path):
        continue

    img = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f'读取失败: {src_path}')
        continue

    h, w = img.shape[:2]

    # 裁剪到能被12整除
    h_new = h - (h % 12)
    w_new = w - (w % 12)

    img_mod = img[:h_new, :w_new]

    dst_path = os.path.join(dst_dir, name)
    cv2.imwrite(dst_path, img_mod)

    print(f'{name}: {w}x{h} -> {w_new}x{h_new}')

print('GTmod12 生成完成')