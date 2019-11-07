# -*- coding: utf-8 -*-

import os, sys
from PIL import Image


# https://pillow.readthedocs.io/en/stable/


img = 'van gog - starry nigth.jpg'

van_goh = Image.open(img)
# print(van_goh.format, van_goh.size, van_goh.mode)


def jpg2png(img: str):
    # Transform .jpg to .png
    file, ext = os.path.splitext(img)
    outfile = file + '.png'
    Image.open(img).save(outfile)
    return


def crop(img: str, size: tuple):
    """
    Crop image with size = size
    :param img: strimn with image-name
    :param size: (width, length) - values of size
    :return:
    """
    with Image.open(img) as im:
        im.crop(size).save('crop_{}'.format(img))
    return


def resize(img: str, size: tuple):
    """
    Function, which change size
    :param img: string with image-name
    :param size: (width, length) - tuple with values of size
    :return:
    """
    pic = Image.open(img)
    pic.resize(size).save('resized_{}'.format(img))
    return


def change_dpi(img: str, dpi: tuple):
    """
    Function, which change dpi of image
    :param img: strimn with image-name
    :param dpi: (x, y) - tuple where x, y - dpi-values
    :return:
    """
    with Image.open(img) as im:
        im.save('ch_dpi_{}'.format(img), dpi=dpi)
    return



