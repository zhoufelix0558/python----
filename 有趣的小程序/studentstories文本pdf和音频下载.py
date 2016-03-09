#用于studentstories网站的文件下载，输入序号（1-10X即可）
#包含库：基本的库即可
#author：zhoufelix


import urllib
import urllib.request
import re
import os

def geturl(num):
    pdf=re.compile('http://www.studentstories.de/sites/default/files/podcasts/scripts/folge.*?\x2Epdf')
    mp3=re.compile('http://www.studentstories.de/sites/default/files/podcasts/audio/folge.*?\x2Emp3')
    
    urla='http://www.studentstories.de/search/node/Folge%20'+str(num)
    txt=urllib.request.urlopen(urla)
    txte=txt.read().decode('utf-8')
    pdffind=pdf.findall(txte)
    mp3find=mp3.findall(txte)
    return pdffind[0]+'.pdf',mp3find[0]
def getname(string):
    txt=string.split('/')
    return txt[-1]
def download(url):
    urllib.request.urlretrieve(url,os.getcwd()+'/'+getname(url))
    print(getname(url)+"下载完成\n")
#url='http://www.studentstories.de/'
#trt=urllib.request.urlopen(url)
#data =trt.read()
#print(data)
def downnum(num):
    pdfname,mp3name=geturl(num)
    download(pdfname)
    download(mp3name)

#print(geturl(56))
