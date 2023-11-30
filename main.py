from get_wordle_answer import Get_wordle_answer
from game import Game


def main():
    wordle_word = Get_wordle_answer("wordle_cs.json")

    # cprint(wordle_word, 'white', 'on_red', attrs=['bold'])

    Game(wordle_word)


main()