def check_weight(weight):
    if weight<=0:
        print("invalid weight.....")
    
    elif 0 < weight <= 5:
        print("the shipping fee is 5rs")
    
    elif 0 < weight<=15:
        print("the shipping fee is 10rs")
        
    elif 0 < weight<20:
        print("the shipping fee is 20rs")
        
check_weight(8)
print(check_weight)

# # if statement

# color='red'
# if color=='red':
#     print("color is red")
    

# #if - else statement
# color = "pink"
# if color=='yellow':
#     print("color is yellow")
# else:
#     print("color is pink")
    
        
