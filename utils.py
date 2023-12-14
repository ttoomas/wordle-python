"""
Utils Module
"""

from readchar import readchar
from translation import translation

class Utils:
    """
    Utils class
    """

    @staticmethod
    def clear_terminal():
        """
        Method for clearing the terminal
        """

        print(chr(27) + "[2J")

    @staticmethod
    def press_continue(lang):
        """
        Method to wait untill user press any key
        """

        print(f"\n{translation.translate('Press any key to continue', lang)}: ")
        readchar()
