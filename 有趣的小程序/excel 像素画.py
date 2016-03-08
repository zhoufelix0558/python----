'''将图片中的像素变成excel中每个单元格的背景颜色'''
#运行环境 python3
#安装包：xlsxwriter PIL (anaconda里面都有)
#time:2015-05
#author:zhoufelix



import xlsxwriter
from PIL import Image
import time
t1=time.time()
img = Image.open("test.bmp")
    #打开图片文件
def trans(num):
    str=''
    if num<=26:
        return chr(64+num)
    else:
        num1,yu=divmod(num,26)
        if yu==0:
            num1=num1-1
            yu=yu+26
        str=str+trans(num1)+chr(64+yu)
        return str
#递归哎，我好棒
def hex1(num):
    if num<=15:
        return '0'+hex(num)[2:]
    else:
        return hex(num)[2:]

width=3

array=img.load()
[leng,heig]=img.size
print('长度与宽度：',leng,heig)
    #打印出图片文件的长和宽

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('merge.xlsx')
worksheet = workbook.add_worksheet()
for i in range(0,leng-1):
    worksheet.set_column(i,i,width/10)
for j in range(0,heig-1):
    worksheet.set_row(j,width)
for i in range(0,leng-1):
    for j in range(0,heig-1):
        #worksheet.set_column(i,i,width/10)
        #worksheet.set_row(j,width)
        colij=array[i,j]
        string='#'+hex1(colij[0])+hex1(colij[1])+hex1(colij[2])
        merge_format = workbook.add_format({'fg_color': string})
        #print(i,j)
        #print(i,j,trans(i+1)+str(j+1),string)
        worksheet.write(trans(i+1)+str(j+1),'',merge_format)

# Create a format to use in the merged range.
#merge_format = workbook.add_format({
    #'bold': 1,
    #'border': 1,
    #'align': 'center',
    #'valign': 'vcenter',
    #'fg_color': '#555555'})
    #'#232307'绝壁是我看代码研究出来的，，，，
workbook.close()
t2=time.time()
print('共用时s=',t2-t1,'秒')

