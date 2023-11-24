from get_wordle_answer import Get_wordle_answer
from termcolor import cprint


def main():
    wordle_word = Get_wordle_answer("wordle_cs.json")

    cprint(wordle_word, 'white', 'on_red', attrs=['bold'])

main()