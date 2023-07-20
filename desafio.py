saldo = 0
limite = 500
extrato = "0.00"
numero_saque = 0
LIMITE_SAQUE = 3

print( """
      =========== menu =============
        [1] Depopsitar
        [2] Sacar
        [3] Extratro
        [0] Sair
      ==============================

""")
while True:
    opcao = float(input("Informe a opção desejada: "))

    if opcao == 1:
        valor = float (input('Informe o valor desejado para deposito. '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósto : R$ {valor:.2f}/n'

            print( """
      =========== menu =============
        [1] Depopsitar
        [2] Sacar
        [3] Extratro
        [0] Sair
      ==============================

        """)
        

        else :
            print ("Operação falhou ! Valor informado invalido ")
        
        
    elif opcao == 2:
        valor = float (input('Informe o valor desejado para o saque . '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print ("Operação invalida ! Limite insuficiente. ")
        
        elif excedeu_limite:
            print(' Operação Falou ! O valor desejado excedeu o limite .')

        elif excedeu_saques:
            print("Operação falhou ! O numero de saques excedeu .")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : {valor:.2f}/n"

            print( """
      =========== menu =============
        [1] Depopsitar
        [2] Sacar
        [3] Extratro
        [0] Sair
      ==============================

        """)
        
        else:
            print('Falha na operação ! o valor informado é invalido. ')


    
    elif opcao == 3:
        print("\n =============== Extrato ===============")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo disponivel: R$ {saldo:.2f}")
        print("========================================")



        print( """
      =========== menu =============
        [1] Depopsitar
        [2] Sacar
        [3] Extratro
        [0] Sair
      ==============================

        """)
    
    elif opcao == 0:
        print('Programa finalizado! até logo , Obrigado por ser nosso cliente .')
        break
    

    else:
        print('opção invalida! por favor selecione uma opção valida')
    
