
"""Игра угадай число.
    Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток.
    Механизм реализации:
    Случайно выбираем число от 1 до 100. Считаем количество попыток для его нахождения и кладём в список. 
    Так делаем 1000 проходов. Затем из 1000 результатов считаем среднее количество попыток.
"""

import numpy as np
import statistics


def random_predict(number: int=1) -> int:
    """Угадываем число ограничивая рамки подбора
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # счётчик попыток угадывания числа
    min, max = 1, 100 # начинаем новую итерацию поиска числа между 1 и 100
    predict_number = max / 2 # сразу начнём поиск с деления всех вариантов пополам

    while number != predict_number:
        count+=1
        
        if number > predict_number: 
            min = predict_number + 1
        elif number < predict_number: 
            max = predict_number - 1

        predict_number = round((max + min ) / 2) # разбиваем пополам новые рамки поиска
    return(count)
 

def avg_attempt(number: int=1000) -> int:
    attempt_ls = [] # список-хранилище количества попыток угадывания числа
    
    for i in range(1, number+1):
        predict = np.random.randint(1, 100)
        attempt_ls.append(random_predict(predict))
    
    # score = int(round(np.mean(attempt_ls))) # посчитать можно  с помощью numpy или statistics
    score = int(round(statistics.mean(attempt_ls)))
    return(score)


# score = avg_attempt(20) # Можно задать количество проходов, по умолчанию 1000
score = avg_attempt()
print(f"Ваш алгоритм угадывает число в среднем за количество попыток: {score}")
