import json
from abc import ABC, abstractmethod
from pathlib import Path


class IOutputStrategy(ABC):
    @abstractmethod
    def send(self, data: str):
        pass


class ConsoleOutput(IOutputStrategy):
    def send(self, data: str):
        print(f"\n[CONSOLE OUTPUT]: {data}")


class KafkaOutput(IOutputStrategy):
    def __init__(self, settings):
        from kafka import KafkaProducer

        self.topic = settings.get("topic", "default_topic")
        self.producer = KafkaProducer(
            bootstrap_servers=settings.get("bootstrap_servers"),
            value_serializer=lambda value: value.encode("utf-8"),
        )

    def send(self, data: str):
        try:
            self.producer.send(self.topic, value=data)
            self.producer.flush()
            print(f"[KAFKA] Message sent to topic: {self.topic}")
        except Exception as e:
            print(f"[KAFKA ERROR]: {e}")


class RedisOutput(IOutputStrategy):
    def __init__(self, settings):
        import redis

        self.client = redis.Redis(
            host=settings.get("host", "localhost"),
            port=settings.get("port", 6379),
            db=settings.get("db", 0),
        )
        self.list_name = settings.get("list_name", "dataset_list")

    def send(self, data: str):
        try:
            self.client.rpush(self.list_name, data)
            print(f"[REDIS] Row added to list: {self.list_name}")
        except Exception as e:
            print(f"[REDIS ERROR]: {e}")


class FirebaseOutput(IOutputStrategy):
    def __init__(self, settings):
        import firebase_admin
        from firebase_admin import credentials, firestore

        if not settings:
            raise ValueError("firebase_settings are required")

        credentials_path = settings.get("credentials_path")
        if not credentials_path:
            raise ValueError("'credentials_path' is required for firebase_settings")

        credentials_file = Path(credentials_path)
        if not credentials_file.exists():
            raise FileNotFoundError(
                f"Firebase credentials file not found: {credentials_file}"
            )

        self.collection_name = settings.get("collection_name", "dataset_rows")

        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate(str(credentials_file))
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def send(self, data: str):
        try:
            payload = json.loads(data)
        except json.JSONDecodeError:
            payload = {"raw": data}

        try:
            self.db.collection(self.collection_name).add(payload)
            print(f"[FIREBASE] Document added to collection: {self.collection_name}")
        except Exception as e:
            print(f"[FIREBASE ERROR]: {e}")