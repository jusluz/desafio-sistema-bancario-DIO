# Definindo as variáveis

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

menu = '''
█████████████████████████████████████████
█▄─▄▄─█▄─█─▄███▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─█─▄█
██─▄▄▄██▄─▄█████─▄─▀██─▀─███─█▄▀─███─▄▀██
▀▄▄▄▀▀▀▀▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀ 

[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair
=> '''

while True:
    opcao = input(menu)
    opcao = opcao.lower()
 
    if opcao == 'd':
          try:
               valor = float(input("Informe o valor de depósito: "))
               if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f}\n"
               else:
                    print("Valor inválido")
          except ValueError:
               print("Valor inválido")
         
    elif opcao == 's':
          try:
               valor = float(input("Informe o valor do saque: "))
               excedeu_saldo = valor > saldo
               excedeu_limite = valor > limite
               excedeu_saques = numero_saques >= LIMITE_SAQUES

               if excedeu_saldo:
                    print("Saldo insuficiente")
               elif excedeu_limite:
                    print("Valor de saque excedido")
               elif excedeu_saques:
                    print("Limite de saques excedido")
               elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
               else:
                    print("Valor inválido")
          except:
               print("Valor inválido")
         
    elif opcao == 'e':
         print('\n*********** EXTRATO ***********')
         print("Não foram realizadas movimentação" if not extrato else extrato)
         print(f'Saldo: R$ {saldo:.2f}')
         print('********************************')
         
    elif opcao == 'q':
         break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")