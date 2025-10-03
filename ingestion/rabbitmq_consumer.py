import pika, json
from validation.finance_validation import validate_finance_data

def callback(ch, method, properties, body):
    record = json.loads(body)
    print(f"📥 Received batch record: {record}")
    result = validate_finance_data(record)
    print(f"✅ Validation result: {result}")

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='erp-batch')
    channel.basic_consume(queue='erp-batch', on_message_callback=callback, auto_ack=True)
    print("🚀 RabbitMQ Worker listening...")
    channel.start_consuming()

if __name__ == "__main__":
    consume()
