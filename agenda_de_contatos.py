#Agenda de contatos
import re
contatos = {}

def adicionar_contato():
    while True:
        while True:
            nome = input("\nDigite o nome do contato: ").strip().capitalize()
            if len(nome)< 2:
                print("\nPor favor,digite um numero valido!")
            else:
                break
        add_gmail = input ("\nGostaria de adicionar o gmail do contato s/n?: ").strip().lower()
        if add_gmail == "s":
            gmail = input("Digite o gmail: ")
            break
        elif add_gmail == "n":
            gmail = "Não informado"
            break
    while True:
        numero =input("Digite o numero de telefone: ")
        padrao = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
        if re.fullmatch(padrao, numero):
            novo_contato = {
                    "nome" : nome,
                    "gmail": gmail,
                    "numero": numero

            }
            contatos[nome] = novo_contato
            print("\nNovo contato adicionado!")
            return
        else:
            print("O numero não está correto")
            
def visualizar_contatos():
    print("\n===Contatos===\n")
    if not contatos:
        print("\nSua lista de contatos está vazia!")
        return
    for nome in contatos:
        print("\n",nome)
    nome = input("\nDigite o nome do contato: ").strip().capitalize()
    if nome in contatos :
        print("Nome:", contatos[nome]["nome"])
        print("Gmail:", contatos[nome]["gmail"])
        print("Número:", contatos[nome]["numero"])
        return
    else:
        print("\nEste contato não existe!")
        return
    
    


def excluir_contato():
    if not contatos:
        print("\nSua lista de contatos está vazia!")
        return
    nome = input("Qual o nome do contato que deseja excluir?: ").strip().capitalize()
    if nome in contatos:
        del contatos[nome]
        print("\nContato excluido!")
        return
    else:
        print("\nEste contato não existe!!!")
        return



escolhas = ("1", "Adicionar contatos", "Adicionar contato", "2", "Visualizar contatos","Visualizar contato","3","Excluir contato","Excluir contatos")
if __name__ == "__main__":
    while True:
        print("\n===Agenda de contatos===\n")
        print("O que gostaria de fazer?")
        print("1- adicionar contatos")
        print("2- visualizar contatos")
        escolha = input("3- excluir contato").strip().capitalize()
        if escolha not in escolhas:
            print("\nPor favor, escolha uma opção valida")
        if escolha == "1" or escolha == "Adicionar contatos" or escolha == "Adicionar contato":
            adicionar_contato()
        elif escolha == "2" or escolha == "Visualizar contatos" or escolha == "Visualizar contato":
            visualizar_contatos()
        elif escolha == "3" or escolha == "Excluir contato" or escolha == "Excluir contatos":
            excluir_contato()
        
        