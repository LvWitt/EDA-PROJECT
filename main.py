import os
from biblioteca import base
from db import Database


def main(): 
    db = Database()
    db.create_tables()
    sair = 0
    while sair == 0:
        os.system('cls')
        comando = input("\n-----GERÊNCIAMENTO-BIBLIOTECA-----\n\nMenu:\n1- Cadastro\n2- Consulta\n3- Empréstimo\n4- Sair\nDigite uma opção: ")
        os.system('cls')
        repetir = "s"

        if comando == "1":
            print("---CADASTRO-DE-LIVOS---\n")
            while repetir != "menu":
                base.cadastrar(db)
                repetir = input("\nSucesso!\nAperte ENTER para fazer novo cadastro ou digite 'menu' para voltar:\n")
        elif comando == "2":
            print("---CONSULTA-DE-LIVOS---\n")
            while repetir != "menu":
                base.consultar()
                repetir = input("\nAperte ENTER para fazer nova consulta ou digite 'menu' para voltar:\n")
        elif comando == "3":
            print("---EMPRÉSTIMO-DE-LIVOS---\n")
            while repetir != "menu":
                base.emprestar()
                repetir = input("\nSucesso!\nAperte ENTER para fazer novo empréstimo ou digite 'menu' para voltar:\n ")
        elif comando == "4":
            sair = 1
        else:
            print("\nOpção inválida!\n")

    print("\nPrograma finalizado!")
    exit(0)

if __name__ == "__main__":
    main()



