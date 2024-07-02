item= input("what do you want to buy: ")
amount= int (input("how many of these items would you like to purchase?"))
price= int (input("enter the price"))
if amount >0 and price >0:
    print(price*amount)