number = int(input("Please input number : "))
for x in range(number):
    print(" "*(number-x) + "*"*((x+1)+x))