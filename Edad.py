# -*- coding: utf-8 -*-
class Concurrencias():

	def obtener_diccionario(self,texto):
	#split each sentences at '.'
	lista = texto.lower().split('.')
	#declare empty dictionary for the counter
	diccionario = {}
	listaAux = []

	for sentence in lista:
		words = sentence.split()
		for word in words:
			index = words.index(word)
			listaAux.append(index)
			if word not in diccionario:
				diccionario[word] = list()
				diccionario[word].append(index)
			else:
				diccionario[word]= list()
				diccionario[word].append(index)
	return diccionario
