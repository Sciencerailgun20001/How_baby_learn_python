name = ['zhangsan','lisi',[1,2]]
# help(input)
# for each_item in name:
#     if isinstance(each_item,list):
#         for nested_item in each_item:
#             print(nested_item)
#     else:
#         print(each_item )
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(name)