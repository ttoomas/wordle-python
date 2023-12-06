from wordle_answer import Get_wordle_answer
from game import Game
from mode import Mode

def main():
    GAME_ROUNDS = 1
    WORDLE_JSON_NAME = "wordle_en.json"

    game_mode = Mode()

    wordle_word = Get_wordle_answer(WORDLE_JSON_NAME, game_mode)

    Game(wordle_word, GAME_ROUNDS, game_mode["lang"])


main()