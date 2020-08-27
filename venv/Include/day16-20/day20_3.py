"""

Written by: Jack Lee                                                   
Time: 2020/8/27 16:27                                                  

Function:   Python进阶Day20：异步处理--aiohttp的使用

                                                           
"""

"""aiohttp是Python的一个第三方库，它提供了异步的HTTP客户端和服务器，这个第三方库可以跟asyncio模块一起工作，
并提供对Future对象的支持。asyncio可以实现单线程的并发IO操作，如果仅在客户端，发挥的威力不大。如果把他用在服务器端，
例如web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持

asyncio实现了TCP、UDP、SSL等协议， aiohttp则是基于asyncio实现的HTTP框架
"""

# 例子1：下面的代码异步的从5个URL中获取页面并通过正则表达式的命名捕获组提取了网站的标题

import asyncio
import re

import aiohttp

# (?<name>exp)	匹配exp并捕获到名为name的组中
PATTERN = re.compile(r'<title>(?P<title>.*)</title>')


async def fetch_page(session, url):
    # async with 是异步上下文管理器：是指在enter和exit方法处能够暂停执行的上下文管理器
    # 参考 https://blog.csdn.net/sl_world/article/details/86608702
    # with 上下文管理器 上下文管理器包含方法__enter__和__exit__方法
    # 参考 https://www.jianshu.com/p/5b01fb36fd4c； https://www.cnblogs.com/pythonbao/p/11211347.html
    # 通过session.get()可以返回一个ClientResponse对象， 可以从这个对象中获取我们任何想要的信息
    async with session.get(url,ssl=False) as resp:
        # 这里必须加await 将程序挂起 去执行其他消息队列中的任务
        return await resp.text()


async def show_title(url):
    # 创建一个会话，返回一个ClientSession对象，赋值为session
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        # search方法搜索字符串中第一次出现正则表达式的模式， 成功返回匹配对象，否则返回None
        # 通过匹配对象.group()方法来得到整个该匹配对象中匹配的字符串
        print(PATTERN.search(html).group('title'))

def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    # asyncio.wait()和asyncio.gather()都是接受多个future或coro组成的列表，
    # 但是不同的是，asyncio.gather会将列表中不是task的coro预先封装为future,而wait则不会。
    # 不过，loop.run_until_complete(asyncio.wait(tasks))运行时，会首先将tasks列表里的coro先转换为future
    # 参考 https://www.cnblogs.com/saolv/p/9975383.html
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()

if __name__ == '__main__':
    main()



