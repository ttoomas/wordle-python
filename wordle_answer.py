"""
Wordle Answer Module
"""

import json
import random
import math
from translation import translation

class GetWordleAnswer:
    """
    Class for getting wordle word
    """

    def __new__(cls, json_name, game_mode, played_words):
        """
        Method to return wordle word when created
        """

        wordle_data = cls._load_json(json_name)
        wordle_word = cls._generate_wordle(wordle_data, played_words)

        translated_wordle_word = wordle_word

        if not translated_wordle_word:
            return False

        if game_mode["mode"] == 2 and game_mode["lang"] != "en" and game_mode["lang"] != "english":
            translated_wordle_word = cls._translate_word(wordle_word, game_mode["lang"])

        return {
            "original_word": wordle_word,
            "translated_word": translated_wordle_word
        }

    @staticmethod
    def _load_json(json_name):
        """
        Method for loading json
        """

        with open(json_name, encoding="UTF-8") as file:
            data = json.load(file)

            return data

    @staticmethod
    def _generate_wordle(wordle_data, played_words):
        """
        Method for selecting random wordle word
        """

        non_played_words = [i for i in wordle_data if i not in played_words]
        if len(non_played_words) == 0:
            return False

        random_index = math.floor(random.random() * len(non_played_words))

        return non_played_words[random_index]

    @staticmethod
    def _translate_word(word, lang):
        """
        Method to translate wordle word
        """

        translated_word = translation.translate(word, lang).lower()

        return translated_word
