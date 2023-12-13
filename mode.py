from googletrans import LANGUAGES
from translation import translation
from tabulate import tabulate
from csv_handler import Csv_handler
from readchar import readchar

class Mode():
    prev_lang = False

    def __new__(self, given_lang = False):
        lang = given_lang

        if not lang:
            lang = self.select_lang()

        mode = self.select_game_mode(lang)

        if mode == True:
            return True

        return {
            "lang": lang,
            "mode": mode
        }

    def select_lang():
        if Mode.prev_lang:
            return Mode.prev_lang

        print(chr(27) + "[2J")

        selected_lang = ""

        while selected_lang not in LANGUAGES and selected_lang not in LANGUAGES.values():
            selected_lang = input("Select any language you want: ").strip().lower()

        Mode.prev_lang = selected_lang
        
        return Mode.prev_lang
    
    def select_game_mode(lang):
        selected_mode = False
        possible_game_modes = ("1", "2", "3", "4")

        intro_text = (
            "Now you can select game mode you want to play.\n\n"
            "Enter 1 for classic mode. In this mode, you will have to guess 5 letter word in english.\n"
            "Enter 2 for translated mode. In this mode, you will have to guess word, that has been translated from english, so number of letters is unknown.\n"
            "Enter 3 to view your all-time game stats\n"
            "Enter 4 to end the game"
        )

        print(chr(27) + "[2J")
        print(translation.translate(intro_text, lang), end="\n\n")

        while selected_mode not in possible_game_modes:
            selected_mode = input(f"{translation.translate('Now select game mode you want to place (1, 2, 3 or 4)', lang)}: ").strip()

        if selected_mode == "3":
            print(chr(27) + "[2J")
            Mode.print_results(lang)

            print(f"\n{translation.translate('Press any key to continue', lang)}: ")
            readchar()
            
            return Mode(lang)
        elif selected_mode == "4":
            return True

        return int(selected_mode)
    
    def print_results(lang):
        played_words = Csv_handler.read_csv_data()

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

    def no_word(lang):
        selected = False
        possible_modes = ("1", "2")

        text = (
            "You guessed all the words, congratulation.\n"
            "Type 1 if you want to delete your statistics and play again\n"
            "Type 2 if you want to end the game\n"
        )

        print(chr(27) + "[2J")
        print(translation.translate(text, lang), end="\n\n")

        while selected not in possible_modes:
            selected = input(f"{translation.translate('Now select, what do you want to play (1 or 2)', lang)}: ").strip()
        
        if selected == "2":
            return True
        
        Csv_handler.clear_file()

        Mode(lang)

        return False