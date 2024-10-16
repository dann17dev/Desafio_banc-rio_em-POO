from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao("Saque", self.valor)
        else:
            return "Operação falhou! Você não tem saldo suficiente."

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao("Depósito", self.valor)
        else:
            return "Operação falhou! O valor informado é inválido."

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        self.transacoes.append(transacao)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property 
    def cliente(self):
        return self._cliente

    @property 
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False
        self._saldo -= valor
        return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

# Menu e controle de usuários e contas
menu = """ 
[d] Depositar 
[s] Sacar 
[e] Extrato 
[c] Criar Usuário 
[cc] Criar Conta Corrente 
[l] Listar Contas 
[q] Sair 

=> """ 

usuarios = []  # Lista para armazenar usuários 
contas = []  # Lista para armazenar contas 
numero_conta = 1  # contador para número da conta 

# Função para criar usuários
def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Usuário já cadastrado com esse número de CPF!")
            return None  # retornar None se já existir o CPF

    novo_usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)  
    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente(usuario_cpf):
    global numero_conta  
    agencia = "0001"

    usuario_localizado = None
    for usuario in usuarios:
        if usuario.cpf == usuario_cpf:
            usuario_localizado = usuario
            break

    if not usuario_localizado:
        print("Usuário não localizado!")
        return None  

    nova_conta = ContaCorrente(numero_conta, usuario_localizado)
    contas.append(nova_conta)  
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

    numero_conta += 1  

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(f"Agência: {conta.agencia}, Número da Conta: {conta.numero}, Titular: {conta.cliente.nome}")
    print("==================================================")

# Loop principal 
while True:
    opcao = input(menu)

    if opcao == "d":  # Depositar
        cpf = input("Informe o CPF do usuário: ")
        valor = float(input("Informe o valor do depósito: "))
        for conta in contas:
            if conta.cliente.cpf == cpf:
                deposito = Deposito(valor)
                erro = deposito.registrar(conta)  # Usando a classe Deposito
                if erro:
                    print(erro)
                else:
                    print("Depósito realizado com sucesso!")
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "s":  # Sacar
        cpf = input("Informe o CPF do usuário: ")
        valor = float(input("Informe o valor do saque: "))
        for conta in contas:
            if conta.cliente.cpf == cpf:
                saque = Saque(valor)
                erro = saque.registrar(conta)  # Usando a classe Saque
                if erro:
                    print(erro)
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "e":  # Extrato
        cpf = input("Informe o CPF do usuário: ")
        for conta in contas:
            if conta.cliente.cpf == cpf:
                print("\n================ EXTRATO ================")
                for transacao in conta.historico.transacoes:
                    print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
                print(f"Saldo: R$ {conta.saldo:.2f}")
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "c":  # Criar Usuário
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade - estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "cc":  # Criar Conta Corrente
        cpf = input("Informe o CPF do usuário: ")
        criar_conta_corrente(cpf)

    elif opcao == "l":  # Listar Contas
        listar_contas()

    elif opcao == "q":  # Sair
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
