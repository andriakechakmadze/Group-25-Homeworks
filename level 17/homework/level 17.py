# დავალება N1
for i in range (30):
    print("GOA is the best")

# დავალეა N2
for i in range  (5,151):
    print (i)

# დავალება N3
for i in range(2,50,4):
    print(i)

# დავალება N4
for i in range(0,11):
    print(str(i) + " GOA" )

# დავალება N5
print("ლუწი რიცხვები:")
for i in range(2, 21, 2):
    print(i)

print("კენტი რიცხვები:")
for i in range(1, 20, 2):
    print(i)

import random
target_number = random.randint(1, 100)
guessed = False

print("გამოიცანით რიცხვი 1-დან 100-მდე:")

while not guessed:
    user_guess = int(input("შეიყვანეთ რიცხვი: "))

    if user_guess == target_number:
        print("გილოცავთ! თქვენ გამოიცანით რიცხვი.")
        guessed = True
    else:
        print("არასწორია, სცადეთ ისევ.")


