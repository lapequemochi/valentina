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
    def CambiarConsignacionValor (self,NuevaConsignacionValor):
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
    
    def ConsignarCuentaCorriente (self):
        #Aqui va el codigo de la consigna de la cuenta
        return self.ConsignarCuentaCorriente
    def ConsignarCuentaAhorros (self):
        #Aquie va el codigo
        return self.ConsignarCuentaAhorros
    def CalcularSaldoTotal (self):
        #Aqui va el coigo
        return "CalcularSaldoTotal:" +(self.CuentaAhorros.saldo+self.CuentaCorriente.saldo+self.CDT.saldo)
    