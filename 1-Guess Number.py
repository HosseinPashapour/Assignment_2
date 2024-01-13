import random

computer_choice = random.randint(10,25)
guess_number = 0

for i in range(5):
    user_choice = int(input("Please enter your guess:"))

    if computer_choice > user_choice:
        print("go up")
        print("⬆️")
        guess_number = guess_number+1

    elif computer_choice < user_choice: 
        print("go down")
        print("⬇️")
        guess_number = guess_number+1

    elif computer_choice == user_choice:
        print("🎉🎉🎉🎉🎉 Y o u W i n !! 🎉🎉🎉🎉🎉")
        guess_number = guess_number+1
        break

print("The number of your guesses:" , guess_number)