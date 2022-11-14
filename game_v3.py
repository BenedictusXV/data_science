import numpy as np

predict_number = np.random.randint(1,100) # Загадываем число

# Количество попыток

def random_predict (number:int=1)-> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток"""
    
    count = 0
    number=np.random.randint(1, 101) #Предполагаемое число
    limit_a=0
    limit_b=0
    while True:
        count+=1
        if number > predict_number:
            limit_b = number
            number = (limit_b - limit_a)//2
        elif number < predict_number:
            limit_a = number
            number = (limit_a + limit_b)//2
        elif number == predict_number:        
            break
       
    return(count)

def score_game(random_predict)->int:
    """За какое количество попыток из 1000 подходов наш алгоритм в среднем угадывает число
    
    Args:
    random_predict([type]): функция угадывания
    
    returns:
    int: Среднее количество попыток"""
        
    count_ls=[] # Список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score=int(np.mean(count_ls)) # находим среднее количество попыток

    print(f"Ваш алгоритм в среднем угадывает число за {score} попыток")
    return score

score_game(random_predict)