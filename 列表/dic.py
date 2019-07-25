cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))
cleese['Name'] = 'John Cleese'
cleese['Occuptions'] = ['actor','comedian']
palin = {'Name':'Michael Palin','Occuptions':['actor','comedian']}
print(palin['Name'])#使用括号中的索引来访问数据项，不过括号内不是数字而是用键做索引
print(cleese['Occuptions'][-1])#索引串链，从右向左读
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min,sec) = time_string.split(splitter)#拆分方法，拆分器，按照上面的‘-’‘：’来拆分时间
    return (min + '-' + sec)
def get_data(filename):
    try:
        with open (filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return  ({'Name':templ.pop(0),
                  'Dob':templ.pop(0),
                  "Times":str(sorted((set([sanitize(t) for t in templ]))))})
    except IOError as ioerror:
        print('File error :'+set(ioerror))
        return (None)

    james = get_data('james2.txt')
    print(james['Name']+"'s faster  times are :"+ja,james['Times'])