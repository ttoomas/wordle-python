from wordle_answer import Get_wordle_answer
from game import Game
from mode import Mode
from csv_handler import Csv_handler

GAME_ROUNDS = 2
WORDLE_JSON_NAME = "wordle_en.json"

def main():
    # # game_mode = Mode()

    game_mode = {"lang": "en", "mode": 1}
    Mode.print_results(game_mode["lang"])
    played_words = Csv_handler.get_played_words()

    # # print(played_words)

    wordle_word = Get_wordle_answer(WORDLE_JSON_NAME, game_mode, played_words)

    if not wordle_word:
        print("TODO")
        
        return

    Game(wordle_word, GAME_ROUNDS, game_mode["lang"])

    # # Csv_handler.write("dog")


main()