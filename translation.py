"""
Transition module
"""

from googletrans import Translator

class Translate:
    """
    Class for translation words
    """

    def __init__(self):
        """
        Init method
        """

        self.cache = {}
        self.translator = Translator()

    def translate(self, string_to_translate, to_lang):
        """
        Method for translating
        """

        english_lang = ("en", "english")
        if to_lang in english_lang:
            return string_to_translate

        if not string_to_translate in self.cache:
            self.cache[string_to_translate] = {}

        if not to_lang in self.cache[string_to_translate]:
            translated_text = self.translator.translate(string_to_translate, src="en", dest=to_lang)

            self.cache[string_to_translate][to_lang] = translated_text.text.capitalize()

        return self.cache[string_to_translate][to_lang]

translation = Translate()
