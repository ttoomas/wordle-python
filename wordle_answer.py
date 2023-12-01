import json
import random
import math

class Get_wordle_answer:
    def __new__(self, json_name):

        wordle_data = self._load_json(json_name)
        wordle_word = self._generate_wordle(wordle_data)

        return wordle_word

    def _load_json(json_name):
        json_data = open(json_name)
        data = json.load(json_data)

        return data
    
    def _generate_wordle(wordle_data):
        random_index = math.floor(random.random() * len(wordle_data))

        return wordle_data[random_index]