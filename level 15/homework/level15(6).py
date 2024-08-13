gpa= float (input("enter your gpa"))
familyincome= int (input("enter your family income"))
if gpa>0 and familyincome>0:
    if gpa >=3.5:
        print("you are eligible for a stipend")
    elif gpa>=3 and familyincome<50000:
        print("you are eligible for a bigger stipend")
    elif gpa<3:
        print("you are not eligible for a stipend")