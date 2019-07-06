#导入模块，使用dump（）保存数据，以后某个时间使用load（）恢复数据，唯一的要求是必须以二进制访问模式打开这些文件
import pickle
import os
os.getcwd()
os.chdir('D:\\git的东西\\How-baby-learn-python\\txt文件')
man = []
other = []
try:
    with open('man_data.txt','wb')as man_file,open('other_data.txt','wb')as other_file:
        pickle.dump(man,man_file)#将之前的print_lol改成了pickle.dump
        pickle.dump(other,other_file)
except IOError as err:
    print('File error'+ str(err))
except pickle.PickleError as perr:
    print('Pickling error' + str(perr))
