import csv
import os

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
                data.append(row)
        return data


if __name__ == "__main__":
    reader = CSVReader("data/courses.csv")
    data = reader.read_csv()
    print(data[0])  