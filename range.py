my_range=range(8)
print(my_range)
print(type(my_range))
print(list(my_range))

ran1=range(5,20,5)
print(type(ran1))
print(ran1)
print(list(ran1))

ran1=range(5,20,5)
for n in ran1:
    print(n)

#multiplication table
num=int(input("Enter any number : "))
i=1
while(i<11):
    print(i*num)
    i+=1


range_1=range(1,100,2)
print(range_1.start)
print(range_1.stop)
print(range_1.step)
print(list(range_1))
print(tuple(range_1))
print(set(range_1))
# range cant not convert into dict # print(dict(range_1))

odd_num=range(1,50,2)
print(odd_num.index(47))
print(list(odd_num))