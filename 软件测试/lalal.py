# import calendar
# calendar.setfirstweekday(firstweekday=6)
# print(calendar.calendar(2019, w=1, l=1, c=5))

#
# import datetime
# today = datetime.date.today()
# print (today)
# tomorrow = today + datetime.timedelta(days=1)
# print(tomorrow)
#



import datetime

flag = True
while flag:
    a = int(input("请输入年"))
    if 1900 <= a <= 2050:
        flag = False
    else:
        flag = True
        print("输入越界请重新输入一个大于1900且小于2050的数")

flag = True
while flag:
    b = int(input("请输入月"))
    if 1 <= b <= 12:
        flag = False
    else:
        flag = True
        print("输入越界请重新输入一个大于1且小于12的数")
        # b = input()

flag = True
while flag:
    c = int(input("请输入日"))
    if b == 1 or b==3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
        if 1 <= c <= 31:
            flag = False
        else:
            flag = True
            print("输入越界请重新输入一个大于0且小于31的数")
        # c = input()
    elif b == 3 or b == 4 or b == 6 or b == 9 or b == 11:
        if 1 <= c <= 30:
            flag = False
        else:
            flag = True
            print("输入越界请重新输入一个大于0且小于30的数")
            # c = input()
    elif b == 2:
        if a % 4 == 0 or a % 100 != 0:
            if 1 <= c <= 29:
                flag = False
            else:
                flag = True
                print("输入越界请重新输入一个大于0且小于29的数")
                # c = input()
        else:
            if 1 <= c <= 28:
                flag = False
            else:
                flag = True
                print("输入越界请重新输入一个大于0且小于28的数")
                # c = input()

d1 = datetime.date(a, b, c)
print(d1)
print(d1 + datetime.timedelta(+1))  # timedelta(day=0,seconds=0,microseconds=0)
