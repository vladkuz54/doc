from abc import ABC, abstractmethod


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