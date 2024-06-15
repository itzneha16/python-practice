def update_car_info(**car):
    print(update_car_info)
    print(type(update_car_info))
    title=car['brand']
    money=car['price']
    statment=car['is_available']
    print(f"my car name is {title} , its cost is {money} $ and it is {statment} that it run faster than other vehicle")
  

update_car_info(brand='audi', price=2000, is_available=True)

