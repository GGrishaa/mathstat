import math
import random
import json
import matplotlib.pyplot as plt
import numpy as np


def log_summa(t, m):
    s = 0
    for i in range(1, int(m) + 1):
        s += (t ** i) / i
    return s


def log_function(x, t):
    try:
        return -1 / math.log(1 - t) * log_summa(t, x)
    except ZeroDivisionError:
        return 0


def uni_function(x, t):
    if x < 0:
        return 0
    elif x > t:
        return 1
    else:
        return x/t


def uniform():
    return random.random()


def quantil(gamma, theta):
    if gamma < 0:
        return -1
    elif gamma == 0:
        return 1
    elif gamma >= 1:
        return 999999999
    else:
        q = 1
        while True:
            if log_function(q, theta) >= gamma:
                return q
            else:
                q += 1


def emperic_function(sample, t):
    s = 0
    n = len(sample)
    for i in sample:
        if i < t:
            s += 1
    s /= n
    return s


def act1():
    theta = float(input("Введите значение параметра в интервале от 0 до 1:\t"))
    if theta >= 1 or theta <= 0:
        print("Параметр не может принимать такое значение")
    else:
        gamma = float(input("Введите уровень квантиля:\t"))
        ans = quantil(gamma, theta)
        if ans == -1:
            print("Нет квантиля такого уровня")
        elif ans == 1:
            print(f'Квантиль уровня {gamma} равен 1')
        elif ans == 999999999:
            print(f'Квантиль уровня {gamma} равен бесконечности')
        else:
            print(f'Квантиль уровня {gamma} равен {ans}')


def act2(theta):
    u = uniform()
    return quantil(u, theta)


def act3(theta):
    u = uniform()
    return theta * u


def act5():
    theta = 31 / 37
    sample_sizes = [5, 10, 100, 200, 400, 600, 800, 1000]
    num_samples = 5

    result = {
        "parameter": theta,
        "samples": {}
    }

    for n in sample_sizes:
        result["samples"][str(n)] = {}
        for sample_num in range(1, num_samples + 1):
            logarithmic_sample = [act2(theta) for _ in range(n)]

            result["samples"][str(n)][str(sample_num)] = logarithmic_sample

    filename = "log_samples.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def act6():
    theta = 34
    sample_sizes = [5, 10, 100, 200, 400, 600, 800, 1000]
    num_samples = 5

    result = {
        "parameter": theta,
        "samples": {}
    }

    for n in sample_sizes:
        result["samples"][str(n)] = {}
        for sample_num in range(1, num_samples + 1):
            uniform_sample = [act3(theta) for _ in range(n)]

            result["samples"][str(n)][str(sample_num)] = uniform_sample

    filename = "uni_samples.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def act7(filename, n, i):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sample = data["samples"][n][i]
    return sample


mode = input("Введите режим работы:\t")
while mode != "-1":
    if mode == "1":
        act1()
    elif mode == "2":
        print(uniform())
    elif mode == "3":
        n = int(input("Сколько элементов должно быть в выборке? Введите натуральное число:\t"))
        if n < 1:
            print(f'Нельзя сгенерировать выборку из {n} элементов')
            continue
        theta = float(input("Введите значение параметра для логарифмического распределения в интервале от 0 до 1:\t"))
        if theta <= 0 or theta >= 1:
            print(f'Логарифмическое распределение не может иметь параметр {theta}')
            continue
        for i in range(n - 1):
            print(act2(theta), end=', ')
        print(act2(theta))
    elif mode == "4":
        n = int(input("Сколько элементов должно быть в выборке? Введите натуральное число:\t"))
        if n < 1:
            print(f'Нельзя сгенерировать выборку из {n} элементов')
            continue
        theta = float(input("Введите значение неотрицательного параметра для равномерного распределения:\t"))
        if theta <= 0:
            print(f'Равномерное распределение не может иметь параметр {theta}')
            continue
        for i in range(n - 1):
            print(round(act3(theta), 4), end=', ')
        print(round(act3(theta), 4))
    elif mode == "5":
        act5()
        act6()
    elif mode == "6":
        l = input('Какую выборку хотите считать? Введите "л" - для логарифмического и "р" - для равномерного:\t')
        if l == 'л':
            l = "log_samples.json"
        elif l == 'р':
            l = "uni_samples.json"
        else:
            print("Нет выборки для такого распределения")
            continue
        n = input("Какого размера выборку хотите считать?\t")
        if int(n) not in [5, 10, 100, 200, 400, 600, 800, 1000]:
            print(f'Нет выборки размера {n}')
            continue
        i = input("Какую выборку хотите взять? Введите номер от 1 до 5\t")
        if int(i) > 5 or int(i) < 1:
            print(f'Всего было сгенерировано по 5 выборок каждого размера, нет выборки с номером {i}')
            continue
        sample = act7(l, n, i)
        max_val = round(max(sample)) + 1
        x = np.linspace(0, max_val, max_val * 10)
        y1 = [emperic_function(sample, i) for i in x]
        if l == "log_samples.json":
            y2 = [log_function(i, 31/37) for i in x]
        else:
            y2 = [uni_function(i, 34) for i in x]
        plt.plot(x, y1, color='r', label='Эмперическая функция распределения')
        plt.plot(x, y2, color='g', label='Функция распределения')
        plt.xlabel('t')
        plt.title('График функций распределения')
        plt.legend()
        plt.show()
    elif mode == "7":
        l = input('Какую выборку хотите считать? Введите "л" - для логарифмического и "р" - для равномерного:\t')
        if l == 'л':
            l = "log_samples.json"
        elif l == 'р':
            l = "uni_samples.json"
        else:
            print("Нет выборки для такого распределения")
            continue
        n1 = input("Какого размера первую выборку хотите считать?\t")
        if int(n1) not in [5, 10, 100, 200, 400, 600, 800, 1000]:
            print(f'Нет выборки размера {n1}')
            continue
        n2 = input("Какого размера вторую выборку хотите считать?\t")
        if int(n2) not in [5, 10, 100, 200, 400, 600, 800, 1000]:
            print(f'Нет выборки размера {n2}')
            continue
        i1 = input("Какую первую выборку хотите взять? Введите номер от 1 до 5\t")
        if int(i1) > 5 or int(i1) < 1:
            print(f'Всего было сгенерировано по 5 выборок каждого размера, нет выборки с номером {i1}')
            continue
        i2 = input("Какую вторую выборку хотите взять? Введите номер от 1 до 5\t")
        if int(i2) > 5 or int(i2) < 1:
            print(f'Всего было сгенерировано по 5 выборок каждого размера, нет выборки с номером {i2}')
            continue
        sample1 = act7(l, n1, i1)
        sample2 = act7(l, n2, i2)
        max_dif = 0
        all_points = sorted(set(sample1 + sample2))
        for point in all_points:
            if abs(emperic_function(sample1, point) - emperic_function(sample2, point)) > max_dif:
                max_dif = abs(emperic_function(sample1, point) - emperic_function(sample2, point))
        diff = math.sqrt(int(n1) * int(n2) / (int(n1) + int(n2))) * max_dif
        print(f'Двувыборочная статистика = {diff}')
    elif mode == "8":
        l = input('Какую выборку хотите считать? Введите "л" - для логарифмического и "р" - для равномерного:\t')
        if l == 'л':
            l = "log_samples.json"
        elif l == 'р':
            l = "uni_samples.json"
        else:
            print("Нет выборки для такого распределения")
            continue
        n = input("Какого размера выборку хотите считать?\t")
        if int(n) not in [5, 10, 100, 200, 400, 600, 800, 1000]:
            print(f'Нет выборки размера {n}')
            continue
        i = input("Какую выборку хотите взять? Введите номер от 1 до 5\t")
        if int(i) > 5 or int(i) < 1:
            print(f'Всего было сгенерировано по 5 выборок каждого размера, нет выборки с номером {i}')
            continue
        sample = act7(l, n, i)
        sample_mean = 0
        for t in sample:
            sample_mean += t
        sample_mean /= int(n)
        sample_var = 0
        for t in sample:
            sample_var += (t - sample_mean) ** 2
        sample_var /= int(n)
        print(f'Среднее выборочное = {sample_mean}, выборочная дисперсия = {sample_var}')
    else:
        print('Такого режима работы нет')
    mode = input("Введите режим работы:\t")
