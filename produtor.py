#!/usr/bin/env python
import pika, json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

def publish(method, body, rt):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key=rt, body=json.dumps(body), properties=properties)

def publish2(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='busca', body=json.dumps(body), properties=properties)

def publish_emprestimo(method,body,rt):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='emprestimo_'+rt, body=json.dumps(body), properties=properties)