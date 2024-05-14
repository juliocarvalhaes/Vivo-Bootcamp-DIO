saldo = 0
valor_limite_saque = 500
quantidade_limite_saque = 0
historico_saques = []
depositos = []

def deposito(saldo, valor, extrato): 
    if valor <= 0:
        print('Operação falhou! O valor informado é inválido.')
    else:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
    return saldo, extrato

def sacar(valor):
    global saldo, quantidade_limite_saque, valor_limite_saque, historico_saques

    if quantidade_limite_saque >= 3:
        return "Você já realizou 3 saques hoje. Tente novamente amanhã."
    elif valor > valor_limite_saque:
        return f"O valor máximo para saque é de R${valor_limite_saque:.2f}."
    elif saldo < valor:
        return "Saldo insuficiente para realizar o saque."
    else:
        saldo -= valor
        quantidade_limite_saque += 1
        historico_saques.append(valor)
        return f"Saque de R${valor:.2f} realizado com sucesso. Seu saldo atual é R${saldo:.2f}."

def extrato(saldo, historico_saques, depositos):
    if not historico_saques and not depositos:
        print("Não foram realizadas movimentações.")
    else:
        print("Histórico de Saques:")
        for saque in historico_saques:
            print(f"Saque: R${saque:.2f}")
        
        print("\nHistórico de Depósitos:")
        for deposito in depositos:
            print(f"Depósito: R${deposito:.2f}")

    print(f"\nSaldo Atual: R${saldo:.2f}")

# Loop principal
while True:
    print("\nEscolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")
    
    opcao = input("Digite o número correspondente à operação desejada: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo, _ = deposito(saldo, valor_deposito, "")
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso. Seu saldo atual é R${saldo:.2f}")

    elif opcao == '2':
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        mensagem_saque = sacar(valor_saque)
        print(mensagem_saque)

    elif opcao == '3':
        extrato(saldo, historico_saques, depositos)

    elif opcao == '4':
        print("Sessão encerrada.")
        break

    else:
        print("Opção inválida. Por favor, digite um número de 1 a 4.")
