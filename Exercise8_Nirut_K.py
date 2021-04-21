UserInput = input("Username : ")
PasswordInput = input("Password : ")
if UserInput == "admin" and PasswordInput == "1234" :
    print("Done")
    print("---------Welcome to Monkey Shop---------")
    print("List product")
    print("1. Pepsi     x1     20 THB")
    print("2. Lays      x1     30 THB")
    print("3. Bakery    x1     40 THB")

    print("Please select product")
    UserSelected = int(input(">>"))
    Number = int(input("number : "))

    if UserSelected == 1 :
        print("Pepsi x",Number, "=", Number * 20, "THB" )
    elif UserSelected == 2 :
        print("Lays x",Number, "=", Number * 30, "THB" )
    elif UserSelected == 3:
        print("Bakery x", Number, "=", Number * 40, "THB")
    else:
        print("No product as you select")
else:
    print("Username or Password invalid !!!")