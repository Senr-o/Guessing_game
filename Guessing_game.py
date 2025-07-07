import random

random_number = random.randint(1, 100) 
answer = input("devinez un nombre entre 1 et 100: ")

while True:
    try:
        answer = int(answer)
        break
    except ValueError:
        answer = input("ce n'est pas un nombre valide, essayez encore: ")

while answer != random_number:
    try:
        if answer < random_number:
            answer = int(input("plus grand:  "))
        elif answer > random_number:
            answer = int(input("plus petit:  "))
    except ValueError:
        answer = input("ce n'est pas un nombre valide, essayez encore: ")
    
print(f"""bravo vous avez trouvé le nombre, {random_number}
merci d'avoir joué""")
