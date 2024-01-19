import random
from math import pi


# from random import randint


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    perimeter = 2 * (a + b)

    assert perimeter == 60

    area = a * b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23

    area = pi * r ** 2
    print(area)
    assert area == 1661.9025137490005

    length = 2 * pi * r
    print(length)

    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """

    sorted_random_list = sorted(random.sample(range(1, 101), 10))
    print(sorted_random_list)
    assert len(sorted_random_list) == 10
    assert all(sorted_random_list[i] <= sorted_random_list[i + 1] for i in range(len(sorted_random_list) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    result_dict = dict(zip(first, second))

    assert isinstance(result_dict, dict)
    assert len(result_dict) == 5
    assert list(result_dict.keys()) == first
    assert list(result_dict.values()) == second
