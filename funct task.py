# def merge_list_to_dict(list1,list2):
#     main=zip(list1,list2)
#     dict1=dict(main)
#     print(dict1)
 
# name=['neha','swaraj','nikita']
# age=[21,18,24]
# merge_list_to_dict(name,age)

# def sum_function(*args):
#     print(args)
#     print(type(args))
#     print(args[0])
#     return sum(args)

# print(sum_function(2,5,7,8,9))

# def sort_element(*args):
#     return sorted(args)

# print(sort_element(22,90,10,55,39,100 ))

#keyword argument
def information(name,sub):
    print(information)
    print(type(information))
    line=(f'i am {name} and im learning {sub}')
    return line

line=information(name='neha', sub='python')
print(line)

    




# def  post_info(**person):
#     print(person) #print dictionaries
#     print(type(person))
#     info=(f"{person ['name']} wrote"
#           f"{person ['num']} posts")
#     return info

# info=post_info(name='neha',num=98)
# print(info)