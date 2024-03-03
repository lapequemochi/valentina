class CuentaAhorros :
    # Aqui va el codigo de la cuenta de ahorros
    """-----------------------
    # Atributos 
    ----------------------"""
    saldo = 0
    interesMensual = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def ConsultarSaldo(self):
        return self.saldo
    
    def ConsignarMonto(self, monto):
        # #Forma 1
        # self.saldo += monto
        # # Forma 2
        # self.saldo = self.saldo + monto
        # # Forma 3
        total = self.saldo + monto
        self.saldo = total
    
    def RetirarMonto(self, monto):
        # #Forma 1
        # self.saldo -= monto
        # # Forma 2
        # self.saldo = self.saldo - monto
        # # Forma 3
        total = self.saldo - monto
        self.saldo = total
