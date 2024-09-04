class Cuenta:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial

    # Métodos
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        elif cantidad > self.__saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    # Getters
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo


cuenta = Cuenta(numero_cuenta=123456, saldo_inicial=1000.0)

# Depositar dinero
cuenta.depositar(222.0)

# Retirar dinero
cuenta.retirar(700.0)

# Intentar retirar más dinero del que hay en la cuenta
cuenta.retirar(15003.0)

# Imprimir saldo actual
print(f"Saldo actual: {cuenta.get_saldo()}")