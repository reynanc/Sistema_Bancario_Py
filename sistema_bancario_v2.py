class ContaCorrente:
    numero_conta = 0

    def __init__(self, cliente):
        ContaCorrente.numero_conta += 1
        self.agencia = "0001"
        self.numero = ContaCorrente.numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.limite_saque = 500
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def realizar_deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True, self.saldo, self.extrato
        else:
            return False, self.saldo, ["Valor de depósito inválido."]

     
    def realizar_saque(self, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
        if valor > 0:
            if saldo >= valor:
                if numero_saques < limite_saques:
                    if valor <= limite:
                        saldo -= valor
                        extrato.append(f"Saque: R$ {valor:.2f}")
                        numero_saques += 1
                        return True, saldo, extrato
                    else:
                        return False, saldo, ["Valor de saque excede o limite permitido."]
                else:
                    return False, saldo, ["Limite de saques diários atingido."]
            else:
                return False, saldo, ["Saldo insuficiente."]
        else:
            return False, saldo, ["Valor de saque inválido."]
        
        
    def visualizar_extrato(self, saldo, *, extrato):
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Extrato:")
        
        if extrato:
            for movimentacao in extrato:
                print(movimentacao)
            else:
                return False, ["Não foram realizadas movimentações."]


def criar_conta_corrente(usuarios, contas):
    cpf = input("Digite o CPF do usuário para vincular à conta-corrente: ")
    usuarios_filtrados = [user for user in usuarios if user.cpf == cpf]

    if not usuarios_filtrados:
        print("Usuário não encontrado.")
        return None

    cliente = usuarios_filtrados[0]
    conta = ContaCorrente(cliente)
    contas.append(conta)
    return conta


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta corrente encontrada.")
        return

    print("Lista de contas correntes: ")
    for idx, conta in enumerate(contas, start=1):
        print(f"{idx}. Agência: {conta.agencia}, Número: {conta.numero}, Cliente: {
              conta.cliente.nome} - Saldo: R$ {conta.saldo:.2f}")


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def formatar_endereco(self):
        return f"{self.endereco['logradouro']}, {self.endereco['numero']}, {self.endereco['bairro']}, {self.endereco['cidade']} - {self.endereco['estado']}"


def criar_usuario(usuarios):
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/YYYY): ")
    cpf = input("Digite o CPF(apenas números): ")
    endereco = {
        "logradouro": input("Digite o logradouro: "),
        "numero": input("Digite o número: "),
        "bairro": input("Digite o bairro: "),
        "cidade": input("Digite a cidade: "),
        "estado": input("Digite a sigla do estado: ")
    }

    if cpf in [user.cpf for user in usuarios]:
        print("CPF já cadastrado.")
        return None

    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    return usuario


    # Menu
menu = """
[1] Criar Usuário
[2] Criar Conta Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar Contas
[0] Sair

=> """

usuarios = []
contas_correntes = []

while True:
    opcao = input(menu)

    # CRIAR CONTA CLIENTE
    if opcao == "1":
        usuario = criar_usuario(usuarios)
        if usuario:
            print(f"Usuário {usuario.nome} criado com sucesso.")

       # CRIAR CONTA CORRENTE
    elif opcao == "2":
        if usuarios:
            conta_corrente = criar_conta_corrente(usuarios, contas_correntes)
            if conta_corrente:
                print(f"Conta corrente {conta_corrente.numero} criada com sucesso para {
                      conta_corrente.cliente.nome}.")
        else:
            print("Crie um usuário primeiro.")

         # DEPOSITAR
    elif opcao == "3":
        if contas_correntes:
            conta_idx = int(
                input("Digite o número da conta-corrente para depositar: ")) - 1
            valor = float(input("Digite o valor para depositar: "))

            if conta_idx >= 0 and conta_idx < len(contas_correntes):
                conta = contas_correntes[conta_idx]
                sucesso, novo_saldo, novo_extrato = conta.realizar_deposito(
                    valor)

                if sucesso:
                    print(f"Depósito de R$ {
                          valor:.2f} realizado com sucesso. Novo saldo: R$ {novo_saldo:.2f}")
                else:
                    print(f"Erro ao realizar depósito: {novo_extrato[-1]}")
            else:
                print("Conta corrente não encontrada.")
        else:
            print("Crie uma conta corrente primeiro.")

           # SACAR
    elif opcao == "4":
        if contas_correntes:
            conta_idx = int(
                input("Digite o número da conta corrente para sacar: ")) - 1
            valor = float(input("Digite o valor para sacar: "))

            if conta_idx >= 0 and conta_idx < len(contas_correntes):
                conta = contas_correntes[conta_idx]
                sucesso, novo_saldo, novo_extrato = conta.realizar_saque(
                    saldo=conta.saldo,
                    valor=valor,
                    extrato=conta.extrato,
                    limite=conta.limite_saque,
                    numero_saques=conta.numero_saques,
                    limite_saques=conta.LIMITE_SAQUES
                )
                if sucesso:
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {
                          novo_saldo:.2f}")
                else:
                    print(f"Erro ao realizar saque: {novo_extrato[-1]}")
            else:
                print("Conta corrente não encontrada.")
        else:
            print("Crie uma conta corrente primeiro.")

        # EXTRATO
    elif opcao == "5":
        if contas_correntes:
            conta_idx = int(input("Digite o número da conta corrente para visualizar o extrato: ")) - 1
            
            if conta_idx >= 0 and conta_idx < len (contas_correntes):
                conta = contas_correntes[conta_idx]
                conta.visualizar_extrato(
                    saldo = conta.saldo,
                    extrato = conta.extrato
                )
            else:
                print("Conta corrente não encontrada.")
        else:
            print("Crie uma conta corrente primeiro.")
           

        # LISTAR CONTAS
    elif opcao == "6":
        listar_contas(contas_correntes)

        # SAIR
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
