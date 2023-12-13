import pytest
from csv_handler import Csv_handler
from wordle_answer import Get_wordle_answer
from translation import translation


# CSV Handler
def test_write_csv():
    result = Csv_handler.write("pepa", 10, "10.5.2020")

    assert True == result

def test_read_csv():
    result = Csv_handler.read_csv_data()

    assert list == type(result)

def test_get_played_words():
    result = Csv_handler.get_played_words()

    assert list == type(result)

def test_clear_file():
    result = Csv_handler.clear_file()

    assert True == result


# Wordle Answer
def test_get_wordle():
    json_name = "wordle_en.json"
    game_mode = {
        "lang": "cs",
        "mode": 2
    }
    played_words = []

    result = Get_wordle_answer(json_name, game_mode, played_words)

    assert dict == type(result) and "original_word" in result and "translated_word" in result

# Translation
@pytest.mark.parametrize('word, lang, translated', [
    ("dog", "cs", "Pes"),
    ("hello", "czech", "Ahoj"),
    ("Welcome", "en", "Welcome"),
    ("school", "es", "Escuela")
])
def test_translation(word, lang, translated):
    result = translation.translate(word, lang)

    assert translated == result