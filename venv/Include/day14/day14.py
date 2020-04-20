"""
Python网络编程入门和网络应用开发
author: Jack Lee
time: 2020/4/20 12:35


requests库的使用：通过requests实现一个访问数据接口从中下载图片保存到本地
"""


from time import time
from threading import Thread
import requests


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        # string.rfind(substr) 返回字符串中substr最后出现的一次位置
        filename = self._url[self._url.rfind('/') + 1:]
        print('Start downloading: %s' % filename)
        resp = requests.get(self._url)
        with open(filename, 'wb') as f:
            # 返回bytes型二进制数据（获取图片文件用resp.content)
            f.write(resp.content)


def main():
    start_time = time()
    # requests.get()构造一个想服务器请求资源的url对象
    # 返回值是一个包含服务器资源的Response对象
    resp = requests.get('http://api.tianapi.com/meinv/index?key=024759fe3b09b55caf5d462e8002d716&num=10')
    # print(resp)
    # print(type(resp)) # 返回Response对象
    # Requests中内置一个JSON解码器，可处理JSON数据返回成字典
    data_model = resp.json()
    # print(data_model)
    # print(type(data_model)) #返回 dict类型
    download_threads = []
    for mn_dict in data_model['newslist']:
        url = mn_dict['picUrl']
        # DownloadHandler(url).start()
        dt = DownloadHandler(url)
        download_threads.append(dt)
        dt.start()
    # 等待所有线程执行结束
    for dt in download_threads:
        dt.join()
    # 花费时间
    end_time = time()
    print("Total Cost %s" % (end_time - start_time))

if __name__ ==  '__main__':
    main()