import random

def guessNumber():
    print("\033[1;36mДобро пожаловать в игру «Угадай число»!\033[0m")
    print("Компьютер загадал число от 1 до 100. У Вас есть 5 попыток, чтобы его угадать.")
    
    # Генерация случайного числа
    numberGuess = random.randint(1, 100)

    #Подсказка для тестирования:
    print(f"\033[1;35m(Подсказка для тестирования: Загаданное число — {numberGuess})\033[0m\n")

    attempts = 5

    for attempt in range(1, attempts + 1):
        try:
            userGuess = int(input(f"\033[1;33mПопытка {attempt} из {attempts}. Введите ваше число: \033[0m"))
        except ValueError:
            print("\033[1;31mПожалуйста, введите корректное число.\033[0m")
            continue

        if userGuess == numberGuess:
            print("\033[1;32mПоздравляем! Вы угадали правильное число! 🎉\033[0m")
            return
        elif userGuess < numberGuess:
            print("\033[1;34mСлишком маленькое число! Попробуй число больше.\033[0m")
        else:
            print("\033[1;34mСлишком большое число! Попробуй число меньше.\033[0m")

    print(f"\033[1;31mВы исчерпал все попытки. Правильное число было: {numberGuess}. Попробуй снова!\033[0m")

# Запуск игры
guessNumber()