'''
1.socket服务器的搭建
2.http


'''


#（1）socket服务器的搭建（windows环境中开启不了）
def func_name1():
    import socket

    s = socket.socket(socket.AF_INET,SOCK_STREAM)
    #socket.AF_INET-->基于IP的;    SOCK_STREAM-->tcp/ip

    s.bind(('127.0.0.1',8125))
    #输入的是一个元组(ip,端口)-->绑定ip和端口

    socket.listen(8)
    #n代表允许多少个同时请求,超过的需要等待队列

    while True:
        connection,address = s.accept()         #没有请求的时候会停在这里
        buf = connection.recv(1024)
        connection.send(buf)
    s.close()
#func_name1()















