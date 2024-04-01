class ContaBancaria:
    def __init__ (self, nome, saldo):
        self. nome = nome
        self. saldo=  saldoDevedor = 0

    def depositar (self, valor):
        self. saldo += valor

    def sacar (self, valor):
        self. saldo -= valor
        
    def mostrarSaldo (self):
        print("Seu saldo é de: ", self. saldo)

    def mostrarSaldoDevedor (self):
        print("Seu saldo devedor é de: ", self. SaldoDevedor)

    def emprestimo(self, valor, prazo):
        self. saldo += valor
        self. saldoDevedor += (valor + valor * (prazo / 100))

