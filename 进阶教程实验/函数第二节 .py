# -*- coding: utf-8 -*-
'''
1.函数注释的写法
2.元组和list都是可以迭代
3.自省：调用函数内部信息和属性
4.作用域:全局变量
5.函数引入可变参数：可变参数能被修改（比如list）
6.lambda函数的使用
7.python3关于filter函数返回值的改变
8.函数关键字的匹配
'''
#（1）函数的使用文档
def func_name1(a,b,c):
    """
        @a:参数a的解释
        @b:参数b的解释
        ...
    """
    return a+b+c


#（2）元组turple和list都是可以迭代的,sorted之后都是list
def func_name2():
    er=[12,23,2,45,56,34,45,65,53]
    op=(12,23,2,45,56,34,45,65,53)
    print(type(er),type(op),type(sorted(er)),type(sorted(op)))
    print(sorted(er),sorted(op))
#func_name1()

#（3）查看函数的属性
def func_name3():
    print(help(func_name1.__code__),'--***--')
        #help函数的返回值是None
    print(dir(func_name1.__code__))
    print(func_name1.__code__.co_varnames)
    print(func_name1.__code__.co_filename)
#func_name3()

    
#（4）参数的作用域：函数的作用域只是作用于本身
    '''
        只有函数内外定义的参数开头都加上global才能是全局变量
    '''
global arg1
global arg2
arg1=1
arg2=2
arg3=3

def func_name4():
    global arg1
    arg1=21
    arg2=22
    arg3=23
    arg4=24
#print(arg4)-->NameError: name 'arg2' is not defined
#func_name4();print(arg1,arg2,arg3)


#（5）函数引入可变参数：可变参数支持自修改
    '''
        本例中tlist引入函数后就会被修改
        tuple不支持修改变量
    '''
def func_name5(arg):
    arg[0]=5
    return arg
tlist=[1,2,3]
#print(func_name5(tlist),tlist)
    
#（6）匿名函数lamdba函数的使用(python里面的lamdba功能比较弱)
'''lamdba函数省略了函数中的return，大部分功能是被用作表达式，而不是语句'''
def func_name6():
    '''1个参数'''
    func1 = lambda x:x*2
    print(func1(3)) #结果为6
    print('---------------')
    '''多个参数(可以初始化参数)'''
    func2 = lambda x,y,z=1: x+y+z
    print(func2(2,3)) #结果为6
    print(func2(2,3,4)) #结果为9
    print('---------------')
    '''也可以使用列表推导'''
    func3 = lambda x:[(x,i) for i in range (1,10)]
    print(func3(10))
    print('---------------')
    '''存放函数到列表里面'''
    info=[lambda x:x+1,lambda x:x*2]
    print(info[0](2),info[1](2))
    
#func_name6()



#（7）python3 起，filter 函数返回的对象从列表改为 filter object（迭代器）
'''filter(function or None, iterable) --> filter object'''
def func_name7():
    t=[1,2,3,4,5]
    g=filter(lambda x:x>3,t)        #t中大于3的输出。t替换前面的x（filter要求2个参数）
    '''print(g)--><filter object at 0x00000000037FD080>'''
    for item in g:
        print(item)
#func_name7()


#（8）函数关键字的匹配（和传统的位置匹配不一样）
def  func_name8():
    def func(k1='',k2=None,k3=''):
        return k1,k2,k3
    print(func(k1=4,k3=5))
    print(func(k3=5,k1=4))
    print(func(k3=5,k1=4,k2=3))
#func_name8()


#（9）函数收集匹配（元组收集和字典收集）
'''
    *kargs 元组
    **kwargs 字典（和关键词匹配原理差不多）
    参数位置：
        1.先是位置匹配的参数     func(name)
        2.再是关键字匹配的参数   func(key=value)
        3.手机匹配的元组参数     func(name,arg1,arg2)
        4.手记匹配的关键字参数   func(name,key1=value1,key2=value2)
标准形式：def fun(a,d,b=4,*kargs,**kwargs)
        
'''
def  func_name8():            
    def fun(a,*kargs,**kwargs):
        return kargs,kwargs
    print(fun(2,3,4,5,6,7,8,[1,2,3,4],{1:2,3:4}))
func_name8()





























