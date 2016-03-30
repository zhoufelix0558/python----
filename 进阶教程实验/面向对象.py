# -*- coding: utf-8 -*-
'''
1.如何去定义一个最基本的class

注意：
    1.面向对象编程，是面向对象，不是面向类。不是所有都开始类设计
'''

#（1）定义class
'''
如何去使用对象内置的方法
    1.实例化这个class （test）  t=test()
    2.使用 class.method()的方式去调用class的内置方法
注意：
    1.当定义一个class的内置方法的时候，方法的第一个参数永远是self，没有的话会报错
        self代表的是对象本身，在class内部是全局调用的
'''

class test(object):     #继承最基本的一个object，python默认的类
    '''
    get被称之为test对象的方法，只属于test对象本身，外界不能调用
    使用方法：
        t=test()
        print(t.get())

    '''
    a=1
    def __init__(self,var1=None):        #初始化对象t=test(4) --> varl=4;  变量可以被其他函数使用
                                         #构造函数                   
        self.var1=var1
        pass 
    def get(self,a=None):
        
        return self.var1
    def __del__(self):                   #析构函数（大部分时间用不到），用于销毁变量（python会自动执行的）
        del self.var1

def func_name1():   
    t=test()                #变量t是类class的一个实例
    print(t.a)
    print(t.get())
#func_name1()



#（2）类的继承
class Base(object):
    def __init__(self,name):
        self.name=name
class b(Base):                          #b里面如果没有init方法，程序就会去Base里面找
    def get_name(self):
        print(self.name)
def func_name2():
    newa=b('hello')
    print(newa.get_name())
func_name2()

































