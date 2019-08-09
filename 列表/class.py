# class Athlete:
#     def __init__ (self, a_name, a_dob=None, a_times=[]): #__init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用；
#         self.name = a_name#初始化3个属性，使用所提供的参数数据，为这三个类属性赋值
#         self.bod = a_dob
#         self.time  = a_times

# 在python中使用__开头 并以__结尾的方法，称之为魔法方法；
# __init__(self) 是类的初始化方法，也称构造方法，是一种特殊的魔法方法。
# __init__(self)在实例化后，会自动调用，而不用手动调用，所以一般把属性设置在_init__()里。
# 常用到的魔法方法还有：__str__(self) 、 __del__(self)等。

## __str__(self)
# class student(object):
#     # 定义构造方法
#     def __init__(self, n, a):
#         # 设置属性
#         self.name = n
#         self.age = a
#
#     # 输出一个字符串(追踪对象属性信息变化)
#     def __str__(self):  # __str__(self)不可以添加参数(形参)
#         return "名字：%s 年龄：%d" % (self.name, self.age)
#
#
# # 实例化一个对象john
# john = student("约翰", 19)
#
# # 当使用print输出对象时，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
# print(john)

#上面的那个算得上是定制类了，他的问题在于每次的更新都需要重新写类，下面的这个则属于继承类，好处就是emmmmmmmm反正就是好

class Athletelist(list):#继承内置的list
     def __init__(self,a_name,a_dob=None,a_times=[]):
         list.__init__([])
         self.name = a_name#初始化3个属性，使用所提供的参数数据，为这三个类属性赋值
         self.bod = a_dob
         self.extend(a_times)
     def top3(self):
        return (sorted(set([sanitize(t)for t in self]))[0:3])
def sanitize(time_string):
         if '-' in time_string:  # 使用in检测是否包含特殊字符
             splitter = '-'
         elif ':' in time_string:
             splitter = ':'
         else:
             return (time_string)  # 如果不需要清理就啥也不干
         (mins, secs) = time_string.split(splitter)  # 分解字符串，抽出分和秒
         return (mins + '.' + secs)
# sarah = Athletelist('Sarah Sweeney', '2002-6-17', ['2:58','2.58','1.56'])
# james = Athletelist('James Jones')#创建两个选手
# print(type(sarah))#确认俩人都是选手
# print(type(james))
# print(sarah)#显示计算机山的他俩的地址
# print(james)
# print(sarah.name)
# print(james.name)
# print(sarah.bod)
# print(james.bod)
# print(sarah.time)
# print(james.time)

vera = Athletelist('Vera Vi')
vera.append('1.30')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])

print(vera.top3)
#注意：不同于c++，对于python，是没有静态非静态的概念的
#https://blog.csdn.net/zhc_24/article/details/82026024c++与python类的区别来自这里