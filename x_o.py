# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:44:56 2024

@author: diz
"""

import random

# Функция для вывода игрового поля
def print_field(field):
    print(" " + field[0] + " | " + field[1] + " | " + field[2])
    print("---+---+---")
    print(" " + field[3] + " | " + field[4] + " | " + field[5])
    print("---+---+---")
    print(" " + field[6] + " | " + field[7] + " | " + field[8])

# Функция для проверки победы
def check_win(field):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if field[condition[0]] == field[condition[1]] == field[condition[2]] != " ":
            return True
    return False

# Функция для проверки ничьей
def check_draw(field):
    return " " not in field

# Основная функция игры
def game():
    field = [" "] * 9
    current_player = "X"
    while True:
        print_field(field)
        move = input("Игрок " + current_player + ", введите номер ячейки (1-9): ")
        if field[int(move) - 1] != " ":
            print("Ячейка уже занята!")
            continue
        field[int(move) - 1] = current_player
        if check_win(field):
            print_field(field)
            print("Игрок " + current_player + " победил!")
            break
        elif check_draw(field):
            print_field(field)
            print("Ничья!")
            break
        current_player = "O" if current_player == "X" else "X"

# Запуск игры
game()