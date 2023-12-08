import csv
import os

fieldnames = ['word']

class Csv_handler():
    def write(word):
        exist_folder = True

        if not os.path.isdir('.data'):
            os.mkdir('.data')
        if not os.path.isfile('.data/data.csv'):
            exist_folder = False

        with open(".data/data.csv", "a+", newline="", encoding="UTF8") as file:
            writer = csv.writer(file)

            if not exist_folder or os.path.getsize('.data/data.csv') == 0:
                writer.writerow(fieldnames)

            writer.writerow([word])
        
    def get_played_words():
        words = []

        try:
            file = open(".data/data.csv", "r", encoding="UTF8")
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                words.append(row[0])
        except:
            words = []
        
        return words