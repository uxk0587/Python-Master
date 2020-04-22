"""
基于传输层协议的套接字编程
author: Jack Lee
time: 2020/4/21 11:06

TCP套接字
"""

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def server_main():
    # 创建套接字对象并指定使用哪种传输服务
    # family=AF_INET IPv4地址
    # family=AF_INET IPv6地址
    # type=SOCK_STREAM TCP套接字
    # type=SOCK_DGRAM UDP套接字
    # type=SOCK_RAM 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 绑定IP地址和端口（端口用于区分不同的服务）
    # 同一时间在同一端口上只能绑定一个服务 否则报错
    server.bind(('192.168.1.2', 6798))
    # 开启监听 监听客户端连接到服务器
    # 参数512可以理解为连接队列大小
    server.listen(512)
    print('服务器开始监听...')

    while True:
        # 通过循环接受客户端的连接并作出相应的处理（提供服务）
        # accept方法是一个阻塞方法如果没有客户端连接到服务器不会向下执行
        # accept方法返回一个元组其中第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端地址（由IP和端口两部分组成）
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 断开连接
        client.close()

def client_main():
    # 创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 连接到服务器（需要指定IP和端口）
    client.connect(('192.168.88.143', 65535))
    # 从服务器接收数据
    print(client.recv(1024).decode('utf-8'))

    client.close()



if __name__ == '__main__':
    client_main()
