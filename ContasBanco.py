# coding=utf-8
from datetime import datetime
import pytz

contas = []

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf, agencia, numero_conta):
        self.saldo = 0
        self.nome = nome
        self.cpf = cpf
        self.tipo = 'corrente'
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é R${:,.2f}'.format(self.saldo))


    def depositar_saldo(self, valor):
        self.saldo += valor
        print('Valor de R${:,.2f} depositado com sucesso'.format(valor))
        self.consultar_saldo()
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def sacar_saldo(self, valor):
        if self.saldo - valor < 0:
            print('Saldo insuficiente')
            self.consultar_saldo()
        else:
            print('Saque realizado com sucesso')
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))


    def historico_transacoes(self):
        print('Histórico de Transacoes')
        print('Valor, Saldo Data e Hora')
        for transacao in self.transacoes:
            print(transacao)


    def tranferencia_saldo(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        print('A transferencia foi realizada no valor de R${:,.2f}'.format(valor))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))



class CartaoCredito:


    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
        self.limite = None
        self.senha = None

## Programa funcionando

conta_hugo = ContaCorrente('hugo', '02099892113', 432543, 54252)

conta_hugo.consultar_saldo()





