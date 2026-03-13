
class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []


class BancoDoStark:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular: str):
        if titular in self.contas:
            print('ERRO - Conta já existe:', titular)
            return
        self.contas[titular] = Conta(titular)
        print('OK - Conta criada para:', titular)

    def depositar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        # Observação: validações intencionalmente simples (para QA encontrar problemas)
        self.contas[titular].saldo += valor
        self.contas[titular].extrato.append(('deposito', valor))
        print('OK - Depósito realizado:', valor)

    def sacar(self, titular: str, valor: float):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        if self.contas[titular].saldo < valor:
            print('ERRO - Saldo insuficiente')
            return
        self.contas[titular].saldo -= valor
        self.contas[titular].extrato.append(('saque', valor))
        print('OK - Saque realizado:', valor)

    def transferir(self, origem: str, destino: str, valor: float):
        if origem not in self.contas:
            print('ERRO - Conta origem não encontrada')
            return
        if destino not in self.contas:
            print('ERRO - Conta destino não encontrada')
            return
        if self.contas[origem].saldo < valor:
            print('ERRO - Saldo insuficiente')
            return
        self.contas[origem].saldo -= valor
        self.contas[destino].saldo += valor
        self.contas[origem].extrato.append(('transferencia_saida', valor))
        self.contas[destino].extrato.append(('transferencia_entrada', valor))
        print('OK - Transferência realizada:', valor)

    def saldo_atual(self, titular: str):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        print('SALDO', titular, '=', self.contas[titular].saldo)

    def mostrar_extrato(self, titular: str):
        if titular not in self.contas:
            print('ERRO - Conta não encontrada:', titular)
            return
        print('EXTRATO:', titular)
        for item in self.contas[titular].extrato:
            print(' -', item)


banco = BancoDoStark()
print('Banco do Stark carregado!')

# =========================================
# CENÁRIO INICIAL (caminho feliz)
# =========================================

print('=== CRIAR CONTAS ===')
banco.criar_conta('tony')
banco.criar_conta('pepper')
banco.criar_conta('banner')

print('\n=== DEPÓSITOS ===')
banco.depositar('tony', 1000)
banco.depositar('pepper', 500)

print('\n=== SALDOS ===')
banco.saldo_atual('tony')
banco.saldo_atual('pepper')

print('\n=== SAQUE ===')
banco.sacar('tony', 200)
banco.saldo_atual('tony')

print('\n=== TRANSFERÊNCIA ===')
banco.transferir('tony', 'pepper', 100)
banco.saldo_atual('tony')
banco.saldo_atual('pepper')

print('\n=== EXTRATO (tony) ===')
banco.mostrar_extrato('tony')

print('\n=================================')
print('TESTES NEGATIVOS (QA)')
print('=================================\n')

print('Teste N1 - Depósito com valor zero')
banco.depositar('tony', 0)

print('\nTeste N2 - Depósito negativo')
banco.depositar('tony', -100)

print('\nSaldo após depósitos inválidos')
banco.saldo_atual('tony')

print('\nTeste N3 - Saque acima do saldo')
banco.sacar('tony', 100000)

print('\nTeste N4 - Transferência para conta inexistente')
banco.transferir('tony', 'thor', 50)

print('\nTeste N5 - Consulta de conta inexistente (saldo)')
banco.saldo_atual('natasha')

print('\nTeste N6 - Consulta de conta inexistente (extrato)')
banco.mostrar_extrato('natasha')

print('\n=================================')
print('TESTES ADICIONAIS (BUSCA DE BUGS)')
print('=================================\n')

print('Teste Extra 1 - Transferência para si mesmo')
banco.transferir('tony', 'tony', 10)

print('\nTeste Extra 2 - Transferência com valor negativo')
banco.transferir('tony', 'pepper', -50)

print('\nTeste Extra 3 - Saque com valor negativo')
banco.sacar('tony', -20)

print('\nSaldo final Tony:')
banco.saldo_atual('tony')
