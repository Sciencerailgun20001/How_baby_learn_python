import os
os.getcwd()
os.chdir('D:\\git的东西\\How-baby-learn-python\\txt文件')#更改为指定的文件夹，注意每个文件夹之间要用\\隔开而不是\

def sanitize(time_string):
    if '-'in time_string:#使用in检测是否包含特殊字符
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)#如果不需要清理就啥也不干
    (mins, secs) = time_string.split(splitter)#分解字符串，抽出分和秒
    return (mins + '.' + secs)
# with open ('james.txt')as jaf:
#     data = jaf.readline()
# james = data.strip().split(',')#strip()应用到data中的数据行 会去除字符串所不想要的空白符
# #之后，split（','）会创建一个列表，所得到的的列表在用到以上代码中的标识符
# #这种方式可以吧多个方法串链在一起，生成所需的结果最好从左向右读
# with open ('julie.txt')as juf:
#     data = juf.readline()
# julie = data.strip().split(',')
# with open ('mikey.txt')as mif:
#     data = mif.readline()
# mikey = data.strip().split(',')
# with open ('sarah.txt')as saf:
#     data = saf.readline()
# sarah = data.strip().split(',')

def get_data (filename):
    try:
        with open(filename) as  f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return (None)
sarah = get_data('sarah.txt')#注意文件名要用引号引起来
julie = get_data('julie.txt')
mikey = get_data('mikey.txt')
james = get_data('james.txt')


# clean_james = []#创建4个全新的列表
# clean_julie = []
# clean_mikey = []
# clean_sarah = []

# for each_t in james:
#     clean_james.append(sanitize(each_t))#取原数据进行清洗，放入新的列表里
# for each_t in julie:
#     clean_julie.append(sanitize(each_t))
# for each_t in mikey:
#     clean_mikey.append(sanitize(each_t))
# for each_t in sarah:
#     clean_sarah.append(sanitize(each_t))

clean_james = [sanitize(t) for t in james]#创建4个全新的列表,使用更加简单的方法来清洗数据
clean_julie = [sanitize(t) for t in julie]#格式为clean = [sanitize(t) for each_t in what]sanitize可以制定一个转换
clean_mikey = [sanitize(t) for t in mikey]
clean_sarah = [sanitize(t) for t in sarah]

# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
