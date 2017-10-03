# -*- coding: utf-8 -*-
import unittest

from edad import Edad

class testEdad(unittest.TestCase):
	"""docstring for Edad Test"""

	def setUp(self):
		self.edad = Edad()

	def test_no_existes(self):
		edad = self.edad.calcular_edad(-1)
		self.assertEquals(edad,'No existes')

	def test_nino(self):
		edad = self.edad.calcular_edad(12)
		self.assertEquals(edad, 'Eres niño')

	def test_adolescente(self):
		edad = self.edad.calcular_edad(17)
		self.assertEquals(edad, 'Eres adolescente')

	def test_adulto(self):
		edad = self.edad.calcular_edad(64)
		self.assertEquals(edad, 'Eres adulto')

	def test_adulto_mayor(self):
		edad = self.edad.calcular_edad(120)
		self.assertEquals(edad, 'Eres adulto mayor')


	def test_mumm_ra(self):
		edad = self.edad.calcular_edad(121)
		self.assertEquals(edad, 'Eres Mumm-Ra')

	def test_letras(self):
		edad = self.edad.calcular_edad('hola')
		self.assertEquals(edad, 'Datos incorrectos')


		

	

	
if __name__ == '__main__':
	unittest.main()
