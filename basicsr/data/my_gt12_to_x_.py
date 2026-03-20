import os
import cv2

original_dir = r'G:\BiShe\LKDN\datasets\Urban100\original'
save_root = r'G:\BiShe\LKDN\datasets\Urban100'
gt_dir = os.path.join(save_root, 'GTmod12')

scales = [2, 3, 4]

os.makedirs(gt_dir, exist_ok=True)
for scale in scales:
    os.makedirs(os.path.join(save_root, f'LRbicx{scale}'), exist_ok=True)

for name in os.listdir(original_dir):
    src_path = os.path.join(original_dir, name)

    if not os.path.isfile(src_path):
        continue

    img = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f'读取失败: {src_path}')
        continue

    h, w = img.shape[:2]

    h_mod = h - (h % 12)
    w_mod = w - (w % 12)
    gt = img[:h_mod, :w_mod]

    gt_path = os.path.join(gt_dir, name)
    cv2.imwrite(gt_path, gt)

    print(f'{name}: original {w}x{h} -> GTmod12 {w_mod}x{h_mod}')

    for scale in scales:
        lr_dir = os.path.join(save_root, f'LRbicx{scale}')
        lr = cv2.resize(gt, (w_mod // scale, h_mod // scale), interpolation=cv2.INTER_CUBIC)
        lr_path = os.path.join(lr_dir, name)
        cv2.imwrite(lr_path, lr)
        print(f'    x{scale}: {w_mod//scale}x{h_mod//scale}')

print('GTmod12 和 LRBicx2/x3/x4 全部生成完成')