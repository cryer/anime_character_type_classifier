from PIL import Image
from PIL import ImageEnhance
import random

def resize_image(filename,size_wh,outputname):
    im = Image.open(filename)
    im_w,im_h = im.size
    if im_w < size_wh or im_h < size_wh:
        pass
    else:
        # im.thumbnail((size_wh,size_wh))
        out = im.resize((size_wh,size_wh))
        out.save(outputname)
# resize_image("1.jpg",128,"1a.jpg")

# 随机变换 左右置换，旋转
def image_transform(filename,savename,trans_type):
    im = Image.open(filename)
    rand = random.randrange(15,46)
    rand_choice = random.randrange(0,2)

    if trans_type == 0:
        out = im.rotate(rand)
        if rand_choice == 0:
            out = out.transpose(Image.FLIP_LEFT_RIGHT)
        out.save(savename)
    elif trans_type == 1:
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
        if rand_choice == 0:
            rand = random.randrange(0,15)
            out = im.rotate(rand)
        out.save(savename)
    elif trans_type == 2:
        out = im.rotate(-rand)
        if rand_choice == 0:
            out = out.transpose(Image.FLIP_LEFT_RIGHT)
        out.save(savename)
    else:
        pass

# image_transform("1.jpg","1b.jpg",2)
#随机变换，调整亮度，色彩和对比度
def image_enhance(filename,savename,enhance_type):
    im = Image.open(filename)
    if enhance_type == 0:
        enh_bri = ImageEnhance.Brightness(im)
        brightness = random.uniform(0.7,1.2)
        out = enh_bri.enhance(brightness)
        out.save(savename)
    elif enhance_type == 1:
        enh_col = ImageEnhance.Color(im)
        color = random.uniform(0.7,1.5)
        out = enh_col.enhance(color)
        out.save(savename)
    elif enhance_type == 2:
        enh_con = ImageEnhance.Contrast(im)
        contrast = random.uniform(0.7,3.0)
        out = enh_con.enhance(contrast)
        out.save(savename)
    else:
        pass

# image_enhance("1.jpg","1b.jpg",1)