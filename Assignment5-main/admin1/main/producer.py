import pika, json

params = pika.URLParameters('amqps://rxxmhubl:kLdbTY6wzsPE5S8e3KiZPftfQHwF3o2L@beaver.rmq.cloudamqp.com/rxxmhubl')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
