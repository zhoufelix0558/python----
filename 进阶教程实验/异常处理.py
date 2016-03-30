'''
1.try except常见格式
2.with 方法的使用
3.自己去定义异常

'''

#a=[1,2,3,4,5,6],a[6]        #IndexError


#（1）try except常见格式
'''
捕获某种特定的异常：
    except IOError：
        ...
打印错误类型的信息：
    except IOError as e:
        print(e)

'''
def func_name1():
    try:                                #存放易抛出异常的代码                                
        a+b
    except:                             #抛出错误时要执行的代码
        print("error")
    else:                               #没错误的时候执行的代码
        print("right")
    finally:                            #都会执行
        print("you will get here")

#func_name1()


#with方法的使用

def func_name2():
    '''
    d=open("a","r")
    d.read()
    d.close()
    等价于：
    with open("a","r") as a:
        e=a.read()              #with语句不用写close，因为他能自动处理
    进入时，调用对象的__enter__
    退出时，调用对象的__exit__
注意：
    对象没有__enter__，__exit__这两个方法就不能使用with方法

    '''
    #with方法的一种实现
    class sth(object):
        def __init__(self,haha):
            self.a=haha
        def __enter__(self):
            print("进来了")
            return self.a                           #写成a了，结果报出错误“没定义参数”
        def __exit__(self,type,value,traceback):    #这几个参数不能漏
            print("出去了")
    with sth("hello") as s:                         #s是__enter__的返回值
        print(s)
#func_name2()


#（3）自己定义异常
def func_name3():
    class myException(Exception):
        def __init__(self,error,msg):
            self.args = (error,msg)
            self.error = error
            self.msg = msg
    try:
        raise myException(1,"my exception message")
    except Exception as e:
        print(e)
func_name3()        













































