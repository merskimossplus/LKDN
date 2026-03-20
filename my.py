import os

folders = [
    r'G:\Dataset-SR\DF2K\DF2K_train_LR_bicubic\X4',
    r'G:\Dataset-SR\DF2K\DF2K_train_LR_bicubic\X4_sub'
]

for folder in folders:
    print(f'\n处理文件夹: {folder}')

    for name in os.listdir(folder):
        old_path = os.path.join(folder, name)

        if not os.path.isfile(old_path):
            continue

        # 去掉文件名里的 m
        new_name = name.replace('m', '')
        new_path = os.path.join(folder, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f'{name} → {new_name}')

print('\n全部处理完成')