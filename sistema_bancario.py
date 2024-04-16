#DESAFIO:
#Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
#Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
#Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

#OPERAÇÃO DE DEPÓSITO
#Deve ser possível depositar valores positivos para a minha conta bancária. 
#A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agencia e conta bancária. 
#Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

#OPERAÇÃO DE SAQUE
#O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
#Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
#Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#OPERAÇÃO DE EXTRATO
#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
#Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações".
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx
#Exemplo: 1500.45 = R$ 1500.45

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Digite o valor para depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        else:
            print("Valor de depósito inválido. Tente mais tarde!")


    elif opcao == "2":
            valor = float(input("Digite o valor para sacar: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
                
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

            else:
                print("O valor informado é inválido..")
                        
            
    elif opcao == "3":
        if extrato:
            print(extrato + f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
