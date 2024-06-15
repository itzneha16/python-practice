# # list unpacking
# my_list=['apple','banana','mango']
# my_apple=my_list[0]
# my_banana=my_list[1]
# my_mango=my_list[2]
# print(my_apple)
# print(my_banana)
# print(my_mango)

# my_list=['apple','banana','mango']
# my_apple,my_banana,my_mango=my_list
# print(my_apple)
# print(my_banana)
# print(my_mango)

# list1=[45,90,87,65]
# num1,*num2=list1
# print(num1)
# print(num2)
# print(type(num2))


# #tuple unpacking
# tup1=('apple','banana','mango')
# my_apple=tup1[0]
# my_banana=tup1[1]
# my_mango=tup1[2]
# print(my_apple)
# print(my_banana)
# print(my_mango)

# tup1=('apple','banana','mango')
# my_apple,my_banana,my_mango=tup1
# print(my_apple)
# print(my_banana)
# print(my_mango)

# dict1={'name':'neha','comment':20}

# def statment(name,comment=0):
#     if not comment:
#         return f" {name} has no comments"
#     return f"{name} has {comment} comments. "
# print(statment(**dict1))


# #list  unpacking(list contain tuple)
# list=[('user1','passward1'),
#       ('user2','passward2'),
#       ('user3','passward3')]

# user1,user2,user3=list
# print(user1)
# print(user2)
# print(user3)

# user1,passward1=user1
# user2,passward2=user2
# user3,passward3=user3
# print(user1,passward1)
# print(user2,passward2)
# print(user3,passward3)

# def create_user(username,email,password):
#     return {'username':username,'email':email,'password':password}

# dict2={'username':'neha','email':'neha@gmail.com','password':'neha12345'}

# user1=create_user(**dict2)
# print(user1)

# list_new=['swaraj','swaraj@gmail.com',78965]
# print(create_user(*list_new))

# # dictionary unpacking opretor(**)
# yellow_button={'width':200,'text':'buy'}
# red_button={ **yellow_button , 'color':'red'}
# print(red_button)
# print(yellow_button)

# # dictionary unpacking opretor
# button_style={
#     'height':210, 'width':100,'color':'red'
# }
# button_info={'text':'buy'}
# button={**button_info,**button_style}
# print(button)

person={'name':'neha','age':22}
other_person={**person,'age':30}
print(person)
print(other_person)
print(id(person)==id(other_person))








