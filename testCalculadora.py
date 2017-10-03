import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):
    """docstring for CalculadoraTest"""

    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_es_igual_a_cero(self):
        self.assertEquals(self.calc.obtener_resultado(),0)
        
    def test_sumar_dos_mas_dos(self):
        self.calc.suma(2,2)
        self.assertEquals(self.calc.obtener_resultado(),4)
    
    def test_sumar_tres_mas_tres(self):
        self.calc.suma(3,3)
        self.assertEquals(self.calc.obtener_resultado(),6)

    def test_sumar_menos_uno_mas_dos(self):
        self.calc.suma(-1,2)
        self.assertEquals(self.calc.obtener_resultado(),1)

    def test_sumar_letra_mas_uno(self):
        error = self.calc.suma('l',1)
        self.assertEquals(error,'Datos incorrectos')
    
    def test_suma_numeros_grandes(self):
        error = self.calc.suma(100001,1)
        self.assertEquals(error,'No se aceptan numeros mayores a 10000')





    def test_resta_dos_menos_dos(self):
        self.calc.resta(2,2)
        self.assertEquals(self.calc.obtener_resultado(),0)

    def test_resta_cuatro_menos_tres(self):
        self.calc.resta(4,3)
        self.assertEquals(self.calc.obtener_resultado(),1)

    def test_resta_menosuno_mas_dos(self):
        self.calc.resta(-1,2)
        self.assertEquals(self.calc.obtener_resultado(),-3)
    
    def test_resta_menosuno_menosdos(self):
        self.calc.resta(-1,-2)
        self.assertEquals(self.calc.obtener_resultado(),1)

    def test_resta_letras(self):
        error = self.calc.resta('l',2)
        self.assertEquals(error,'Datos incorrectos')

    def test_resta_numeros_grandes(self):
        error = self.calc.resta(100001,1)
        self.assertEquals(error,'No se aceptan numeros mayores a 10000')




    def test_multi_tres_x_tres(self):
        self.calc.multi(3,3)
        self.assertEquals(self.calc.obtener_resultado(),9)

    def test_multi_menosdos_x_tres(self):
        self.calc.multi(-2,3)
        self.assertEquals(self.calc.obtener_resultado(),-6)

    def test_multi_diez_x_cuatro(self):
        self.calc.multi(10,-4)
        self.assertEquals(self.calc.obtener_resultado(),-40)        

    def test_multi_menoscuatro_x_menosnueve(self):
        self.calc.multi(-4,-9)
        self.assertEquals(self.calc.obtener_resultado(),36)     

    def test_multi_seis_x_cero(self):
        self.calc.multi(6,0)
        self.assertEquals(self.calc.obtener_resultado(),0)      

    def test_multi_letra_x_letra(self):
        error = self.calc.multi('boy','girl')
        self.assertEquals(error,'Datos incorrectos')        

    def test_multi_numeros_grandes(self):
        error = self.calc.multi(10004,10007)
        self.assertEquals(error,'No se aceptan numeros mayores a 10000')        




    def test_divi_menostres_entre_menostres(self):
        self.calc.divi(-3,-3)
        self.assertEquals(self.calc.obtener_resultado(),1)
    

    def test_divi_menoscinco_entre_uno(self):
        self.calc.divi(-5,1)
        self.assertEquals(self.calc.obtener_resultado(),-5)


    def test_divi_cuatro_entre_menosuno(self):
        self.calc.divi(4,-1)
        self.assertEquals(self.calc.obtener_resultado(),-4)

    def test_divi_numeros_grandes(self):
        error = self.calc.divi(10003,10006)
        self.assertEquals(error,'No se aceptan numeros mayores a 10000')

    def test_divi_letras(self):
        error = self.calc.divi('hey','hola')
        self.assertEquals(error,'Datos incorrectos')

    def test_divi_entre_cero(self):
        error = self.calc.divi(100,0)
        self.assertEquals(error,'No se puede dividir entre 0')




    def test_expo_tres_a_cero(self):
        self.calc.expo(3,0)
        self.assertEquals(self.calc.obtener_resultado(),1)

    def test_expo_menostres_a_menostres(self):
        self.calc.expo(-3,-3)
        self.assertEquals(self.calc.obtener_resultado(),-0.037037037037037035
)

    def test_expo_seis_a_menosdos(self):
        self.calc.expo(6,-2)
        self.assertEquals(self.calc.obtener_resultado(),0.027777777777777776)


    def test_expo_menoscinco_a_cinco(self):
        self.calc.expo(-5,5)
        self.assertEquals(self.calc.obtener_resultado(),-3125)

    def test_expo_numeros_grandes(self):
        error = self.calc.expo(10001,10002)
        self.assertEquals(error, 'No se aceptan numeros mayores a 10000')

    def test_expo_letras(self):
        error = self.calc.expo('Hola','karim')
        self.assertEquals(error, 'Datos incorrectos')




    def test_raiz_25(self):
        self.calc.raiz(25)
        self.assertEquals(self.calc.obtener_resultado(),5)

    def test_raiz_menostres(self):
        error = self.calc.raiz(-3)
        self.assertEquals(error,'Error, no puede sacar raiz a numeros negativos')

    def test_raiz_cero(self):
        self.calc.raiz(0)
        self.assertEquals(self.calc.obtener_resultado(),0)

    def test_raiz_letras(self):
        error = self.calc.raiz('hola')
        self.assertEquals(error,'Datos incorrectos')

    def test_raiz_numeros_grandes(self):
        error = self.calc.raiz(10004)
        self.assertEquals(error,'No se aceptan numeros mayores a 10000')


    
if __name__ == '__main__':
    unittest.main()
