#!/usr/bin/env python
import random
import threading
import pika, json
from consts import GENEROS_DE_LIVROS

def callback(ch, method, properties, body):
    DecodificaParaString= body.decode('utf-8')
    Desserializa = json.loads(DecodificaParaString)
    data = json.loads(Desserializa)

    if properties.content_type == 'criar_livro':
        print("Livro cadastrado:", data)


def escuta_emprestimo(genero_aleatorio):
    def callback_emprestimo(ch, method, properties, body):
        DecodificaParaString= body.decode('utf-8')
        Desserializa = json.loads(DecodificaParaString)
        data = json.loads(Desserializa)
        print("Livro emprestado:", data)  

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))  
    channel = connection.channel()
    queue = "emprestimo_{}".format(str(genero_aleatorio))
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=callback_emprestimo, auto_ack=True)
    print('Começa a escutar EMPRESTIMOS de livros do tipo:', GENEROS_DE_LIVROS[genero_aleatorio])
    channel.start_consuming()
    channel.close()


def run():
    genero_aleatorio = random.randint(0, 4)
    receberEmprestimo = input("\nDeseja receber notificação sobre o empréstimo do gênero '{}'? (s/n) ".format(GENEROS_DE_LIVROS[genero_aleatorio]))    
    if receberEmprestimo=='s':
        thread = threading.Thread(target=escuta_emprestimo, args=(genero_aleatorio,))
        thread.start()

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))   
    channel = connection.channel()
    channel.queue_declare(queue=str(genero_aleatorio))
    channel.basic_consume(queue=str(genero_aleatorio), on_message_callback=callback, auto_ack=True)
    print('Começa a escutar CADASTROS de livros do tipo:', GENEROS_DE_LIVROS[genero_aleatorio])

    channel.start_consuming()
    channel.close()

run()