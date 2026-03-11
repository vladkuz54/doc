import csv
from datetime import datetime


class CSVReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_csv(self): 
        data = []
        with open(self.filepath, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for key, value in row.items():
                    if value == "":
                        row[key] = None
                    elif value.lower() in ['true', 'false']:
                        row[key] = 0 if value.lower() == 'false' else 1
                    elif value.isdigit():
                        row[key] = int(value)
                    elif key == "release_date" and value is not None:
                        row[key] = datetime.strptime(row["release_date"], "%Y-%m-%d").date()
                data.append(row)
        return data
