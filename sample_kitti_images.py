
import os
import glob
import random
from shutil import copyfile


def sample_n_image(d, n):
    img_list = glob.glob(os.path.join(d, '*.jpg'))
    return random.sample(img_list, n)

def swap_string(inp, a='/', b='__'):
    # swap filename of a with b
    pass


date = '2011_09_26'
kitti_dir = os.path.join('kitti_data', date)
sync_dir_list = glob.glob(os.path.join(kitti_dir, '2011_09_26_drive_*'))
sync_dir_list.sort()

images_list = []
for d in sync_dir_list:
    im_dir = glob.glob(os.path.join(d, 'image_*'))
    im_dir.sort()

    for _d in im_dir:
        images_list.extend(sample_n_image(os.path.join(_d, 'data'), 1))


for src in images_list:
    dst = src.replace('/', '__')
    dst = os.path.join('./assets/kitti_data', dst)
    copyfile(src, dst)
