#在希望输入时使用input()函数，但是在输入时默认为String类型，所以需要在之前加上int()来转换类型 如:
a = 1
int(input(a))
# 需要输出错误时使用try exexp来输出 如：
try:
     print("正常执行""=)
except AttributeError:
     print("错误1:)
except ImportError:
    print("错误类型2)
finally:#需要注意的是在次语句之后的代码是正常执行的，并不会收到上面的干预
    print("xxxxxxx")
#还有
def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行
# try:
#     正常逻辑
# except Exception,err:
#     触发自定义异常
# else:
#     其余代码
# 实例
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2
# 输出结果
# 1 Invalid level!


#还有datetime.date有点厉害