# -*- coding: utf-8 -*-
########################
#author:Andrewseu
#date:2015/9/23
#login weibo
########################
#urlib2变成了urllib.request
#cookielib变成http.cookiejar
#raw_input变成input
#urllib.parse.quote变成urllib.parse.quote
#urllib.urlencode变成urllib.parse.urlencode

#bytes->string  :text.decode('utf-8')
#string->bytes  :text.encode('utf-8')

#retcode=101,5   密码错误
#retcode=4057    你的账号异常，需要人工认证一下
#retcode=4049,2070  需要验证码
#如果是需要验证码:post时候加个参数就可以了door=验证码



import sys
import urllib
import urllib.request
import http.cookiejar
import base64
import re
import json
import rsa
import binascii
#import requests
#from bs4 import BeautifulSoup

#新浪微博的模拟登陆
class weiboLogin:
    def enableCookies(self):
            #获取一个保存cookies的对象
        cj = http.cookiejar.CookieJar()
            #将一个保存cookies对象和一个HTTP的cookie的处理器绑定
        cookie_support = urllib.request.HTTPCookieProcessor(cj)
            #创建一个opener,设置一个handler用于处理http的url打开
        opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
            #安装opener，此后调用urlopen()时会使用安装过的opener对象
        urllib.request.install_opener(opener)

    #预登陆获得 servertime, nonce, pubkey, rsakv
    def getServerData(self):
        url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=ZW5nbGFuZHNldSU0MDE2My5jb20%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1442991685270'
        data = urllib.request.urlopen(url).read()
        p = re.compile('\((.*)\)')
        try:
            #20151230_TypeError: can't use a string pattern on a bytes-like object
            #原因是data是b''形式，需要将data装换成string
            data=data.decode('utf-8')
            json_data = p.search(data).group(1)
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce']
            pubkey = data['pubkey']
            rsakv = data['rsakv']
            return servertime, nonce, pubkey, rsakv
        except:
            print('Get severtime error!'+str(data))
            return None
                

    #获取加密的密码
    def getPassword(self, password, servertime, nonce, pubkey):
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
        #expected bytes, str found,     没有将string变成bytes
        message=message.encode('utf-8')
        #print(message, type(message))
        #print(key,type(key))
        passwd = rsa.encrypt(message, key) #加密
        passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
        return passwd

    #获取加密的用户名
    def getUsername(self, username):
        username_ = urllib.parse.quote(username)
        username_=username_.encode(encoding="utf-8")
        #20151230_没有将string类型转换成bytes
        #print(type(username_))
        username = base64.encodestring(username_)[:-1]
        return username

     #获取需要提交的表单数据   
    def getFormData(self,userName,password,servertime,nonce,pubkey,rsakv):
        userName = self.getUsername(userName)
        psw = self.getPassword(password,servertime,nonce,pubkey)
        
        form_data = {
            'entry':'weibo',
            'gateway':'1',
            'from':'',
            'savestate':'7',
            'useticket':'1',
            'pagerefer':'http://weibo.com/p/1005052679342531/home?from=page_100505&mod=TAB&pids=plc_main',
            'vsnf':'1',
            'su':userName,
            'service':'miniblog',
            'servertime':servertime,
            'nonce':nonce,
            'pwencode':'rsa2',
            'rsakv':rsakv,
            'sp':psw,
            'sr':'1366*768',
            'encoding':'UTF-8',
            'prelt':'115',
            'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype':'META'
            }
        #20151230_POST data should be bytes or an iterable of bytes. It cannot be of type str.
        #在下面函数urllib.parse.urlencode后面加上.encode(encoding='UTF8')
        formData = urllib.parse.urlencode(form_data).encode(encoding='UTF8')
        return formData

    #登陆函数
    def login(self,username,psw):
        self.enableCookies()
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
        servertime,nonce,pubkey,rsakv = self.getServerData()
        formData = self.getFormData(username,psw,servertime,nonce,pubkey,rsakv)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}
        req  = urllib.request.Request(
                    url = url,
                    headers = headers,
                    data = formData
            )
        #print(req,type(req),formData,type(formData))

        result= urllib.request.urlopen(req)
        text = result.read()
        print(text.decode('GBK'))
        #还没完！！！这边有一个重定位网址，包含在脚本中，获取到之后才能真正地登陆
        p = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
        #有了try之后，try里面连变量名写错都不报错，直接运行except
        try:
            #20151230_TypeError: can't use a string pattern on a bytes-like object
            #原因是text是b''形式，需要将data装换成字符,str()和decode()两种转换方式有差异
            text=text.decode('GBK')
            login_url = p.search(text).group(1)
            #print(login_url)
                #由于之前的绑定，cookies信息会直接写入
            urllib.request.urlopen(login_url)
            print("Login success!")
        except:
            print('Login error!')
            return 0

        #访问主页，把主页写入到文件中
        url = 'http://weibo.com/u/2924736702/home?topnav=1&wvr=6'
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        text = response.read()
        fp_raw = open("e://weibo.html","w+",encoding='utf-8')
        #新浪页面用的是‘GBK’编码，decode的时候也是GBK
        #print(text)
        #UnicodeEncodeError: 'gbk' codec can't encode character '\xdf'
        #in position 16472: illegal multibyte sequence
        #因为我记错了，原来微博页面用的是utf-8。并且创建文件的时候应该加上encoding='utf-8'
        fp_raw.write(text.decode('utf-8'))
        fp_raw.close()
            #print text
            
wblogin = weiboLogin()
print('新浪微博模拟登陆:')
#username = input(u'用户：')
#password = input(u'密码：')
username='*********@sina.com'
password='********'
wblogin.login(username,password)
