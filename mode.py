from googletrans import LANGUAGES
from translation import translation

class Mode():
    def __new__(self):
        lang = self.select_lang()

        mode = 1
        
        if lang != "en":
            mode = self.select_game_mode(lang)

        return {
            "lang": lang,
            "mode": mode
        }

    def select_lang():
        while True:
            selected_lang = input("Select any language you want: ").strip().lower()

            if selected_lang in LANGUAGES or selected_lang in LANGUAGES.values():
                return selected_lang
    
    def select_game_mode(lang):
        selected_mode = False

        print(translation.translate("Now you can select game mode you want to play", lang))
        print(translation.translate("Enter 1 for classic mode. In this mode, you will have to guess 5-letter word in english", lang))
        print(translation.translate("Enter 2 for translated mode. In this mode, you will have to guess word, that has been translated from english, so number of letters is unknown", lang))
        print()

        while selected_mode is not "1" and selected_mode is not "2":
            selected_mode = input(f"{translation.translate('Now select game mode you want to place (1 or 2)', lang)}: ").strip()
        
        return int(selected_mode)