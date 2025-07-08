import random
continue_game = "yes"

while continue_game == "yes":
    random_number = random.randint(1, 100) 
    answer = input("Guess a number between 1 and 100 : ")

    while True:
        try:
            answer = int(answer)
            break
        except ValueError:
            answer = input("This answer is not valid, try again : ")

    while answer != random_number:
            if answer < random_number:
                answer = print("Higher")
            else: 
                answer = print("Lower")
            while True :
                try:
                    answer = int(input("Your guess : "))
                    break
                except ValueError:
                    print("This answer is not valid, try again")         
    
    print("Congrats you found the number : ", random_number)
    continue_game = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")