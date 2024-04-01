from banco import ContaBancaria

c1 = ContaBancaria("Igor", 0)

c1.mostrarSaldo()

c1.depositar(150.50)
c1.mostrarSaldo()
c1.sacar(50.50)
c1.mostrarSaldo()
c1.emprestimo(1000, 50)
c1.mostrarSaldo()
c1.mostrarSaldoDevedor()
