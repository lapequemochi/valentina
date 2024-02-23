class Empleado :
    # Aqui va el codigo del empleado
    """-----------------------------
    # Atributos 
    --------------------------"""
    nombre = ""
    apellido = ""
    """----------------------------
    # 1 - Masculino 2 = Femenino ---"""
    sexo = 0
    salario = 0
    """----------------------------
    # Metodos
    ----------------------------"""
    def CambiarSalario(Self, nuevoSalario):
        # Aqui va el codigo del metodo
        return 0
    
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va el codigo del nuevo empleado
        return None

    def ConsultarSalario(self):
        # Aqui va el codigo del metodo
        return self.salario
    
    def ConsultarNombre(self):
        # Aqui va el codigo del metodo
        return self.nombre
    
    def ConsultarApellido(self):
        # Aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        return self.nombre +" "+ self.apellido
    
    def ConsultarSexo(self):
        # Aqui va el codigo del metodo
        return self.sexo
    
    def AumentoSalarial(self):
        nSalario =self.salario = 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario
        return "El nuevo salario es de : " + self.salario
    