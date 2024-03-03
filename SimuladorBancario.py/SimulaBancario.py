from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import  CDT


class SimulaBancario :
    # Aqui va el codigo del CDT
    """-------------------------
    # Atributos
    ------------------------"""
    cedula=''
    nombres=''
    mesActual=''

    """---------------------------
    #1 =VIP 2= Platino 3= Normal
    --------------------------------"""
    TipoDeCliente= ''

    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    
    corriente = CuentaCorriente()
    ahorros = CuentaAhorros()
    cdt = CDT()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    """---------------------------
    Inicializacion tipo de cliente #1 =VIP 2= Platino 3= Normal
    --------------------------------"""
    
    def __init__(self, cedula, nombres, mesActual, TipoDeCliente):
        self.cedula = cedula
        self.nombres = nombres
        self.mesActual = mesActual
        self.TipoDeCliente = TipoDeCliente

    def CambiarTipoDeCliente(self):
        nTipoDeCliente = self.TipoDeCliente
        self.TipoDeCliente = nTipoDeCliente

        #aqui va el codigo

    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0

    def consultarSaldoCorriente (self):
        return "Tu saldo es: "+self.corriente.consultarsaldo()
        
    def DuplicarAhorro(self):
        #forma 1
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo())
        #forma 2
        self.ahorros.saldo *= 2
    def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.ahorros.RetirarMonto(self.ahorros.saldo())
        self.corriente.RetirarMonto(self.corriente.saldo())
        return "Retirarse total: "+total
