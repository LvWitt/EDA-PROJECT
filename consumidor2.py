#!/usr/bin/env python
import pika, json

from db import Database

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='busca')
db = Database()

def callback(ch, method, properties, body):
    print('Received in Busca\n')
    DecodificaParaString= body.decode('utf-8')
    Desserializa = json.loads(DecodificaParaString)
    OpcaoBuscar = json.loads(Desserializa)

    if properties.content_type == 'buscar_livro':
        if OpcaoBuscar.isdigit():
            buscar_codigo = int(OpcaoBuscar)
            livros = db.fetch_books_by_id(buscar_codigo)
            for livro in livros:
                print(f"{livro}\n")
        elif OpcaoBuscar == "todos":
            livros = db.fetch_all_books()
            for livro in livros:
                print(f"{livro}\n")
        else:
            livros = db.fetch_books_from_str(OpcaoBuscar)
            for livro in livros:
                print(f"{livro}\n")

channel.basic_consume(queue='busca', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()



