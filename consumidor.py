#!/usr/bin/env python
import random
import threading
import pika, json
from tipos_livros import TIPOS_DE_LIVROS

def callback(ch, method, properties, body):
    DecodificaParaString= body.decode('utf-8')
    Desserializa = json.loads(DecodificaParaString)
    data = json.loads(Desserializa)

    if properties.content_type == 'criar_livro':
        print("Livro cadastrado:", data)


def escuta_emprestimo(tipo_aleatorio):
    def callback_emprestimo(ch, method, properties, body):
        DecodificaParaString= body.decode('utf-8')
        Desserializa = json.loads(DecodificaParaString)
        data = json.loads(Desserializa)
        print("Livro emprestado:", data)  

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))  
    channel = connection.channel()
    queue = "emprestimo_{}".format(str(tipo_aleatorio))
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=callback_emprestimo, auto_ack=True)
    print('Começa a escutar EMPRESTIMOS de livros do tipo:', TIPOS_DE_LIVROS[tipo_aleatorio])
    channel.start_consuming()
    channel.close()


def run():
    tipo_aleatorio = random.randint(0, 4)
    receberEmprestimo = input("\nDeseja receber notificação sobre o empréstimo do tipo '{}'? (s/n) ".format(TIPOS_DE_LIVROS[tipo_aleatorio]))    
    if receberEmprestimo=='s':
        thread = threading.Thread(target=escuta_emprestimo, args=(tipo_aleatorio,))
        thread.start()
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))   
    channel = connection.channel()
    channel.queue_declare(queue=str(tipo_aleatorio))
    channel.basic_consume(queue=str(tipo_aleatorio), on_message_callback=callback, auto_ack=True)
    print('Começa a escutar CADASTROS de livros do tipo:', TIPOS_DE_LIVROS[tipo_aleatorio])

    channel.start_consuming()

    channel.close()

run()

#########

# def callback(ch, method, properties, body):
#     print('Consumidor -> Cadastro')
#     print(" Recebeu: %r" % json.loads(body))

#     # if properties.content_type == 'product_created':
#     #     product = Livro(codigo=body.codigo, nome=body.nome, editora=body.editora, ano=body.ano)
#     #     product.livros[body.codigo] = product
#     #     print('Livro cadastrado!')


# channel.basic_consume(queue='cadastro', on_message_callback=callback, auto_ack=True)

# print('Started Consuming')

# channel.start_consuming()

# channel.close()


