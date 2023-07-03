"""This code is used for feature visualization. Change the path of features and run. Provided by LJM, heihei."""

from glob import glob

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def visualize_features(img_path):
    img = mpimg.imread(img_path)
    print("Image:", img_path)
    print("Shape:", img.shape, end='\t')
    print("Min-Value:", np.min(img), end='\t')
    print("Max-Value", np.max(img))

    # FIXME: 色卡: plasma, RdYlBu_r, bone, afmhot, hot, gist_heat, etc.
    plt.imshow(img, cmap='hot', vmin=np.min(img), vmax=np.max(img))
    # plt.imshow(img, cmap='hot', vmin=0.2, vmax=1.0)
    plt.colorbar()
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    for img_i in glob('visuals/*_600/lmd_0015/*kodim15.png'):
        visualize_features(img_i)

    # FIXME: Used to visualize and save many results in batches.
    # idx = 0
    # for img in glob("visual_vr18_k07/mid_0/y_i_top80/*.png"):
    #     visual_latent("visual_vr18_k07/mid_0/y_ori_i_top80/kodim07_y_ori_%d.png" % idx)
    #     idx += 1

    # i = 0
    # for i in range(80):
    #     img_path = "visuals/backup/visual_vr18/mid_0/y_ori_i_top80/kodim07_y_ori_%d.png" % i
    #     print(img_path)
    #     img = mpimg.imread(img_path)
    #     i += 1
    #     if i == 1:
    #         vmin, vmax = np.min(img), np.max(img)
    #     plt.subplot(8, 10, i)
    #     plt.imshow(img, cmap='RdYlBu_r', vmin=vmin,
    #                vmax=vmax)  # , vmin=vmin, vmax=vmax
    #     plt.title("%d" % i)
    #     plt.axis('off')
    # # plt.suptitle("Channel-Top80")
    # plt.show()
