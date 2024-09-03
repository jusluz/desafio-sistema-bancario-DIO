import textwrap
import os

def limpar_tela():
     os.system('cls' if os.name == 'nt' else 'clear')

def nome_programa():
     print('''
█████████████████████████████████████████
█▄─▄▄─█▄─█─▄███▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─█─▄█
██─▄▄▄██▄─▄█████─▄─▀██─▀─███─█▄▀─███─▄▀██
▀▄▄▄▀▀▀▀▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀ d
           
     ''')

def menu():
     menu = '''\n
     __________ MENU ___________

     [d]\tDepositar
     [s]\tSacar
     [e]\tExtrato
     [nc]\tNova conta
     [lc]\tListar contas
     [nu]\tNovo usuário
     [q]\tSair
     => '''

     return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
     try:     
          if valor > 0:
               saldo += valor
               extrato += f"Depósito: R$ {valor:.2f}\n"
               print('\n=== Depósito realizado com êxito. ===')
          else:
               print("\n@@@ Operação falhou! O Valor informado é inválido. @@@")
     except:
          print("\n@@@ Operação falhou! Tente novamente. @@@")
     
     return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques >= limite_saques     
     
     try:
          if excedeu_saldo:
               print("\n@@@ Saldo insuficiente. @@@")
          elif excedeu_limite:
               print("\n@@@ Valor de saque excedido. @@@")
          elif excedeu_saques:
               print("\n@@@ Limite de saques diários excedido. @@@")
          
          elif valor > 0:
               saldo -= valor
               extrato -= f"Saque: R$ {valor:.2f}\n"
               numero_saques += 1
               print('\n=== Saque realizado com êxito. ===')
          
          else:
               print("\n @@@ Valor inválido. @@@")
     except:
          print("Valor inválido")
     
def exibir_extrato(saldo, /, *, extrato,):
     print('\n=========== EXTRATO ===========')
     print("Não foram realizadas movimentação" if not extrato else extrato)
     print(f'\nSaldo:\t\tR$ {saldo:.2f}')
     print('=================================')

     
def criar_usuario(usuarios):
     try:
     
          cpf = input("Informr o CPF (somente número)s:")
          usuario = filtrar_usuario(cpf, usuarios)

          if usuario:
               print("\n@@@ CPF já cadastrado. @@@")
               return
          
          nome = input('Informe o nome completo: ')
          #senha = input('Informe a senha: ')
          data_nascimento = input('Inform e a data de  nascimento (dd-mm-aaaa): ')
          endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

          usuarios.append({'nome:': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
          print('\n=== Usuário criado com sucesso! ===')
     
     except:
          print('\n@@@ Erro ao criar usuário. @@@')

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input('Informe o CPF do usuário: ')
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print('\n=== Conta criada com sucesso!. ===')
          return {'agencia': agencia,'numero_conta': numero_conta,'usuario': usuario}
     
     print('\n@@@ Usuário não encontrado, conta não pôde ser criada. @@@')
     
def listar_contas(contas):
     for conta in contas:
          linha = f'''\
               Agência:\t{conta['agencia']}
               C/C:\t\t{conta['numero_conta']}
               Titular:\t{conta['usuario']['nome']}
          '''

          print('=' * 100)
          print(textwrap.dedent(linha))

def main():
     limpar_tela()
     nome_programa()

     LIMITE_SAQUES = 3
     AGENCIA = "0001"

     saldo = 0
     limite = 500
     extrato = ''
     numero_saques = 0
     usuarios = []
     contas = []

     while True:
          
          opcao = menu()
          opcao = opcao.lower()
     
          if opcao == 'd':
               valor = float(input("Informe o valor de depósito: "))
                         
               saldo, extrato = depositar(saldo, valor, extrato)
               
          elif opcao == 's':
               valor = float(input("Informe o valor do saque: "))
               
               saldo, extrato, sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
               )
               
          elif opcao == 'e':
               exibir_extrato(saldo, extrato=extrato)

          elif opcao == 'nu':
               criar_usuario(usuarios)
                
          elif opcao == 'nc':
               numero_conta = len(contas) +1
               conta = criar_conta(AGENCIA, numero_conta, usuarios)

               if conta:
                    contas.append(conta)
                
          elif opcao == 'lc':
               listar_contas(contas)
               
          elif opcao == 'q':
               break
          
          else:
               print("Opção inválida, por favor selecione novamente a operação desejada.")
          
main()






