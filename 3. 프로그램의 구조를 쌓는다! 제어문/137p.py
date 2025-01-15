coffee = 10

while True:
    money = int(input("Pleas put money in."))

    if money == 300:
        print("Serving coffee...")
        coffee = coffee - 1
    elif money > 300:
        print("Serving coffee... Change is %d won." %(money - 300))
        coffee = coffee - 1
    else:
        print("Not enough money.")
        print("There is(are) %d cup(s) of coffee left." %coffee)
    
    if coffee == 0:
        print("Coffee has run out.")
        break