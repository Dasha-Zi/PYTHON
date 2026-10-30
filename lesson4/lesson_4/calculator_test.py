import pytest
from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums(): #поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, -10) #поменяли параметры
    assert res == -16

def test_sum_positive_and_negative_nums(): #поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, 6) #поменяли параметры
    assert res == 0

def test_sum_float_nums(): #проверка сложения десятичных дробей
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)  
    assert res == 9.9

def test_sum_zero_nums(): #проверка сложения целого числа и нуля
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

def test_div_positive(): #проверка деления чисел
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero(): #проверка деления на ноль
    calculator = Calculator()
    with pytest.raises(ArithmeticError): 
        calculator.div(10, 0)

def test_avg_empty_list(): #проверка нахождения среднего для пустого списка
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0
