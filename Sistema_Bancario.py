menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[t] Transferir
[c] Central de Ajuda
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_para_conta_destinaria = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input('Digite o valor a ser depositado: R$ '))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito efetuado: R${deposito:.2f}\n"
        else:
            print('O valor do depósito deve ser acima de zero!')

    elif opcao == "s":
        print("Saque")

        if LIMITE_SAQUES > numero_saques:
            saque = float(input('Digite um valor a ser sacado: R$'))
        
            if  saque > 500 or saque > saldo or saque < 0:
                print ("Valor inválido, saque novamente")
            else:
                numero_saques +=1
                saldo = saldo - saque
                extrato += f"Saque efetuado: R${saque:.2f}\n"
        else:
            print('Você atingiu seu limite de saques, portanto não poderá sacar.')

    elif opcao == "e":
        if extrato == "":
            print('Não foram realizadas movimentações')
        else:
            print(f"========= Extrato =========\n{extrato}===========================")
    
    elif opcao == "q":
        print(f'O saldo Atual é: R$ {saldo:.2f}')
        
        if extrato == "":
            print('Não foram realizadas movimentações')
        else:
            print(f"""========= Extrato =========\n{extrato}===========================""")
        break
    elif opcao == "t":
        conta_destinataria = int(input(f'Transferência\nDigite o número da conta que deseja transferir: '))
        Valor_Transferido = int(input('Digite um valor para transferir: '))
        if Valor_Transferido > saldo:
            print('Você não tem essa grana toda não! Digite um valor válido.')
        else: 
            valor_para_conta_destinaria += Valor_Transferido
            extrato += f'Transferência de R${valor_para_conta_destinaria} efetuada para a conta de número {conta_destinataria}\n'
            
    elif opcao == "c":
        Duvida = input('Digite sua dúvida: ')
        print('Agradecemos pela dúvida, nossa central em breve retornará com uma resposta detalhada!')

    else:
        print ("Operação invalida, por favor selecione novamente a operação desejada.")
