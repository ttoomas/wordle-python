from wordle_answer import Get_wordle_answer
from game import Game


def main():
    GAME_ROUNDS = 2

    wordle_word = Get_wordle_answer("wordle_cs.json")

    Game(wordle_word, GAME_ROUNDS)


main()