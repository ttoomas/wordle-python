"""
Test Module
"""

import pytest
from csv_handler import CsvHandler
from wordle_answer import GetWordleAnswer
from translation import translation


# CSV Handler
def test_write_csv():
    """
    Method for testing writing to csv file
    """

    result = CsvHandler.write("pepa", 10, "10.5.2020")

    assert True is result

def test_read_csv():
    """
    Method for testing reading from csv file
    """

    result = CsvHandler.read_csv_data()

    assert list == type(result)

def test_clear_file():
    """
    Method for testing clearing the csv file
    """

    result = CsvHandler.clear_file()

    assert True is result

def test_get_played_words():
    """
    Method for testing getting played words
    """

    result = CsvHandler.get_played_words()

    assert list == type(result)


# Wordle Answer
def test_get_wordle():
    """
    Method for testing wordle word
    """

    json_name = "wordle.json"
    game_mode = {
        "lang": "cs",
        "mode": 2
    }
    played_words = []

    result = GetWordleAnswer(json_name, game_mode, played_words)

    assert isinstance(result, dict)
    assert "original_word" in dict(result)
    assert "translated_word" in dict(result)

test_get_wordle()

# Translation
@pytest.mark.parametrize('word, lang, translated', [
    ("dog", "cs", "Pes"),
    ("hello", "czech", "Ahoj"),
    ("welcome", "en", "welcome"),
    ("school", "es", "Escuela")
])
def test_translation(word, lang, translated):
    """
    Method for testing translating
    """

    result = translation.translate(word, lang)

    assert translated == result

