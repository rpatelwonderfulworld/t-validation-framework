import pika, json

def publish_batch_job(batch):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='erp-batch')
    channel.basic_publish(exchange='', routing_key='erp-batch', body=json.dumps(batch))
    print(f"📤 Sent batch job: {batch}")
    connection.close()

if __name__ == "__main__":
    publish_batch_job({"batch_id": "BATCH_001", "records": 200})
