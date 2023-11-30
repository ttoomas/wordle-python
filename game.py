import readchar
from termcolor import cprint

class Game:
    def __init__(self, word):
        self.word = list(word)

        self.get_user_input()
    
    def get_user_input(self):
        user_chars = []
        
        for i in range(5):
            print(chr(27) + "[2J")
            print('  '.join(user_chars), end=" ")
            print(" _ " * (5 - i))
            user_chars.append(readchar.readchar())

        print(chr(27) + "[2J")
        word_char_count = {}
        for char in self.word:
            word_char_count[char] = word_char_count.get(char, 0) + 1

        for index, char in enumerate(user_chars):
            if self.word[index] is char:
                word_char_count[char] -= 1

        for index, char in enumerate(user_chars):
            bg_color = "black"

            if self.word[index] is char:
                bg_color = "green"
            elif char in self.word and word_char_count[char] is not 0:
                word_char_count[char] -= 1
                bg_color = "yellow"
            else:
                bg_color = "grey"
                
            cprint(f" {char} ",'white', f"on_{bg_color}", end=" ", attrs=['bold'])