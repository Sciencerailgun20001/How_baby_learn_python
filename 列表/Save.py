import  os
os.getcwd()
os.chdir('D:\\git的东西\\How-baby-learn-python\\txt文件')#更改为指定的文件夹，注意每个文件夹之间要用\\隔开而不是\
man = []
other = []
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
    """
    使用访问模式w时，python会打开指定的文件来完成写。
    如果这个文件已经存在，则会清空它现有的内容，也就是完全清除
    要追加一个文件就要访问模式a。要打开一个文件来完成读和写（不清除）
    需要使用W+。如果想打开有个文件来完成写，但是这个文件不存在，那么首先会为你创建
    一个文件，然后再打开文件进行写
    """
try:
    man_file = open('man_data.txt','w')#打开文件赋值一个文件对象
    other_file = open('other_data.txt','w')
    print(man,file = man_file)#使用print（）将指定的列表保存在指定的磁盘文件
    print(other,file = other_file)
    # man_file.close()#不要忘了关闭文件，但是如果上面的代码出错了将会跳过这两行
    # other_file.close()

except IOError:
    print('file error')
finally:#使用finally语句可以避免在try中出现错误而不去执行将在执行try的最后执行finally 这样就不怕没关文件了
    man_file.close()
    other_file.close()