# -*- coding: utf-8 -*-
'''
1.pass语句
2.三元表达式
3.空函数的返回值
4.直接调用函数不现实return值
5.任意多数字求和的实现
6.可选参数与必选参数
7.参数类型检查
8.断言：assert 最常用的测试方法
'''


'''
python中break、continue和pass之间的区别：
    break:循环结构中执行时，会立即跳出循环结构，转而执行该结构后面的语句
    continue：立即结束本次循环，重新开始下一轮循环
    pass：该语句什么也不做（空操作）
break、continue只能在do/for/while语句中才有效
'''

#（1）空函数和pass语句
#pass充当占位符，此例输出"nicko"
def func_name1():
    pass
    print("nicko")
#func_name1()


#（2）三元表达式(和其他语言不同):为真时的结果 if 判定条件 else 为假时的结果 
def func_name2():
    print(1 if 5>3 else 0)
#func_name2()


#（3）空函数的返回值type 'NoneType'
def func_name3():
    test=func_name1()
    print(type(test))
    print(test==None)
#func_name3()


'''直接调用函数的时候，只执行函数，不输出返回值
    用print函数的时候既执行函数，又输出返回值(函数没有return的话返回None)
    此例返回：
        nicko
        -----------
        nicko
        None
'''
#（4）使用print函数：不仅执行函数，而且返回函数的return值（无论是否是None）
def func_name4():
    func_name1()
    print("----------")
    print(func_name1())
#func_name4()


#（5）任意多数字和
#*num会让元素变成turple
def add(*num):
    #print(type(num))
    d=0
    for i in num:
        d+=i
    return d
#print(add(1,2,3,4,5,6))


'''
可选参数：有默认值
必选参数：没有默认值
区别："="
'''
#（6）可选参数调用的时候不写也没有关系
def add1(num1,num2=3):
    return num1+num2
def func_name6():
    print(add1(3))
    print(add1(3,9))
#func_name6()
    

#（7）参数检查，提高函数的健壮性
def func_name7(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        return num1+num2
    else:
        return "error"
#print(func_name7(1,2),func_name7(1,'2'))
    

#（8）断言assert：测试返回值或者表达式是不是你想要的结果
#结果正确不执行任何操作，错误的话返回AssertionError
def func_name8():
    assert func_name7(1,2)==3
    assert func_name7(1,2)==4
#func_name8()







