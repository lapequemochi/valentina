from Fecha import Fecha

class Empleado :
    #aqui va el codigo del empleado
    """----------------------------
    #atributos
    -------------------------------"""
    cedula=""
    nombre=""
    apellido=""
    
    """----------------------------
    #1 =Masculino y 2=Femenino
    -------------------------------"""
    sexo=0
    salario=0
    """----------------------
    Numero de hijos del empleado
    -----------------"""
    NumeroHijosEmpleado = 0

    """-----------------------------
     #asociaciones
    --------------------------------"""
    
    fechaNacimiento= Fecha()
    fechaIngreso= Fecha()

    """----------------------------
    #metodos
    -------------------------------"""

    def __init__(self, cedula,nombre, apellido, sexo, salario):
        self.cedula =cedula
        self.nombre =nombre
        self.apellido =apellido
        self.sexo =sexo
        self.salario =salario

    def __init__(self, numerohijos):
        self.NumeroHijosEmpleado =numerohijos
       

    def CambiarSalario(self, nuevoSalario):
        #aqui va el codigo
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #aqui va el codigo
        return None
    def ConsultarSalario(self):
        #aqui va el codigo
        return self.salario
    def ConsultarNombre(self):
        #aqui va el codigo
        return self.nombre
    def ConsultarApellido(self):
        return self.apellido
    def ConsultarNombreCompleto(self):
        return self.nombre +""+ self.apellido
    def AumentoSalarial(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario +self.salario
        self.salario = nSalario
        return "el nuevo salario es de: "+self.salario
    
    def DuplicarSalario (self):
        #aqui va el codigo
        #forma 1
        #self.salario *= self.salario*2
        self.salario *=2

    def CalcularSalarioAnual (self):
        #aqui va el codigo
        #forma 1
        salarioAnual= self.salario * 12
        #forma 2
        #return SalarioAnual *12

    def Consultardiacumpleanios(self):
        return "el dia de su cumpleaños es: "+self.fechaNacimiento.ConcultarDia()
    
    def CalcularImpuesto(self):
        #forma 1
        total = self.CalcularSalarioAnual()
        return (total * 19.5)/100
    #forma 2
    #return self.CalcularSalarioAnual() * 0.195

    def CalcularAuxilioEducativo (self):
        #aqui va el codigo
        #forma 1
        AuxilioEducativo= self.salario * self.NumeroHijosEmpleado * 0.5

    def CalcularAuxilioEducativoPorcentaje (self):
        #aqui va el codigo
        #forma 1
        AuxilioEducativoPorcentaje= self.salario * 0.5

    def CalcularDiferenciaSalarial(self):
        # Forma1
        Empleado1 = self.empleado.consultarsalario()
        Empleado2 = self.empleado.consultarsalario()
        return "Diferencia de Salarios Empleado1 y Empleado2: " + Empleado1-Empleado2
