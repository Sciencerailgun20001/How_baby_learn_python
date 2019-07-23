cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))
cleese['Name'] = 'John Cleese'
cleese['Occuptions'] = ['actor','comedian']
palin = {'Name':'Michael Palin','Occuptions':['actor','comedian']}
print(palin['Name'])#使用括号中的索引来访问数据项，不过括号内不是数字而是用键做索引
print(cleese['Occuptions'][-1])#索引串链，从右向左读