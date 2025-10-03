from kafka import KafkaConsumer
import json
from validation.erp_validation import validate_erp_data

def consume_erp_orders():
    consumer = KafkaConsumer(
        'erp-orders',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='erp-validation-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("🚀 ERP Validation Service listening on 'erp-orders' topic...")

    for message in consumer:
        erp_record = message.value
        print(f"Received ERP record: {erp_record}")
        result = validate_erp_data(erp_record)
        print(f"Validation result: {result}")

if __name__ == "__main__":
    consume_erp_orders()
