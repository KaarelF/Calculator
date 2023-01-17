import math


def addition(x: float, y: float) -> float:
    res = x + y
    return res


def subtraction(x: float, y: float) -> float:
    res = x - y
    return res


def multiplication(x: float, y: float) -> float:
    res = x * y
    return res


def division(x: float, y: float) -> float:

    res = x / y
    return res


def floor(x: float, y: float) -> float:
    res = x // y
    return res


def power(x: float, y: float) -> float:
    res = x ** y
    return res


def modulus(x: float, y: float) -> float:
    res = x % y
    return res


def square_root(x: float) -> float:
    res = math.sqrt(x)
    return res


def calculate(a: float, c: str, b=None) -> float:
    if c == '+':
        res = a + b
    elif c == '-':
        res = a - b
    elif c == '*':
        res = a * b
    elif c == '**':
        res = a ** b
    elif c == '√':
        res = math.sqrt(a)
    else:
        res = a / b
    return res
