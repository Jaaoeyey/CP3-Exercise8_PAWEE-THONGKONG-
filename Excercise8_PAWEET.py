usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "PaweeT" and passwordInput == "1234":
    print("Welcome :)")
    print("----------Have A Good day Cafe----------")
    print("What would you like to order?")
    print("1.Coffee")
    print("2.Bakery")
    userselected = int(input(">>"))
    if userselected == 1:
        print("1.Americano")
        print("2.Cappuccino")
        print("3.late")
        coffeeselected = int(input(">>"))
        if coffeeselected ==1:
            print("How many cups of coffee do you get?")
            cups = int(input(">>"))
            pricecoffee = cups * 50
            print("Total: ", pricecoffee, "THB")
        elif coffeeselected ==2:
            print("How many cups of coffee do you get?")
            cups = int(input(">>"))
            pricecoffee = cups * 55
            print("Total: ", pricecoffee, "THB")
        elif coffeeselected ==3:
            print("How many cups of coffee do you get?")
            cups = int(input(">>"))
            pricecoffee = cups * 60
            print("Total: ", pricecoffee, "THB")
    elif  userselected == 2:
        print("1.Strawberry Cake")
        print("2.Donut")
        bakeryselected = int(input(">>"))
        if bakeryselected ==1:
            print("How many strawberry cake would you like?")
            cake = int(input(">>"))
            pricebakery = cake * 95
            print("Total: ", pricebakery, "THB")
        elif bakeryselected ==2:
            print("How many Donut would you like?")
            donut = int(input(">>"))
            pricebakey = donut * 65
            print("Total: ", pricebakey, "THB")
else:
    print("Please enter your new username and password")