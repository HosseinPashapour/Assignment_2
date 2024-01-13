import random

print("Tas Bendaz !🎲")

while 1 == 1:
    computer_choice= random.randint(1,6)
    user_choice= int(input("You:"))
    print("💻:" , computer_choice)

    if computer_choice==6:
        print("Yek bar dighe Bendaz")
        computer_choice= random.randint(1,6)
        user_choice= int(input("You:"))
        print("💻:" , computer_choice)
        print("End game")
       
        break
  
    else:
        print("Next round!")