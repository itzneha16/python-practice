#lenght function
list1=['apple','mango','lime','chiku']
print(len(list1))
print(list1[0])

#append method
list=[]
list.append(202)
list.append(201)
list.append(2038)
list.append(378)
print(list)

#pop method
input=[True, 'hi', 103 , 10.3]
input.pop()
print(input)

input.pop(1)
print(input)

delete = input.pop()
print(delete)
print(input)

#sort method
list=[33,99,45,87,12,78,10]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#string convert into list
line="string convert into list"
list1=list(line)
print(list1)

#dictionary convert into list
dic = { 'name':'Neha', 'surname':'shinde', 'Mom_name':'sarika'}
list2=list(dic)
print(list2)


#Arithmetic operation in list
list=[2.5,5.0,4.3,3.7]
print(max(list))
print(min(list))
print(sum(list))
print(sum(list)/len(list))