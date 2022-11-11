""""Game guess the number"""

import numpy as np

number = np.random.randint(1,100) # Загадываем число

# Количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number should be less!")
    elif predict_number < number:
        print("The number should be greater!")
    else:
        print(f"You've guessed the number with {count} attempts! It's number {number}")
        break # Конец игры выход из цикла
        