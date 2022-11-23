import pika
import json

class Queue:
  def __init__(self, host, port, exchange, queue):
    self.host = host
    self.port = port
    self.exchange = exchange
    self.queue = queue

    self.queue_name = None
    self.channel = None
    self.connection = None

  def connect(self):
    self.connection = pika.BlockingConnection(
      pika.ConnectionParameters(
        host=self.host,
        port=self.port,
      )
    )
    channel = self.connection.channel()
    self.channel = channel

  def queue_bind(self):
    self.channel.exchange_declare(self.exchange, exchange_type='direct')
    result = self.channel.queue_declare(queue=self.queue)
    self.queue_name = result.method.queue
    self.channel.queue_bind(exchange=self.exchange, queue=self.queue_name)

  def publish(self, data):
    self.channel.basic_publish(
      exchange=self.exchange,
      routing_key=self.queue,
      body=json.dumps(data),
    )

  def close(self):
    self.connection.close()
    
  
