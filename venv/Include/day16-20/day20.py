"""

Written by: Jack Lee                                                   
Time: 2020/7/30 10:42                                                  

Function:   Python并发编程进阶

                                                           
"""

"""多线程"""
import glob
import os
import threading
import time
from PIL import Image

PREFIX = 'thumbnails'

# 生成指定图片文件的缩略图
def generate_thumbnail(infile, size, format='PNG'):
    # 将文件名和扩展名分开 text.py => text, .py
    file, ext = os.path.splitext(infile)
    # 返回字符串最后一次出现的位置
    file = file[file.rfind('\\') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    # 打开图像
    img = Image.open(infile)
    # 图像缩放 Pillow 带ANTIALIAS滤镜缩放
    img.thumbnail(size, Image.ANTIALIAS)
    # 保存图片
    img.save(outfile, format)

# 通过类来实现多线程
class GenerateThumbnail(threading.Thread):

    def __init__(self, infile, size, format='PNG'):
        super().__init__()
        self._infile = infile
        file, ext = os.path.splitext(infile)
        self._ext = ext
        self._file = file[file.rfind('\\') + 1:]
        self._image_size = size
        self._format = format

    @property
    def file(self):
        return self._file

    @property
    def format(self):
        return self._format

    # 必须对某属性设置了property才能用xxx.setter方法
    @format.setter
    def format(self, format):
        self._format = format

    # 重写run方法
    def run(self):
        outfile = f'{PREFIX}/{self._file}_{self._image_size[0]}_{self._image_size[1]}.{self._ext}'
        img = Image.open(self._infile)
        img.thumbnail(self._image_size, Image.ANTIALIAS)
        img.save(outfile, self._format)

def main():
    start = time.time()
    threads = []
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    #  标准库glob 不用遍历整个目录判断每个文件是否符合 匹配所有符合条件的文件，将其以list的形式返回
    for infile in glob.glob('images/*.jpg'):
        print(infile)
        for size in (32, 64, 128):
            # # 创建启动线程
            # thread = threading.Thread(
            #     target=generate_thumbnail,
            #     args=(infile, (size,size))
            # )
            # threads.append(thread)
            # thread.start()
            new_thumbnail_thread = GenerateThumbnail(infile, (size, size))
            threads.append(new_thumbnail_thread)
            new_thumbnail_thread.start()

    for thread in threads:
        thread.join()


    end = time.time()


    print(f'Total time cost: {end - start}')

if __name__ == '__main__':
    main()