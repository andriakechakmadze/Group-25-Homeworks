# 2)  დავალება
#ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე.
#პროგრამის დანიშნულება არის ის, რომგამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს.

while True : 

    number = int (input("enter number"))
    
    if number > 100:
        print("you number is over 100 it shoud be under 100")
    elif number < 0:
        print("your number needs to be more then 0")
    elif number == 70:
        print("our numbers match")
        break
    else : 
        print("try again")