import os

import cv2
import numpy as np


# 拼接多张图片
def concat_images():
    images = []
    save_path = 'figure'
    ori_path = 'data/images/cat-dog.jpg'
    image_path = [ori_path, 'outputs/cat-dog/gradcam/23_0.jpg', 'outputs/cat-dog/gradcam/23_1.jpg']
    for img_path in image_path:
        img = cv2.imread(img_path)
        images.append(img)
    w, h = images[0].shape[:2]
    width = w
    height = h * len(images)
    base_img = np.zeros((width, height, 3), dtype=np.uint8)

    for i, img in enumerate(images):
        base_img[:, h * i:h * (i + 1), ...] = img

    imgae_name = os.path.basename(ori_path)  # 获取图片名
    output_path = f'{save_path}/{imgae_name[:-4]}_result.jpg'
    cv2.imwrite(output_path, base_img)


if __name__ == '__main__':
    concat_images()
