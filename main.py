"""
Main Game Module
"""

from wordle_answer import GetWordleAnswer
from game import Game
from mode import Mode
from csv_handler import CsvHandler

GAME_ROUNDS = 2
WORDLE_JSON_NAME = "wordle.json"

def main():
    """
    Main method for starting the game
    """

    while True:
        game_mode = Mode()

        if game_mode is True:
            break

        game_mode = dict(game_mode)

        played_words = CsvHandler.get_played_words()

        wordle_word = GetWordleAnswer(WORDLE_JSON_NAME, game_mode, played_words)

        if not wordle_word:
            game_ended = Mode.no_word(game_mode["lang"])

            if game_ended:
                break

            wordle_word = GetWordleAnswer(WORDLE_JSON_NAME, game_mode, [])

        Game(wordle_word, GAME_ROUNDS, game_mode["lang"])

main()

