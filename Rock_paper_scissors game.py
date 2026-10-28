import random
choice = ["rock", "paper", "scissors"]
user_score=0
computer_score=0
while True:
    user_input=input("select between rock, paper, scissors: ")
    if user_input not in choice:
        print("Invalid input")
        continue
    computer=random.choice(choice)
    print(f"You selected: {user_input}")
    print(f"computer selected: {computer}")
    if user_input==computer:
        print("It's a tie!")
        print("----------------------")
    elif user_input== "rock" and computer== "scissors":
        print("You win!")
        print("----------------------")
        
        user_score+=1

    elif user_input== "paper" and computer== "rock":
        print("You win!")
        print("----------------------")
        
        user_score+=1

    elif user_input== "scissors" and computer== "paper":
        print("You win!")
        print("----------------------")
        
        user_score+=1
    else:
        print("You Lost, Better Luck Next Time!")
        computer_score+=1
    print("----------------------")
    print(f"User score is: {user_score}")
    print(f"Computer score is: {computer_score}")
    print("----------------------")
    play_again= input("Do you want to play again? (yes/no): ").lower()
    if play_again=="no":
            break
print(f"User Final Score is {user_score}")
print(f"Computer Final Score is {computer_score}")
print("Thanks for Playing!")