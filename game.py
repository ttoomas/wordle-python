from readchar import readchar
from termcolor import cprint
from translation import translation
from csv_handler import Csv_handler

class Game:
    def __init__(self, word, rounds, lang):
        self.rounds = rounds
        self.lang = lang

        self.word = list(word)
        self.word_length = len(self.word)

        self.user_chars = []
        self.word_char_count = {}

        self.game_loop()
        
        # TODO - translate
        if not self.won:
            print("You did not guessed the word")
            print("Do you want to play again?")
            return
        
        print("You guessed it!")
        Csv_handler.write("".join(self.word))
        

    def game_loop(self):
        for i in range(self.rounds):
            self.user_chars = self.get_user_chars()
            self.word_char_count = self.count_word()
            self.won = True if len(self.word_char_count) == 0 else False

            self.print_letters()
            self.reset_variables()

            if self.rounds == i + 1 or self.won: break

            print(" ", end="\n")
            print(f"{translation.translate('Press any key to continue', self.lang)}: ")
            readchar()
    
    def get_user_chars(self):
        index = 0

        while len(self.user_chars) < self.word_length:
            print(chr(27) + "[2J")
            print('  '.join(self.user_chars), end=" ")
            print(" _ " * (self.word_length - index))

            user_input = self.get_user_input()

            if user_input is not False:
                self.user_chars.append(user_input)
                index += 1

                continue

            elif index > 0:
                self.user_chars.pop()
                index -= 1


        print(chr(27) + "[2J")

        return self.user_chars

    def get_user_input(self):
        user_char = ""

        while True:
            user_char = readchar()

            if ord(user_char) == 8:
                return False

            if user_char.isalpha():
                break

            print(f"\n{translation.translate('Invalid input', self.lang)}: ")
        
        return user_char
    
    def count_word(self):
        for char in self.word:
            self.word_char_count[char] = self.word_char_count.get(char, 0) + 1

        for index, char in enumerate(self.user_chars):
            if self.word[index] is char:
                self.word_char_count[char] -= 1
            if char in self.word_char_count and self.word_char_count[char] is 0:
                del self.word_char_count[char]

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