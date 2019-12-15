#!/usr/bin/env python3
# coding=utf-8

def main():  # основная функция
    a = int(input('введите A: '))
    b = int(input('введите B: '))
    x = int(input('введите X: '))
    if x >= 4:
        y =(a ** 2 + 5 * x + b ** 2)/ (a * b)
    else:
        y = x * (a - b)
    print("y = %.1f" % y)


