from googletrans import Translator

class Translate():
    def __init__(self):
        self.cache = {}
        self.translator = Translator()
    
    def translate(self, string_to_translate, to_lang):
        if to_lang == "en" or to_lang == "english": return string_to_translate

        if not string_to_translate in self.cache:
            self.cache[string_to_translate] = {}

        if not to_lang in self.cache[string_to_translate]:
            self.cache[string_to_translate][to_lang] = self.translator.translate(string_to_translate, src="en", dest=to_lang).text.capitalize()
        
        return self.cache[string_to_translate][to_lang]

translation = Translate()