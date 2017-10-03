class Calculadora():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        if type(num1) is not str and type(num2) is not str:
            if num1 >= 10001 or num2 >= 10001:
                return 'No se aceptan numeros mayores a 10000'
            else:
                self.resultado = num1 + num2
                return
        else:
            return 'Datos incorrectos'

    def resta(self, num1, num2):
        if type(num1) is not str and type(num2) is not str:
            if num1 >= 10001 or num2 >= 10001:
                return 'No se aceptan numeros mayores a 10000'
            else:
                self.resultado = num1 - num2
                return
        else:
            return 'Datos incorrectos'

    def multi(self, num1, num2):
        if type(num1) is not str and type(num2) is not str:
            if num1 >= 10001 or num2 >= 10001:
                return 'No se aceptan numeros mayores a 10000'
            else:
                self.resultado = num1 * num2
                return
        else:
            return 'Datos incorrectos'

    def divi(self, num1, num2):
        if type(num1) is not str and type(num2) is not str:
            if num1 >= 10001 or num2 >= 10001:
                return 'No se aceptan numeros mayores a 10000'
            elif num2 == 0:
                return 'No se puede dividir entre 0'
            else:
                self.resultado = num1 / num2
                return
        else:
            return 'Datos incorrectos'

    def expo(self, num1, num2):
        if type(num1) is not str and type(num2) is not str:
            if num1 >= 10001 or num2 >= 10001:
                return 'No se aceptan numeros mayores a 10000'
            else:
                self.resultado = num1**num2
                return
        else:
            return 'Datos incorrectos'

    def raiz(self, num1):
        if type(num1) is not str:
            if num1 >= 10001:
                return 'No se aceptan numeros mayores a 10000'
            elif num1 < 0:
                return 'Error, no puede sacar raiz a numeros negativos'

            else:
                self.resultado = num1**0.5
                return
        else:
            return 'Datos incorrectos'

    def prueba(self):
        if True:
            pass
            if False:
                pass
            for x in xrange(1, 10):
                pass
