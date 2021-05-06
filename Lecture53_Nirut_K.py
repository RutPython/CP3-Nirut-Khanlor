def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
totalPrice = float(input("Please input price (THB) "))
print("Price including VAT =", vatCalculate(totalPrice),"THB")