import math

flag = True
while flag :
    try:
        First = int(input('请输入三角形的第一边长:'))
        Second = int(input('请输入三角形的第二边长:'))
        Third = int(input('请输入三角形的第三边长:'))
        if (First is None or Second is None or Third is None):
            print("请输入数据")


        if (First > 0 and Second > 0 and Third > 0) :
            if(First < 100 and Second < 100 and Third <100) :
                flag = False
            else:
                flag = True
                print('输入的三边边长必须要小于100，请重新输入！\n')
        else :
            flag = True
            print('输入的三边边长必须要大于0，请重新输入！\n')
    except ValueError:
        print("1")
        flag = True
        print("输入非法")


# 从小到大排序，并赋值给a、b、c
a = min(First, Second, Third)
c = max(First, Second, Third)
if (First != a and First != c) :
    b = First
elif(Second != a and Second != c) :
    b = Second
else :
    b = Third
print('该三角形三边边长分别为%0.2f, %0.2f, %0.2f' % (a, b, c))
print('\n')

# 判断三边是否能构成三角形
if ( a+b > c and c-a < b and c-b < a ) :

    # 根据三边关系，判断三角形形状并求取其面积
    if (a == b == c) :
        print('该三角形为等边三角形')
    elif (a == b or b == c or a == c) :
        C = (a+b+c) / 2
        print('该三角形为等腰三角形' )
    elif ( a**2 + b**2 == c**2 ) :

        print('该三角形为直角三角形' )
    else :
        print('该三角形为一般三角形' )
else :
    print('当a = %0.2f, b = %0.2f, c = %0.2f为三边长时，不能构成三角形 ！' % (a, b, c))
