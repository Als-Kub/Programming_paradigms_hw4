# Задача №1
# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки 
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между 
# двумя случайными величинами (двумя массивами). Можете 
# использовать любую парадигму, но рекомендую использовать 
# функциональную, т.к. в этом примере она значительно 
# упростит вам жизнь.




import math


def pearson_correlation(arr_1, arr_2):

    # Проверка на равную массивы одинаковой длины
    if len(arr_1) != len(arr_2):
        raise ValueError("Error - Different length of arrays")

    n = len(arr_1)

    # Расчет среднего значения
    mean_x = sum(arr_1) / n
    mean_y = sum(arr_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in arr_1]) / float(len(arr_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in arr_2]) / float(len(arr_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(arr_1, arr_2)]) / float(len(arr_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [2, 4, 6, 8]
array_2 = [2, 4, 10, 12]

correlation = round(pearson_correlation(array_1, array_2), 3)
print(f"Pearson correlation coefficient: {correlation}")