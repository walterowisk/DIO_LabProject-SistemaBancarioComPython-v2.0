import textwrap

def menu():
    menu = """\n
    ====== ESCOLHA UMA OPERAÇÃO ========

    [d]\tDepositar Valor
    [s]\tSacar Valor
    [e]\tConsultar Extrato
    [cu]\tCriar usuário
    [ac]\tAbrir conta
    [lc]\tListar contas
    [x]\tEncerrar Operação

    >>  """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n!!! Depósito realizado com sucesso! !!!")
    else:
        print("\n## Falha na operação! O valor informado é inválido. ##")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n## Falha na operação! Você não tem saldo suficiente. ##")

    elif excedeu_limite:
        print("\n## Falha na operação! O valor do saque excede o limite de saque único. ##")

    elif excedeu_saques:
        print("\n## Falha na operação! Número máximo de saque diário excedido. ##")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n!!! Saque realizado! Recolha seu dinheiro. !!!")

    else:
        print("\n## Falha na operação! O valor informado é inválido. ##")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n=========================================\n")

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n## Erro! Já existe usuário com esse CPF! ##")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (Logradouro, nº - Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n!!! Usuário criado com sucesso! !!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n!!! Conta criada com sucesso! !!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n## Usuário não encontrado! Retornando para o início. ##")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "cu":
            criar_usuario(usuarios)

        elif opcao == "ac":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "x":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
