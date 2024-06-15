def num_info(num):
    if (num%2)==0:
        print(f"{num} is evan number")
    else:
        print(f"{num} is odd number")
        
def process_num(num,callback_fn):
    callback_fn(num)
    
num=int(input("Enetr the number : "))
process_num(num,num_info)

# def send_data(data):
#     pass

# def process_data(input_data,callback_fn):
#     update_data=input_data.copy()
#     callback_fn(update_data)
    
# process_data({'name':'neha'},send_data)