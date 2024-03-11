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

#Configs
number_to_guess = random.randint(1, 100) #диапазон чисел для загадывания
max_attempts = 10                        #макс кол-во попыток игрока 
leaderboard_file = "u_ratings/leaderboard.pkl" #файл сохранения рейтинга игроков

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_leaderboard():
    try:
        # Десериализация данных из файла leaderboard.pickle
        with open(leaderboard_file, "rb") as file:
            leaderboard = pickle.load(file)
            sorted_leaderboard = sorted(leaderboard, key=lambda x: x["score"])
            
            print("\n***** ТАБЛИЦА ЛИДЕРОВ *****")
            
            for indx, entry in enumerate(sorted_leaderboard, start=1):
                print(f"{indx}. Игрок: {entry['username']}, Попыток: {entry['score']}")
            
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

    # Сортировка лидеров по наименьшему количеству попыток
    leaderboard.append(new_entry)
    leaderboard = sorted(leaderboard, key=lambda x: x["score"])

    # Ограничение таблицы лидеров 10 строками
    if len(leaderboard) > 10:
        leaderboard = leaderboard[:10]

    # Сериализация данных обновленной таблицы лидеров в файл leaderboard.pickle
    with open(leaderboard_file, "wb") as file:
        pickle.dump(leaderboard, file)

    print("Ваш результат добавлен в таблицу лидеров!")


def game_menu():

    while True:
        print("Добро пожаловать в игру 'Угадай число'!")
        print("N - Новая игра")
        print("R - показать рейтинг")
        print("X - выход")
        choice = input("Выберите действие: ").upper()

        if choice == "N":
            player_name = input("\nВведите ваше имя: ")
            play_game(player_name)
        elif choice == "R":
            clear_screen()
            show_leaderboard()
        elif choice == "X":
            print("Спасибо за игру! До свидания!")
            break
        else:
            clear_screen()

def play_game(player_name):
    
    clear_screen()
    
    attempts = 0

    print(f"Привет, {player_name}! Я загадал число от 1 до 100. Попробуй угадать его!\nУ тебя {max_attempts} попыток.\n")

    while attempts < max_attempts:
       
        remaining_attempts = max_attempts - attempts
        
        while True:
           try:
            guess = int(input("Введите ваше предположение: "))
            break  # Прерываем цикл, если введено целое число
           except ValueError:
            print("Введите число. Попробуйте снова.")

        attempts += 1

        if guess < number_to_guess:
            clear_screen()
            print(f"\n!Подасказка. Загаданное число БОЛЬШЕ {guess}. (Оставшиеся попытки: {remaining_attempts})")
        elif guess > number_to_guess:
            clear_screen()
            print(f"\n!Подасказка. Загаданное число МЕНЬШЕ {guess}. (Оставшиеся попытки: {remaining_attempts})")
        else:
            clear_screen()
            print(f"\nПоздравляю, {player_name}! Вы угадали число {number_to_guess} за {attempts} попыток.")
            update_leaderboard(player_name, attempts)
            break

    if attempts == max_attempts:
        print(f"\nУ вас закончились попытки. Загаданное число было: {number_to_guess}. Повезет в другой раз :)\n")

try:
  clear_screen()
  game_menu()
except KeyboardInterrupt:
        print("\nВыход из программы.")