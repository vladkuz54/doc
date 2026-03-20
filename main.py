import json
from pathlib import Path

from lab4.processor import DataProcessor
from lab4.reader import fetch_csv_to_file
from lab4.strategies import ConsoleOutput, FirebaseOutput, KafkaOutput, RedisOutput


def main():
    with open("config.json", "r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    dataset_url = "https://www.dallasopendata.com/resource/7h2m-3um5.csv?$limit=50"
    local_file = Path("data/data.csv")

    print("Downloading dataset...")
    if fetch_csv_to_file(dataset_url, local_file):
        output_type = config.get("output_type", "console")

        strategy = get_strategy(output_type, config)
        processor = DataProcessor(strategy)
        processor.process_file(local_file)
    else:
        print("Failed to download dataset.")


def get_strategy(output_type, config):

    strategy_factory = {
        "console": lambda: ConsoleOutput(),
        "kafka": lambda: KafkaOutput(config.get("kafka_settings")),
        "redis": lambda: RedisOutput(config.get("redis_settings")),
        "firebase": lambda: FirebaseOutput(config.get("firebase_settings")),
    }
    try:
        return strategy_factory.get(output_type, strategy_factory["console"])()
    except Exception as e:
        print(f"Error initializing strategy '{output_type}': {e}")
        print("Falling back to console output.")
        return ConsoleOutput()


if __name__ == "__main__":
    main()