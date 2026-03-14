import csv
import json

from dal.strategies import IOutputStrategy


class DataProcessor:
    def __init__(self, strategy: IOutputStrategy):
        self._strategy = strategy

    def process_file(self, file_path: str):
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data_string = json.dumps(row)
                    self._strategy.send(data_string)

            print(f"Processing of file {file_path} completed.")
        except FileNotFoundError:
            print(f"Error: File {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred during processing: {e}")