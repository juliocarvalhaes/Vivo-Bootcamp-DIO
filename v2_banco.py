def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos do CPF
    
    # Verifica se já existe algum usuário com o mesmo CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário cadastrado com esse CPF.")
            return
    
    nome = input("Insira o nome completo do usuário: ")
    data_nascimento = input("Insira a data de nascimento do usuário no formato dd-mm-aaaa: ")
    endereco = input("Insira o endereço (logradouro - bairro - cidade/sigla estado): ")
    
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return

def conta_corrente(usuarios, contas):
    numero_conta = input('Insira o n° da sua conta: ')
    #Verificando se o usuário está ativo
    status_usuario = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            status_usuario = usuario
            break
    if not status_usuario:
        print("Usuário não encontrado ou inativo no momento")
        return
    numero_conta = float(input('Insira o n° da sua conta: '))
    #Verifica de o primeiro n° da conta é igual a 1:
    if numero_conta[0] != '1':
        numero_conta = str(len(contas) + 1)
        print('Número da Conta errado ou inexistente. Insira novamente')
        return conta_corrente(usuario, contas)
        
    else:
       conta_atual = {
        'agencia': '0001',  # Agência padrão
        'numero_conta': numero_conta,
        'usuario': usuario
        }
    conta_atual = { 'agencia': '0001', 'numero_conta': numero_conta , 'usuario': usuario }
    contas.append(conta_atual)
    return 
    
    
def verifica_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

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
def main():
        saldo = 0
        valor_limite_saque = 500
        quantidade_limite_saque = 0
        historico_saques = []
        depositos = []
        usuarios = []
        contas = []
        # Loop principal
        while True:
            print("\nEscolha uma opção:")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Novo Usuário")
            print("5. Nova Conta Corrente")
            print("6. Sair")
            
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
                cadastrar_usuario(usuarios)
                print("Usuário criado com sucesso!")
            
            elif opcao == '5':
                conta_corrente(usuarios, contas)

            elif opcao == '6':
                print("Sessão encerrada.")
                break

            else:
                print("Opção inválida. Por favor, digite um número de 1 a 4.")


main()