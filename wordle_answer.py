import json
import random
import math
from translation import translation

class Get_wordle_answer:
    def __new__(self, json_name, game_mode):
        wordle_data = self._load_json(json_name)
        wordle_word = self._generate_wordle(wordle_data)

        translated_wordle_word = wordle_word

        if game_mode["mode"] is 2 and game_mode["lang"] != "en" and game_mode["lang"] != "english":
            translated_wordle_word = self._translate_word(wordle_word, game_mode["lang"])

        return translated_wordle_word

    def _load_json(json_name):
        json_data = open(json_name)
        data = json.load(json_data)

        return data
    
    def _generate_wordle(wordle_data):
        random_index = math.floor(random.random() * len(wordle_data))

        return wordle_data[random_index]
    
    def _translate_word(word, lang):
        translated_word = translation.translate(word, lang).lower()

        return translated_word