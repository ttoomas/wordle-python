from readchar import readchar
from termcolor import cprint
from googletrans import LANGUAGES
from translation import translation

class Game:
    def __init__(self, word, rounds):
        self.rounds = rounds

        self.user_chars = []
        self.word_char_count = {}

        self.lang = self.select_lang()

        self.game_loop(word)

    def select_lang(self):
        while True:
            selected_lang = input("Select any language you want: ")

            if selected_lang in LANGUAGES or selected_lang in LANGUAGES.values():
                return selected_lang
            

    def game_loop(self, word):
        for i in range(self.rounds):
            self.word = list(word)

            self.user_chars = self.get_user_chars()
            self.word_char_count = self.count_word()
            self.print_letters()

            self.reset_variables()

            if self.rounds == i + 1: break

            print(" ", end="\n")
            print(f"{translation.translate('Press any key to continue', self.lang)}: ")
            readchar()
    
    def get_user_chars(self):
        for i in range(5):
            print(chr(27) + "[2J")
            print('  '.join(self.user_chars), end=" ")
            print(" _ " * (5 - i))

            self.user_chars.append(self.get_user_input())

        print(chr(27) + "[2J")

        return self.user_chars

    def get_user_input(self):
        user_char = ""

        while True:
            user_char = readchar()

            if user_char.isalpha():
                break

            print(f"\n{translation.translate('Invalid input', self.lang)}: ")
        
        return user_char
    
    def count_word(self):
        print(self.word_char_count)

        for char in self.word:
            self.word_char_count[char] = self.word_char_count.get(char, 0) + 1

        for index, char in enumerate(self.user_chars):
            if self.word[index] is char:
                self.word_char_count[char] -= 1
            if char in self.word_char_count and self.word_char_count[char] is 0:
                del self.word_char_count[char]

        print(self.word_char_count)

        return self.word_char_count

    def print_letters(self):
        for index, char in enumerate(self.user_chars):
            bg_color = "black"

            if self.word[index] is char:
                bg_color = "green"
            elif char in self.word and char in self.word_char_count and self.word_char_count[char] is not 0:
                self.word_char_count[char] -= 1
                bg_color = "yellow"
            else:
                bg_color = "black"
                
            cprint(f" {char} ",'white', f"on_{bg_color}", end=" ", attrs=['bold'])

        print()
    
    def reset_variables(self):
        self.user_chars = []
        self.word_char_count = {}