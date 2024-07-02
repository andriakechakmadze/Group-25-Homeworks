weight= int (input("enter your weight"))
height= float (input("enter your height"))
bmi= weight/(height*height)
if bmi<18.5:
    print("underweight")
elif bmi>18.5 and bmi <24.9:
    print ("normalwheight")
elif bmi>25 and bmi<29.9:
    print("overwheight")
elif bmi>30:
    print("obese")