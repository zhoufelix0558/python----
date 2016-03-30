'''
date:2016-3-28
-------------------
1.threading的简单应用
2.迭代的线程
3.线程的迭代-例子
4.对多线程实现的时间顺序的例子
5.互斥锁：对单个对象进行锁定，不让别的线程进行修改
6.协程入门--yield(进击的return)

'''



'''
基本知识：
每个进程用唯一标识符来标识,创造一个进程的时候，会创造一个线程，
    这个线程被称为主线程（只有一个主线程）。
python里的多线程，不是真正意义上的多线程（python 全局锁-->不停切换线程）。
多线程复杂度高，不建议使用

什么是可迭代对象？
    就是能用for i in a：一个个取出来的对象，比如a=[1,2,3,4]
'''
import threading

#（1）threading的简单应用

def func_name1():

    def test():
        print(1)
    a=threading.Thread(target = test)
    b=threading.Thread(target = test)
    a.start()
    b.start()
    
    
    a.join()
    b.join()
#func_name1()

#（2）线程的迭代
def func_name2():
    import time
    def test(p):
        time.sleep(0.001)
        print(p,'.')
    ts=[]
    for i in range(0,15):
        # python3中xrange改成了range（原本的range(10)等价于现在的list(range(10))）
        th = threading.Thread(target=test,args=[i])  #生成迭代对象个（这么多）线程
        th.start()
        ts.append(th)
    print("--pause--")
    for i in ts:
        i .join()       #join的作用，等待线程结束的时候再往下跑
    print("--end--")
        
#func_name2()



#（3）线程的迭代-例子
    '''
        一个程序的复杂度，不都分情况下，只和代码的行数有关
        应用例子：数据库线程池
    '''
def func_name3():
    global num
    num= 0
    def t():
        global num
        num+=1
        print(num)
    for i in range(10):
        d = threading.Thread(target=t)
        d.start()

#func_name3()


#（4）对多线程实现的时间顺序的例子
'''
多线程能大大降低程序运行的时间
下面的例子中：单线程运行4s，多线程2s
做爬虫的时候可能会用到多线程
'''
def func_name4():
    import time
    def a():
        print('a begin')
        time.sleep(2)
        print('a end')
    def b():
        print('b begin')
        time.sleep(2)
        print('b end')
    b_time = time.time()
    a()
    b()
    print(time.time() - b_time)
    b_time = time.time()
    _a = threading.Thread(target  = a)
    _b = threading.Thread(target  = b)
    _a.start()
    _b.start()
    _a.join()
    _b.join()
    print(time.time() - b_time)
#func_name4()



#（5）互斥锁：对单个对象进行锁定，不让别的线程进行修改
'''

'''
def func_name5():
    mlock = threading.Lock()
        #RLock()可以多次锁（有计数概念）
    global num
    num = 0
    def a():
        global num
        mlock.acquire()         #Rlock加锁（有几个加锁，就要有几个释放）
        num += 1
        mlock.release()         #释放锁
        print(num)
    for i in range(0,10):
        d=threading.Thread(target =a)
        d.start()  
#func_name5()



#（6）协程入门--yield(进击的return)
'''
yield生成器
1.包含yield的函数，则是一个可迭代对象


'''
def func_name6():
    def test():
        i = 0
        a = 4
        while i<a:
            '''
            return数字给一个可迭代对象，一块输出
            '''
            yield i
            i+=1
    for i in test():
        print(i)
    print('---****---')

    def test1():
        x=yield
        print("1.-%s"%x)
        x=yield
        print("2.-%s"%x)
        x=yield 'add yield'
        print("3.-%s"%x)
    t=test1()
    print(t)
    print(t.__next__())             #python2的next方法变成了__next__
    print(t.send('test here'))
    print(t.send(5))
'''
python 的 generator 初始化时还没有被运行。所以你直接用 a = G() 不能达到你想要
的效果，要在 a=G() 后面加一句 a.__next__() 才开始运行了。开始运行之后才能
send()。
send的数据必须有yield接受; generator还没有启动,是不能对它send数据的,
只能send(None),也就是next()了 
'''
func_name6()

























