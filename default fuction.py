# def multiplication(num1,num2=2): # num2 contain default value
#     return num1*num2

# print(multiplication(20,10))
# print(multiplication(20))

from datetime import date

def get_weekday():
    return date.today().strftime('%A')

print(get_weekday())

def new_post(post,weekday=get_weekday()):
    copy_post=post.copy()
    copy_post['create_on_weekday']=weekday
    return copy_post

initial_post={'id':254 , 'authod':'swaraj'}
print(new_post(initial_post))
    