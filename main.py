from colorama import Fore, Style, init #instalar a biblioteca
from time import sleep
init(autoreset=True)
#defininfo o banco de dados das contas
class ContaBancaria:
    def __init__(self, nome, cpf, saldo_inicial=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo_inicial

    def mostrar_informacoes(self):
        print(f"{Fore.GREEN}Nome: {self.nome}")
        print(f"{Fore.GREEN}CPF: {self.cpf}")
        print(f"{Fore.GREEN}Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"{Fore.YELLOW}Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(f"{Fore.RED}Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"{Fore.YELLOW}Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(f"{Fore.RED}Saldo insuficiente ou valor inválido para saque.")

    def transferir(self, valor, outra_conta):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            outra_conta.saldo += valor
            print(f"{Fore.YELLOW}Transferência de R$ {valor:.2f} para {outra_conta.nome} realizada com sucesso!")
        else:
            print(f"{Fore.RED}Saldo insuficiente ou valor inválido para transferência.")

def exibir_menu():
    print(Fore.BLUE + "*" * 30)
    print(Fore.GREEN + "Welcome to BANCOC".center(30))
    print(Fore.BLUE + "*" * 30)
    print('''Actions:
    (1) Criar nova conta
    (2) Exibir informações da conta
    (3) Saque
    (4) Depósito
    (5) Transferência
    (6) Ver saldo
    (7) Sair
    ''')

#ações do menu
def main():
    contas = {}
    conta = None

    while True:
        exibir_menu()
        try:
            acao = int(input("Por favor, selecione uma ação: "))
            sleep(1.5)
        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Por favor insira um npumero.")
            sleep(1.5)
        continue

        if acao == 1:
            nome = input('Nome: ')
            while True:
                cpf = input ("CPF: ")
                if len(cpf) ==1 and cpf.isdigit():
                    break
                else:
                    print(f"{Fore.RED}CPF Inválido. Certifique-se de que ele contém exatamente 11 dígitos numéricos.")
                    sleep(1.5)
            try:
                saldo_inicial = float(input("Saldo inicial: R$ "))
                conta = ContaBancaria(nome, cpf, saldo_inicial)
                contas[cpf] =  conta 
                print(f"{Fore.YELLOW}Conta criada com sucesso!")
                sleep(1.5)
            except ValueError:
                print(f"{Fore.RED}Saldo inicial inválido.")
                sleep(1.5)
                
        elif conta is None:
            print(f"{Fore.RED}Nenhuma conta foi criada ainda. Crie uma conta primeiro.")
            sleep(1.5)

        elif acao == 2:
            cpf_consulta = input("Digite o CPF da conta a ser consultada: ")
            if cpf_consulta in contas:
                contas[cpf_consulta].mostrar_informacoes()
            else:
                print(f"{Fore.RED}Conta não encontrada para o CPF informado.")
                sleep(1.5)

        elif acao == 3:
            try:
                valor = float(input("Valor para saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print(f"{Fore.RED}Valor inválido para saque.")
                sleep(1.5)  

        elif acao == 4:
            try:
                valor = float(input("Valor para depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print(f"{Fore.RED}Valor inválido para depósito.")
                sleep(1.5) 

        elif acao == 5: #testar pra ver se ta salvando as contas
            cpf_destino = input("CPF da conta destino: ")
            if cpf_destino in contas:
                conta_destino = contas[cpf_destino]
                try:
                    valor = float(input("Valor para transferência: R$ "))
                    conta.transferir(valor, conta_destino)
                except ValueError:
                    print(f"{Fore.RED}Valor inválido para transferência.")
                    sleep(1.5) 
            else:
                print(f"{Fore.RED}Conta destino não encontrada.")
                sleep(1.5)

        elif acao == 6:
            print(f"{Fore.GREEN}Saldo atual: R$ {conta.saldo:.2f}")

        elif acao == 7:
            print(f"{Fore.YELLOW}Obrigado por usar o BANCOC. Até logo!")
            break

        else:
            print(f"{Fore.RED}Ação inválida. Por favor, tente novamente.")
            sleep(1.5) 

main()