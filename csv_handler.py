import csv
import os

FILE_PATH_NAME = ".data/data.csv"
fieldnames = ['word', 'time', 'date']

class Csv_handler():
    csv_rows = []
    
    def write(word, time, date):
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
        
        Csv_handler.read_csv_data(re_read=True)

        return True

    def read_csv_data(re_read = False):
        if len(Csv_handler.csv_rows) > 0 and not re_read:
            return Csv_handler.csv_rows

        Csv_handler.csv_rows = []
        
        try:
            with open(FILE_PATH_NAME, "r", encoding="UTF8") as file:
                reader = csv.reader(file)
                next(reader)
                
                for row in reader:
                    Csv_handler.csv_rows.append(row)
        except:
            Csv_handler.csv_rows = []

        return Csv_handler.csv_rows
            
    def get_played_words():
        words = [i[0] for i in Csv_handler.read_csv_data()]
        
        return words
    
    def clear_file():
        if not os.path.isfile(FILE_PATH_NAME):
            return
        
        with open(FILE_PATH_NAME, "w") as file:
            file.truncate()

            Csv_handler.read_csv_data(re_read=True)

            return True