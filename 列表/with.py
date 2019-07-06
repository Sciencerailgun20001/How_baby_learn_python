import  os
import sys
os.getcwd()
os.chdir('D:\\git的东西\\How-baby-learn-python\\txt文件')#更改为指定的文件夹，注意每个文件夹之间要用\\隔开而不是\
# try:
#     with open('its.txt','w')as data:#使用with不用考虑关闭打开文件，py会自动为你考虑的
#         #用了with就不需要filally组了
#         print("It's...",file = data)
# except IOError as err:
#     print('file error '+str(err))
man = []
other = []
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):#增加第4个参数，并指定缺省值
    for each_item in the_list:
        if isinstance(each_item,list):#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
            print_lol(each_item,indent,level+1,fh)#注意：签名已经改变
        else:
            if indent:#格式化工具（大概）
                for tab_stop in range(level):
                    print('\t',end='',file=fh)#调整两个print（）调用这
            print(each_item,file=fh)#           来实现这个新参数

try :
    data = open ('sketch.txt')
    for each_line in data:
        try:#try except 语句就是先执行try中的东西，如果能运行成功的话就继续，如果不行就进入except
            (role,line_spoken) = each_line.split(':',1)#split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串,这条语句就是将带有：的句子分成两部分
            line_spoken = line_spoken.split()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()#完成读操作之后一定要。close不然会出错
except IOError:
    print('the data is missing')
try:
    with open('man_file.txt','w')as man_file,open('other_data.txt','w')as other_file:
        print_lol(man,fh=man_file)
        print_lol(other,fh=other_file)
except IOError as err:
    print('file error' + str(err))

