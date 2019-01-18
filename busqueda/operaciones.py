class BusquedaBinaria():
	
	# Se crea el metodo init para agregar los datos y ordenarlos
	def __init__(self, x):
		self.datos = sorted(x)

	# Se crea el metodo para buscar de forma binaria, el cual recibe la llave a buscar
	def busqueda(self, n):
		self.inferior = 0  # Extremo inferior del area de busqueda
		self.superior = len(self.datos) - 1  # Extremo superior del area de busqueda
		self.medio = int((self.inferior + self.superior + 1) / 2)  # Elemento Medio
		self.ubicacion = -1  # Devuelve el valor -1 si es que no se llega a encontrar
		self.flag = True  # Se declara el booleano para poder salir del while
		self.c = 0  # Se declara el contador 

		# El ciclo se repetira hasta que el booleano sea falso o el contador exceda la cantidad de elementos de la lista
		while self.flag and self.c <= len(self.datos):  
			if n == self.datos[self.medio]:  # Si el elemnto se encuentra en medio
				self.ubicacion = self.medio  # Ubicacion toma la posicion del elemto medio actual
				self.flag = False  # El booleano se vuelve falso y se termina el ciclo
			elif n < self.datos[self.medio]:  # Si el elemento es menor a medio
				self.superior = self.medio - 1  # Se desecha la parte superior de la lista
			else:  # Si el elemento es mayor a medio
				self.inferior = self.medio + 1  # Se desecha la parte inferior de la lista 
			self.medio = int((self.inferior + self.superior + 1) / 2)
			self.c = self.c +1  # Se incrementa el contador
		return self.ubicacion  # Se retorna la ubicacion

	# Metodo para presentar los elementos de la lista
	def __str__(self):
		p = ''
		for d in self.datos:
			p = '%s %d' % (p, d)
		return p

