import json
import random
import math
from translation import translation

class Get_wordle_answer:
    def __new__(self, json_name, game_mode, played_words):
        wordle_data = self._load_json(json_name)
        wordle_word = self._generate_wordle(wordle_data, played_words)

        translated_wordle_word = wordle_word

        if not translated_wordle_word: return False

        if game_mode["mode"] is 2 and game_mode["lang"] != "en" and game_mode["lang"] != "english":
            translated_wordle_word = self._translate_word(wordle_word, game_mode["lang"])

        return {
            "original_word": wordle_word,
            "translated_word": translated_wordle_word
        }

    def _load_json(json_name):
        json_data = open(json_name)
        data = json.load(json_data)
        json_data.close()

        return data
    
    def _generate_wordle(wordle_data, played_words):
        non_played_words = [i for i in wordle_data if i not in played_words]
        if len(non_played_words) == 0: return False

        random_index = math.floor(random.random() * len(non_played_words))

        return non_played_words[random_index]
    
    def _translate_word(word, lang):
        translated_word = translation.translate(word, lang).lower()

        return translated_word