from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import  CDT


class SimulaBancario :
    # Aqui va el codigo del CDT
    """-------------------------
    # Atributos
    ------------------------"""
    cedula = ""
    nombre = ""
    mesActual = 0  
    """#ASOCIACIONES"""
    CuentaCorriente= CuentaCorriente
    CuentaAhorros = CuentaAhorros
    CDT = CDT
    """-----------------------------
    #METODOS
    ------------------------------"""  
    def ConsignacionValor (self,NuevaConsignacionValor):
        #Aqui va el codigo de la nueva consignacion
        return 0
    def CambiarRetirarValor (self,NuevoRetirarValor):
        #Aqui va el codigo del retiro
        return 0
    def CambiarInteresMensual (self,NuevoInteresMensual):
        #Aqui va el codigo del Interes
        return 0
    def CambiarSimulaBancario (self,nNuevoConsignacionValor, nNuevoRetirarValor, nNuevoInteresMensual):
        #Aqui va el codigo del Simulador Bancario
        return 0
    def ConsultarConsignacionValor (self):
        #Aqui va el codigo de la consulta de la Consignacion
        return self.ConsultarConsignacionValor
    def ConsultarRetirarValor (self):
        #Aqui va el codigo de la consulta del Retiro
        return self.ConsultarRetirarValor
    def ConsultarInteresMensual (self):
        #Aqui va el codigo de la consulta del interes
        return self.ConsultarInteresMensual
    
    def RetiroSimuladorBancario ( Self.nConsignarCuentaCorriente, nCalcularSaldoTotal, nSaldoCuentaCorriente, nSaladoCuentaAhorros, nRetirarValor, nSaldoFinal):
        return 0
    
       """--------------------------
       #METODOS
       --------------------------"""
    def ConsignarCuentaCorriente (self):
        #Aqui va el codigo de la consigna de la cuenta
        return self.ConsignarCuentaCorriente
    def ConsignarCuentaAhorros (self):
        #Aqui va el codigo
        return self.ConsignarCuentaAhorros
        """------------------
        #CONSULTAR SALDO
        -------------------"""
    def SaldoCorriente (self):
        return 0
    def SaldoAhorros (self):
        return 0
    def CalcularSaldoTotal(self):
        return "Su saldo total es" +(self.SaldoCorriente+self.SaldoAhorros)
    """-------------------
    #PASAR DE AHORROS A CORRIENTE
    ----------------------"""
    def TranferirCorriente(self):
        self.SaldoAhorros + self.ConsignarCuentaCorriente
    """-------------------
    Cuenta bancaria
    ---------------------"""
    def CalcularSaldoTotal (self):
        #Aqui va el codigo
        return "CalcularSaldoTotal:" +(self.CuentaAhorros.saldo+self.CuentaCorriente.saldo+self.CDT.saldo)
    def ConsultarRetirarValor(self):
        #Aqui va el codigo de la consulta
        return "RetirarValor" +(self.RetiroSimuladorBancario+self.CalcularSaldoTotal)
    def CuentaAhorrosCuentaCorriente (self):
       
    