import math
import random
import json


def summa(t, m):
    s = 0
    for i in range(1, m + 1):
        s += (t ** i) / i
    return s


def function(x, t):
    return -1 / math.log(1 - t) * summa(t, x)


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
            if function(q, theta) >= gamma:
                return q
            else:
                q += 1


def act1():
    theta = float(input("Введите значение параметра в интервале от 0 до 1:\t"))
    if theta >= 1 or theta <= 0:
        print("Параметр не может принимать такое значение")
    else:
        gamma = float(input("Введите уровень квантиля:\t"))
        ans = quantil(gamma, theta)
        if ans == -1:
            print("Нету квантиля такого уровня")
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

        def act5():
            theta = 0.8378
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


mode = int(input("Введите режим работы:\t"))
while mode != -1:
    if mode == 1:
        act1()
    elif mode == 2:
        print(uniform())
    elif mode == 3:
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
    elif mode == 4:
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
    elif mode == 5:
        act5()
        act6()
    else:
        print('Такого режима работы нету')
    mode = int(input("Введите режим работы:\t"))
