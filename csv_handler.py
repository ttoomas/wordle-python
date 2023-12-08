import csv
import os

fieldnames = ['word', 'time', 'date']

class Csv_handler():
    csv_rows = []
    
    def write(word, time, date):
        exist_folder = True

        if not os.path.isdir('.data'):
            os.mkdir('.data')
        if not os.path.isfile('.data/data.csv'):
            exist_folder = False

        with open(".data/data.csv", "a+", newline="", encoding="UTF8") as file:
            writer = csv.writer(file)

            if not exist_folder or os.path.getsize('.data/data.csv') == 0:
                writer.writerow(fieldnames)

            writer.writerow([word, time, date])
        
        Csv_handler.read_csv_data(re_read=True)

    def read_csv_data(re_read = False):
        if len(Csv_handler.csv_rows) > 0 and not re_read:
            return Csv_handler.csv_rows

        Csv_handler.csv_rows = []
        
        try:
            with open(".data/data.csv", "r", encoding="UTF8") as file:
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