# # #fuction for addition
# def sum(a,b):
#     c=a+b
#     print(c)
    

# sum(78,78)

# # #another fuction
# def sum(a,b):
#     a=a+1
#     c=a+b
#     return c


# res=sum(11,12)
# print(res)

# #one line function
# def mult(a,b):
#     return a*b

# res=mult(10,2)
# print(res)

#dection used in fuction
# def increase_age(person):
#     person['age'] +=1
#     return person

# person_info={'name':'neha','age':20}

# increase_age(person_info)
# print(person_info['age'])

# def person_age(person):
#     copy_person=person.copy()
#     copy_person['age'] +=1
#     return copy_person

# person1={'name':'neha','age':20}
# person2=person_age(person1)
# print(person1['age'])
# print(person2['age'])

def print_fruit_info(person_name,fruits):
    print(person_name,fruits)
    for fruit in fruits:
        print(f'{person_name} likes {fruit}')
    
name='neha'
list_fruits=['apple','banana','lime']
print_fruit_info(name,list_fruits)