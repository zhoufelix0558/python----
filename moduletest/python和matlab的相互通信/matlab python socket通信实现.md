###Matlab与Python通信方式
`obj = tcpip('rhost',rport) `
creates a TCPIP object with remote port value rport.
`obj = tcpip('localhost', 30000, 'NetworkRole', 'client')` creates a TCPIP object, obj, that is a client interface for a server socket.

###Matlab帮助文档
Start a TCP/IP echo server and create a TCPIP object.
**echotcpip('on',4012)
t = tcpip('localhost',4012);**
Connect the TCPIP object to the host.
**fopen(t)**
Write to the host and read from the host.
**fwrite(t,65:74)
A = fread(t, 10);**
Disconnect the TCPIP object from the host and stop the echo server.
**fclose(t)
echotcpip('off')**

###MATLAB Server
Accept a connection from any machine on port 30000.
**t = tcpip('0.0.0.0', 30000, 'NetworkRole', 'server');**
Open a connection. This will not return until a connection is received.
**fopen(t);**
Read the waveform and confirm it visually by plotting it.
**data = fread(t, t.BytesAvailable);
plot(data);**

###MATLAB Client
This code is running on a second copy of MATLAB.
Create a waveform and visualize it.
**data = sin(1:64);
plot(data);**
Create a client interface and open it.
**t = tcpip('localhost', 30000, 'NetworkRole', 'client');
fopen(t)**
Write the waveform to the server session.
**fwrite(t, data)**

###Python代码
```
import socket

HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("waiting for response from client at port ", PORT)
conn, addr = s.accept()
print('Connected by', addr)
print('hello')
while True:
    data = conn.recv(1024)
    print(data)
    if not data: break
    #clientdata = b"hello client"
    #conn.sendall(clientdata)
conn.close()
```

###Matlab 代码
```
t = tcpip('localhost', 50000);
fopen(t);
% serverdata='nihao'
% fwrite(t, serverdata);


fwrite(t, 20);
data=fscanf(t);
disp(data);
fclose(t);
```

###Python3字符串转换
'12 34'		=>		<class 'str'>
b'12 34'	=>		<class 'bytes'>
####分割str方法
    s_result = '12.34.56'.split('.')
####分割bytes方法：先转换成str类型，或者通过位置进行分割
	s_result = b'1.2 3.4'[0:3]
	float(s_reult)
输出结果为1.2
`float('1.2')`和`float(b'1.2')`效果是相同的
