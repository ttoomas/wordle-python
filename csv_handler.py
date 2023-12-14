"""
CSV Handler Module
"""

import csv
import os

FILE_PATH_NAME = ".data/data.csv"
fieldnames = ['word', 'time', 'date']

class CsvHandler:
    """
    Csv handler class
    """

    csv_rows = []

    @staticmethod
    def write(word, time, date):
        """
        Method for writing word, time and date
        inside of csv file
        """

        exist_folder = True

        if not os.path.isdir('.data'):
            os.mkdir('.data')
        if not os.path.isfile(FILE_PATH_NAME):
            exist_folder = False

        with open(FILE_PATH_NAME, "a+", newline="", encoding="UTF8") as file:
            writer = csv.writer(file)

            if not exist_folder or os.path.getsize(FILE_PATH_NAME) == 0:
                writer.writerow(fieldnames)

            writer.writerow([word, time, date])

        CsvHandler.read_csv_data(re_read=True)

        return True

    @staticmethod
    def read_csv_data(re_read = False):
        """
        Method for reading csv data from file
        """

        if len(CsvHandler.csv_rows) > 0 and not re_read:
            return CsvHandler.csv_rows

        CsvHandler.csv_rows = []

        try:
            with open(FILE_PATH_NAME, "r", encoding="UTF8") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    CsvHandler.csv_rows.append(row)
        except Exception:
            CsvHandler.csv_rows = []

        return CsvHandler.csv_rows

    @staticmethod
    def get_played_words():
        """
        Method for getting played words
        """

        words = [i[0] for i in CsvHandler.read_csv_data()]

        return words

    @staticmethod
    def clear_file():
        """
        Method for clearing csv file
        """

        if not os.path.isfile(FILE_PATH_NAME):
            return False

        with open(FILE_PATH_NAME, "w", encoding="UTF-8") as file:
            file.truncate()

            CsvHandler.read_csv_data(re_read=True)

            return True
