"""
Game Mode module
"""

from googletrans import LANGUAGES
from readchar import readchar
from tabulate import tabulate
from translation import translation
from csv_handler import CsvHandler
from utils import Utils

class Mode:
    """
    Game Mode class
    """

    prev_lang = False

    def __new__(cls, given_lang = False):
        """
        Method for selecting game mode
        and returning selection
        """

        lang = given_lang

        if not lang:
            lang = cls._select_lang()

        mode = cls._select_game_mode(lang)

        if mode is True:
            return True

        return {
            "lang": lang,
            "mode": mode
        }

    @staticmethod
    def _select_lang():
        """
        Method for selection lang by user input
        """

        if Mode.prev_lang:
            return Mode.prev_lang

        Utils.clear_terminal()

        selected_lang = ""

        while selected_lang not in LANGUAGES and selected_lang not in LANGUAGES.values():
            selected_lang = input("Select any language you want: ").strip().lower()

        Mode.prev_lang = selected_lang

        return Mode.prev_lang

    @staticmethod
    def _select_game_mode(lang):
        """
        Method for selecting game mode by user input
        """

        selected_mode = False
        possible_game_modes = ("1", "2", "3", "4")

        intro_text = (
            "Now you can select game mode you want to play.\n\n"
            "Enter 1 for classic mode. In this mode,"
            "you will have to guess 5 letter word in english.\n"
            "Enter 2 for translated mode. In this mode, you will"
            "have to guess word, that has been translated from english,"
            "so the number of letters is unknown.\n"
            "Enter 3 to view your all-time game stats\n"
            "Enter 4 to end the game"
        )

        Utils.clear_terminal()
        print(translation.translate(intro_text, lang), end="\n\n")

        while selected_mode not in possible_game_modes:
            text = "Now select game mode you want to play (1, 2, 3 or 4)"
            selected_mode = input(f"{translation.translate(text, lang)}: ").strip()

        if selected_mode == "3":
            Utils.clear_terminal()
            Mode._print_results(lang)

            Utils.press_continue(lang)

            return Mode(lang)
        if selected_mode == "4":
            return True

        return int(selected_mode)

    @staticmethod
    def _print_results(lang):
        """
        Method for printing game results
        """

        played_words = CsvHandler.read_csv_data()

        if len(played_words) == 0:
            played_words = [["", "", ""]]
        else:
            played_words = [[word[0], word[1] + "s", word[2]] for word in played_words]

        translated_headers = [
            translation.translate("Word", lang),
            translation.translate("Time", lang),
            translation.translate("Date", lang)
        ]

        table = tabulate(
            played_words,
            headers=translated_headers,
            tablefmt='psql',
            showindex=False,
            colalign=("left", "center", "center")
        )

        print(table)

    @staticmethod
    def no_word(lang):
        """
        Method for handling no word in possible wordle words
        """

        selected = False
        possible_modes = ("1", "2")

        text = (
            "You guessed all the words, congratulation.\n"
            "Enter 1 if you want to delete your statistics and play again\n"
            "Enter 2 if you want to end the game\n"
        )

        Utils.clear_terminal()
        print(translation.translate(text, lang), end="\n\n")

        while selected not in possible_modes:
            text = "Now select, what do you want to play (1 or 2)"
            selected = input(f"{translation.translate(text, lang)}: ").strip()

        if selected == "2":
            return True

        CsvHandler.clear_file()

        game_ended = Mode(lang)

        return game_ended is True
