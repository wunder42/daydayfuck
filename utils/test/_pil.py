#! -*- coding:utf-8 -*-
from PIL import Image
import os, sys

# path = '/home/knife/下载/'
path = '/home/knife/桌面/knife/文档/thum/'
thum_path = '/home/knife/桌面/knife/文档/thum/'
test_file = 'biguiyuan.tif'
WIDTH = 658
HEIGHT = 1090

IMG_B = "/home/knife/桌面/knife/文档/thum/biguiyuan.tif"
IMG_C = "/home/knife/桌面/knife/文档/hankuke.png"

def main():
	image = Image.open(os.path.join(path, test_file))
	print image.format, image.size, image.mode

	# height = int(WIDTH * image.size[1] / image.size[0])

	t_image = image.resize((WIDTH, HEIGHT))
	# image.show()
	t_image.save(os.path.join(thum_path, test_file))

def test():
	# pass
	img_a = Image.new("RGB", (950,1320), "#fff") 
	img_b = Image.open(IMG_B)
	img_c = Image.open(IMG_C)
	print 'image b' + str(img_b.size)
	print 'iamge c' + str(img_c.size)

	# img_a.paste(img_b.crop((100, 100, 658, 1090)), (262, 207, 658, 1090))
	img_a.paste(img_c.crop((285,251,612,612)), (285, 251, 612, 612))
	img_a.save(os.path.join(path, "new.png"))




if __name__ == '__main__':
    # main()
    test()