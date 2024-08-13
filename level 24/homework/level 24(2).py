# 4) დავალება დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს ქულები შუალედური გამოცდისთვის, დასკვნითი გამოცდისთვის და პროექტისთვის. დარწმუნდით, რომ მომხმარებელმა შეიყვანოს სწორი ქულები (პოზიტიური რიცხვები 0-დან 100-მდე) თითოეული კომპონენტისთვის.გამოიყენეთ შემდეგი შეფასების კრიტერიუმები: თუ საშუალო ქულა (20% შუალედური კურსისთვის, 40% საბოლოო და 40% პროექტისთვის) არის 70 ან მეტი, სტუდენტი გაივლის კურსს. თუ საშუალო ქულა 70-ზე დაბალია, სტუდენტი ვერ ახერხებს კურსის ჩაბარებას. აჩვენეთ მომხმარებლისთვის შეტყობინება, რომელშიც მითითებულია მისი გავლის/ჩავარდნის სტატუსი და გამოთვლილი საშუალო
gamocda=int(input("enter your score"))
if gamocda>100 or gamocda<0:
    print("you cant have less then 0 or more then 100")
else :
    gamocda=gamocda
gamocda2=int(input("enter your score"))
if gamocda2>100 or gamocda2<0:
    print("you cant have less then 0 or more then 100")
else :
    gamocda2=gamocda2
project=int(input("enter your score"))
if project>100 or project<0:
    print("you cant have less then 0 or more then 100")
else :
    project=project

sedegi=(gamocda+gamocda2+project)/3
if sedegi>70:
    print("you passed")
else :
    print("you faild")