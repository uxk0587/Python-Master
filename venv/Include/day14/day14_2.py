"""

Written by: Jack Lee                                                   
Time: 2020/4/22 21:55                                                  

Function:   
    Multithreading Communication between client and server by using TCP socket
                                                           
"""

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode, b64decode
from json import dumps
from threading import Thread

from json import loads


def server_main():

    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'test.jpg'
            # Json是纯文本不能携带二进制数据
            # 所以图片的二进制数据要先通过base64编码成Bytes型字符串（字节符），再将bytes型字节符解码成str字符串，保存到字典中
            my_dict['filedata'] = data
            # 通过json.dumps()函数将python字典类型处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送数据，str类型转换为bytes类型发送，发送Bytes字节符文本，这样可以让传输的字节更少
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 绑定IP地址和端口
    server.bind(('192.168.88.143', 65535))
    # 开启监听 监听客户端连接到服务器
    server.listen(512)
    print('Server start listening...')
    with open('test.jpg', 'rb') as f:
        # 将二进制数据处理（编码）成base64字符串（是字节符，Bytes类型字符串：b'abc'）再解码成str类型字符串'abc'
        # （网上传输或者保存到硬盘就要用字节符,这里要将字节符转换为str类型写入python字典,再将Python字典类型转换为json字符串)
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, addr = server.accept()
        print(str(addr) + '：连到了服务器')
        # 启动一个线程来处理客户端请求
        FileTransferHandler(client).start()

def client_main():
    client = socket()
    client.connect(('192.168.88.144', 65533))
    # 定义一个保存bytes类型字节符的对象对象  收到字符串转换为二进制
    in_data = bytes()
    # 由于不知道服务器发送数据有多大，每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据（bytes类型）解码成str类型字符串（unicode编码），在通过loads将str类型转为python字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    # 获取Python字典对象中的filedata的文本值（str类型），将其转换为字节符（bytes类型）
    filedata = my_dict['filedata'].encode('utf-8')
    with open(filename, 'wb') as f:
        # 将bytes类型解码转换为二进制数据写入文件
        f.write(b64decode(filedata))
    print('Image saved')

if __name__ == '__main__':
    # server_main()
    client_main()
