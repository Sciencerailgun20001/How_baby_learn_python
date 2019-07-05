import os
os.getcwd()#获取文件所在文件夹
print(os.getcwd())
os.chdir('D:\\qq文件\\1877149913\\FileRecv\\untitled\\txt文件')#更改为指定的文件夹，注意每个文件夹之间要用\\隔开而不是\
os.getcwd()
print(os.getcwd())
try:
    data = open('sketch.txt')

#print(data.readline(),end='')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print(' said:' ,end='')
            print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('this data file is missing!')
