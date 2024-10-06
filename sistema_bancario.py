import random
import os

def menu():
    print('Bem vindo ao banco pazuzu!')
    print('Oque voce deseja fazer, escolha uma opcão:','\n') 
    print(16 * '-')
    print('para criar conta digite 1')
    print('para consultar conta digite 2')
    print('para consultar extrato digite 3')
    print('para depositar digite 4')
    print('para sacar digite 5')
    print(16 * '-')

list = []


def limpar_terminal():  
  os.system('cls')
    
def type_cont():
    while True:
     escolha_conta = input('digite o tipo de conta, CORRENTE OU POUPANCA: ')  
     if (escolha_conta == "corrente" or escolha_conta == "poupanca" ):
      print('ok')
      
      return escolha_conta
      
     else:
         print('tente novamente')
    

def listar_conta():
     for i in list:
      print(i["usuario"])
      print(i["id_aleatorio"])
      print(i["cash"])
      print(i["type_conta"])
      print('\n')
            
    
def depositar():
    
        valor = int(input('Qual valor voce deseja depositar: '))
        print(f'O valor depositado é {valor}')
        name = input('Digite o nome do usúario para depositar: ')
        for i in list:
            if name == i['usuario']:
             i['cash'] = valor + i['cash']
            
            else:
             break            
        limpar_terminal()       
    
def extrato():
    conta = input('Qual é o nome do usúario: ')    
    for i in list:
        if conta == i['usuario']:
            print(i["cash"])
        else: 
            break    
  
    
def cadastrar_conta():
    conta = {
        "usuario":input('digite seu nome: '),
        "id_aleatorio": "".join(map(str, random.sample(range(1, 50), 6))),
        "cash": 0,
        "type_conta": type_cont()
    }
    list.append(conta)
  
def saque():
    subtracao = int(input('Qual valor voce deseja sacar: '))  
    nome = input('Digite o nome do usúario: ')
    for i in list:
        if (nome == i['usuario']):
            i['cash'] = i['cash'] - subtracao
        else:
            break    
    limpar_terminal()   
def run():
    while True:
        menu()
        variavel = int(input('qual é sua opcao: '))
        if (variavel == 2):
            listar_conta()
        elif (variavel == 1):
            cadastrar_conta()    
        elif( variavel == 4):
            depositar()
        elif(variavel == 3):
            extrato()
        elif(variavel == 5):
            saque()
        else:
            break    
        
run()        
        
    
    
    

