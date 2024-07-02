number= int(input("enter a number between 1-1000: "))
if number>1 and number<1000:
    number2= int(input("guess the number"))
    if number2==number:
        print("correct")
    elif number2 != number:
        print("incorrect")
else:
    print("the entered number has to be in between 1 and 1000")