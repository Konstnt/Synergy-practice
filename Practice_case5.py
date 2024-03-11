#Кейс-задача №5
#Тема: Простая игра "Угадай число"
#1. Напишите программу, которая случайным образом выбирает число от 1 до 100.
#2. Запросите у пользователя предположение о загаданном числе.
#3. Реализуйте механизм проверки, было ли предположение пользователя правильным.
#4. Предоставьте пользователю подсказки (слишком маленькое/большое число) для упрощения угадывания.
#5. Ограничьте количество попыток пользователя, после чего завершите игру.

import random
import os

def show_leaderboard():
    try:
        with open("u_ratings/rating.game", "r") as file:
            print("\n***** РЕЙТИНГ *****")
            print(file.read())
    except FileNotFoundError:
        print("Рейтинг еще не сформирован.")

def update_leaderboard(player_name, attempts):
    if not os.path.exists("u_ratings"):
        os.makedirs("u_ratings")

    leaderboard_path = "u_ratings/rating.game"
    player_data = f"{player_name} | {attempts} попыток\n"
    player_added = False

    if not os.path.isfile(leaderboard_path):
        with open(leaderboard_path, "w") as file:
            file.write(player_data)
    else:
        leaderboard = []
        with open(leaderboard_path, "r") as file:
            for line in file:
                name, score = line.strip().split(" | ")
                score = int(score[:-7])  # Extract the number of attempts
                if name == player_name:
                    player_added = True
                    if attempts < score:
                        leaderboard.append(player_data)
                    else:
                        leaderboard.append(line)
                else:
                    leaderboard.append(line)

        if not player_added:
            leaderboard.append(player_data)

        leaderboard.sort(key=lambda x: int(x.split(" | ")[1][:-7]))
        
        with open(leaderboard_path, "w") as file:
            for entry in leaderboard:
                file.write(entry)

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
            print("Неверный выбор. Попробуйте снова.")

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