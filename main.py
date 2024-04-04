from biblioteca import base
from db import Database


def main(): 
    db = Database()
    db.create_tables()
    sair = 0
    while sair == 0:
        comando = input("\nMenu:\n1- Cadastro\n2- Consulta\n3- Empréstimo\n4- Sair\nDigite uma opção: ")

        if comando == "1":
            repetir = "s"
            while repetir != "menu":
                base.cadastrar(db)
                repetir = input("\nDeseja realizar novo cadastro? Aperte enter ou digite 'menu' para voltar\n:")
        elif comando == "2":
            repetir = "s"
            while repetir != "menu":
                base.consultar()
                repetir = input("\nDeseja realizar nova consulta? Aperte enter ou digite 'menu' para voltar\n:")
        elif comando == "3":
            repetir = "s"
            while repetir != "menu":
                base.emprestar()
                repetir = input("\nDeseja realizar novo empréstimo? Aperte enter ou digite 'menu' para voltar\n: ")
        elif comando == "4":
            sair = 1
        else:
            print("\nOpção inválida!\n")

    print("\nPrograma finalizado!")
    exit(0)

if __name__ == "__main__":
    main()



