import random
from colorama import Fore, Style # Модуль для изменения цвета текста в консоли

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang  # Язык алфавита
        self.letters = letters  # Список букв алфавита

    def __str__(self):
        return f"Alphabet in {self.lang} language: " + ", ".join(self.letters)

    def print(self):
        print(f"\nAlphabet in {self.lang} language:")
        print("  " + ", ".join(self.letters))

    def letters_num(self):
        return len(self.letters)

    def add_letter(self, letter):
        if self.is_en_letter(letter):
            if letter.upper() not in self.letters:
                self.letters.append(letter.upper())
                print(f"Letter '{letter}' added to the alphabet.")
            else:
                print(f"Letter '{letter}' is already in the alphabet.")
        else:
            print(f"{Fore.RED}Letter '{letter}' is not a valid English letter.{Style.RESET_ALL}")
    # Удаляем букву из алфавита
    def remove_letter(self, letter):
        if letter.upper() in self.letters:
            self.letters.remove(letter.upper())
            print(f"Letter '{letter}' removed from the alphabet.")
        else:
            print(f"{Fore.RED}Letter '{letter}' is not found in the alphabet.{Style.RESET_ALL}")

    def shuffle(self):
        random.shuffle(self.letters)
        print("\nAlphabet shuffled:")
        print("  " + ", ".join(self.letters))

    def is_valid_word(self, word):
        result = all(letter.upper() in self.letters for letter in word)
        color = Fore.YELLOW if result else Fore.RED
        print(f"Is '{word}' a valid word in the English alphabet? {color}{result}{Style.RESET_ALL}")
        return result

    def is_en_letter(self, letter):
        return letter.upper() in self.letters


class EngAlphabet(Alphabet):
    _letters_num = 26
    # Инициализация объекта английского алфавита
    def __init__(self):
        # Вызываем конструктор родительского класса и передаем язык и буквы
        super().__init__("English", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def letters_num(self):
        return EngAlphabet._letters_num

    @staticmethod
    def example():
        return (
            "The English alphabet consists of 26 letters. "
        )


if __name__ == "__main__":
    eng_alphabet = EngAlphabet()

    eng_alphabet.print()
    print(f"\nNumber of letters: {Fore.YELLOW}{eng_alphabet.letters_num()}{Style.RESET_ALL}")

    letter = 'F'
    result = eng_alphabet.is_en_letter(letter)
    color = Fore.YELLOW if result else Fore.RED
    print(f"\nIs '{letter}' an English letter? {color}{result}{Style.RESET_ALL}")

    letter = 'Щ'
    result = eng_alphabet.is_en_letter(letter)
    color = Fore.YELLOW if result else Fore.RED
    print(f"Is '{letter}' an English letter? {color}{result}{Style.RESET_ALL}")

    print("\nExample text:", Fore.YELLOW + EngAlphabet.example() + Style.RESET_ALL)

    eng_alphabet.add_letter('Я')
    eng_alphabet.add_letter('A')
    eng_alphabet.remove_letter('X')
    eng_alphabet.print()

    eng_alphabet.is_valid_word("HELLO")
    eng_alphabet.is_valid_word("HELLOЩ")