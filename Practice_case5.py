#Кейс-задача №5
#Тема: Простая игра "Угадай число"
#1. Напишите программу, которая случайным образом выбирает число от 1 до 100.
#2. Запросите у пользователя предположение о загаданном числе.
#3. Реализуйте механизм проверки, было ли предположение пользователя правильным.
#4. Предоставьте пользователю подсказки (слишком маленькое/большое число) для упрощения угадывания.
#5. Ограничьте количество попыток пользователя, после чего завершите игру.

import random
import os
import pickle

leaderboard_file = "u_ratings/leaderboard.pickle"

def show_leaderboard():
    try:
        # Десериализация данных из файла leaderboard.pickle
        with open(leaderboard_file, "rb") as file:
            leaderboard = pickle.load(file)
            sorted_leaderboard = sorted(leaderboard, key=lambda x: x["score"])
            
            print("\n***** ТАБЛИЦА ЛИДЕРОВ *****")
            
            for idx, entry in enumerate(sorted_leaderboard, start=1):
                print(f"{idx}. Игрок: {entry['username']}, Попыток: {entry['score']}")
            
            print("***************************\n")

    except FileNotFoundError:
        print("Таблица лидеров еще не сформирована.")

def update_leaderboard(username, score):
    try:
        # Десериализация данных из файла leaderboard.pickle
        with open(leaderboard_file, "rb") as file:
            leaderboard = pickle.load(file)
    except FileNotFoundError:
        leaderboard = []

    new_entry = {"username": username, "score": score}
    leaderboard.append(new_entry)

    # Сортировка лидеров по наименьшему количеству попыток
    leaderboard = sorted(leaderboard, key=lambda x: x["score"])

    # Сериализация данных таблицы лидеров обновленной версии в файл leaderboard.pickle
    with open(leaderboard_file, "wb") as file:
        pickle.dump(leaderboard, file)

    print("Таблица лидеров была успешно обновлена!")


def game_menu():
    print("Добро пожаловать в игру 'Угадай число'!")
    while True:
        print("N - начать новую игру")
        print("R - показать рейтинг")
        print("X - выход")
        choice = input("Выберите действие: ").upper()

        if choice == "N":
            player_name = input("Введите ваше имя: ")
            play_game(player_name)
        elif choice == "R":
            show_leaderboard()
        elif choice == "X":
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("---Опция не выбрана---")

def play_game(player_name):
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print(f"Привет, {player_name}! Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
        guess = int(input("Введите ваше предположение: "))
        attempts += 1

        if guess < number_to_guess:
            print("Загаданное число БОЛЬШЕ вашего..")
        elif guess > number_to_guess:
            print("Загаданное число МЕНЬШЕ вашего..")
        else:
            print(f"Поздравляю, {player_name}! Вы угадали число {number_to_guess} за {attempts} попыток.")
            update_leaderboard(player_name, attempts)
            break
game_menu()