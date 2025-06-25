menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[n] Nova conta
[l] Listar contas
[q] Sair

=> """

# ============ FUNÇÕES BANCÁRIAS ============
def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("❌ Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("❌ Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("❌ Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("❌ Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("✅ Saque realizado com sucesso!")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# ============ FUNÇÕES DE CADASTRO ============
def criar_usuario(usuarios):
    print("\n=== Cadastro de Usuário ===")
    cpf = input("CPF (somente números): ").strip()

    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario_existente:
        print("❌ CPF já cadastrado! Usuário não será criado.")
        return None

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Endereço (rua, número - bairro - cidade/estado): ").strip()

    print("✅ Usuário criado com sucesso!")
    return {"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco}

def criar_conta_corrente(usuario, numero_conta):
    print("\n=== Criando Conta Corrente ===")
    agencia = "0001"
    conta = {
        "agencia": agencia,
        "numero": f"{numero_conta:06d}",
        "usuario": usuario
    }
    print(f"✅ Conta criada com sucesso para {usuario['nome']}! Número: {conta['numero']}")
    return conta

def listar_contas_correntes(contas):
    print("\n=== Contas Correntes Cadastradas ===")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            usuario = conta["usuario"]
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {usuario['nome']}")

# ============ PROGRAMA PRINCIPAL ============
def main():
    usuarios = []
    contas = []
    numero_conta = 1

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "n":
            usuario = criar_usuario(usuarios)
            if usuario:
                usuarios.append(usuario)
                conta = criar_conta_corrente(usuario, numero_conta)
                contas.append(conta)
                numero_conta += 1

        elif opcao == "l":
            listar_contas_correntes(contas)

        elif opcao == "q":
            print("✅ Obrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("❌ Operação inválida. Por favor, escolha novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
