from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

event = {"order_id": "ORD1234", "status": "NEW"}
producer.send("erp-events", value=event)
producer.flush()

print("📤 Sent ERP event:", event)
