fruits=('apple','banana','lime','mango')
fruit_name=('banana','mango','apple','lime')
print(fruits)
print(id(fruits))
print(fruits[1])
print(fruits == fruit_name)

name1="neha"
name2="shravani"
name3="sanika"
name4="nikita"
all_name=(name1,name2,name3,name4)
print(all_name)

numbers=(88,56,76,88,20,19,56,88)
print(numbers.count(88))
print(numbers.index(56))

tup1=(203,198,873,490)
print(tup1)
list1=list(tup1)
print(list1)
list1.append(111)
print(list1)
orignal_tup=tuple(list1)
print(orignal_tup)


tuple1=(198,987)
tuple2=(True,'hi',10.7)
line=tuple1 + tuple2
print(line)

