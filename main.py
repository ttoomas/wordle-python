from wordle_answer import Get_wordle_answer
from game import Game
from mode import Mode
from csv_handler import Csv_handler

GAME_ROUNDS = 2
WORDLE_JSON_NAME = "wordle_en.json"

def main():
    while True:
        game_mode = Mode()

        if game_mode == True:
            break

        played_words = Csv_handler.get_played_words()

        wordle_word = Get_wordle_answer(WORDLE_JSON_NAME, game_mode, played_words)

        if not wordle_word:
            game_ended = Mode.no_word(game_mode["lang"])

            if game_ended: break

            wordle_word = Get_wordle_answer(WORDLE_JSON_NAME, game_mode, [])

        Game(wordle_word, GAME_ROUNDS, game_mode["lang"])


main()