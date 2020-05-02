"""
图像和办公文档处理
Written by: Jack Lee                                                   
Time: 2020/5/2 15:41                                                  

Function: 利用Python操作图像

                                                           
"""

from PIL import Image

def test():
    # Pillow中最重要的类是Image类，读取和处理图像都通过这个类完成。
    image = Image.open('computer.png')
    # 图像格式
    print(image.format)
    # 图像大小（像素）
    print(image.size)
    #
    print(image.mode)
    # 显示图片
    image.show()

# 裁剪图片
def cut_image():
    image = Image.open('computer.png')
    # 生成元组
    rect = 80, 20, 310, 360
    # 裁剪图片
    image.crop(rect).show()

# 生成缩略图
def generate_thumbnail():
    image = Image.open('computer.png');
    size = 128, 128
    image.thumbnail(size)
    image.show()

def zoom_image():
    image = Image.open('computer.png')
    image1 = Image.open('computer.png')
    rect = 80, 20, 310, 360
    # 裁剪图片
    image_head = image.crop(rect)
    # 获得图片尺寸
    width, height = image_head.size
    # 粘贴图片（将一张图片粘贴到另一张图片中）
    image1.paste(image_head.resize((int(width/1.5), int(height/1.5))), (172,40))
    image.show()
    image1.show()


def image_filter():
    from PIL import ImageFilter
    image = Image.open('computer.png')
    # 添加滤镜
    image = image.filter(ImageFilter.CONTOUR)
    # with open('new_image.png', 'wb') as img:
    image.show()
    image.save('new_computer.png')
    #
    # with open('new_computer.png', 'rb') as f:
    #     data = f.read()
    #
    # with open('new_computer1.png', 'wb') as f:
    #     f.write(data)

if __name__ == '__main__':
    # test()
    # cut_image()
    # generate_thumbnail()
    # zoom_image()
    image_filter()
