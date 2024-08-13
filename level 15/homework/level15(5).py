age= int (input("enter your age: "))
paid= int (input("enter how much you paid: "))
if age>0 and paid>0:
    if age>=60:
        print("you are eligible for the sale")
    elif paid>=100: 
        print("you are eligible for the sale")
    elif age>=60 and paid>=100:
        print("you get even a bigger sale")