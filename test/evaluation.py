import matplotlib.image
import os
import sys

sys.path.append("/home/lynx/study/stitch");

from skimage.metrics import structural_similarity
import skimage.measure
import brisque

def entropy(img):
    # 输入图片, 计算信息熵
    return skimage.measure.shannon_entropy(img, base = 2)

def ssim(img_origin, img):
    # 输入参考图片和对比图片, 计算相似度
    return structural_similarity(img_origin, img)

def psnr(img_origin, img):
    # 输入参考图片和对比图片, 计算相似度
    return skimage.measure.compare_psnr(img_origin, img, 255)

def my_brisque(img):
    brisq = brisque.BRISQUE()
    brisq.get_feature(img)
    return brisq.get_score(img)

class Test:
    def fuck(self):
        print('sb')
    def shit(self):
        fuck(self)

if __name__ == "__main__":
    # img1 = matplotlib.image.imread('2.jpg')
    # img2 = matplotlib.image.imread('3.png')
    for num in [1, 2, 4]:
        apap_file = '/home/lynx/fuck_mount/opencv/workspace/test_result/paper/' + str(num) + '_apap.png'
        rew_file = '/home/lynx/fuck_mount/opencv/workspace/test_result/paper/' + str(num) + '_rew.png'
        nis_file = '/home/lynx/fuck_mount/opencv/workspace/test_result/paper/' + str(num) + '_nis.png'
        my_file = '/home/lynx/fuck_mount/opencv/workspace/test_result/paper/' + str(num) + '_my.png'
        if (os.path.isfile(apap_file)
            and os.path.isfile(rew_file)
            and os.path.isfile(nis_file)
            and os.path.isfile(my_file)):
            print([my_brisque(apap_file), my_brisque(rew_file), my_brisque(nis_file), my_brisque(my_file)])
            # print(my_brisque(opencv_result))
        else:
            print('fuck')
            break
