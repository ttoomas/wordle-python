"""
Game module
"""

import time
from datetime import datetime
from readchar import readchar
from termcolor import cprint
from translation import translation
from csv_handler import CsvHandler

class Game:
    """
    Game handle class
    """

    def __init__(self, word, rounds, lang):
        """
        Init game method
        """

        self.rounds = rounds
        self.lang = lang

        self.word = list(word["translated_word"])
        self.original_word = word["original_word"]
        self.word_length = len(self.word)

        self.user_chars = []
        self.word_char_count = {}

        start_time = time.time()

        self._game_loop()

        end_time = time.time()

        if not self.won:
            text = (
                "You did not guessed the word. \n"
                "Do you want to play again?"
            )

            print(translation.translate(text, self.lang))
            return

        final_time = round(end_time - start_time)
        current_datetime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        CsvHandler.write(self.original_word, final_time, current_datetime)

        print(f"\n{translation.translate('Congratulation, You guessed it!', self.lang)}")
        print(f"\n{translation.translate('Press any key to continue', self.lang)}: ")
        readchar()

    def _game_loop(self):
        """
        Game loop method
        """

        for i in range(self.rounds):
            self.user_chars = self._get_user_chars()
            self.word_char_count = self._count_word()
            self.won = len(self.word_char_count) == 0

            self._print_letters()
            self._reset_variables()

            if self.rounds == i + 1 or self.won:
                break

            print(" ", end="\n")
            print(f"{translation.translate('Press any key to continue', self.lang)}: ")
            readchar()

    def _get_user_chars(self):
        """
        Method for getting user chars
        """

        index = 0

        while len(self.user_chars) < self.word_length:
            print(chr(27) + "[2J")
            print('  '.join(self.user_chars), end=" ")
            print(" _ " * (self.word_length - index))

            user_input = self._get_user_input()

            if user_input is not False:
                self.user_chars.append(user_input)
                index += 1

                continue

            if index > 0:
                self.user_chars.pop()
                index -= 1

        print(chr(27) + "[2J")

        return self.user_chars

    def _get_user_input(self):
        """
        Method for getting char from user input
        """

        user_char = ""

        while not user_char.isalpha():
            user_char = readchar()

            if ord(user_char) == 8:
                return False

            print(f"\n{translation.translate('Invalid input', self.lang)}: ")

        return user_char

    def _count_word(self):
        """
        Method for removing chars from word char count
        """

        for char in self.word:
            self.word_char_count[char] = self.word_char_count.get(char, 0) + 1

        for index, char in enumerate(self.user_chars):
            if self.word[index] is char:
                self.word_char_count[char] -= 1
            if char in self.word_char_count and self.word_char_count[char] == 0:
                del self.word_char_count[char]

        return self.word_char_count

    def _print_letters(self):
        """
        Method for printing user chars
        """

        for index, char in enumerate(self.user_chars):
            bg_color = "black"

            if self.word[index] is char:
                bg_color = "green"
            elif (
                char in self.word and
                char in self.word_char_count and
                self.word_char_count[char] != 0
            ):
                self.word_char_count[char] -= 1
                bg_color = "yellow"
            else:
                bg_color = "black"

            cprint(f" {char} ",'white', f"on_{bg_color}", end=" ", attrs=['bold'])

        print()

    def _reset_variables(self):
        """
        Method for reseting variables
        """

        self.user_chars = []
        self.word_char_count = {}

