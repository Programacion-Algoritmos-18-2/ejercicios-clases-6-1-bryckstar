# Se importan los paquetes necesarios
from paquete_archivos.miarchivo import MiArchivo
from busqueda.operaciones import *

m = MiArchivo() # Se crea un objeto de tipo Miarchivo para poder abrir los datos

lista = m.obtener_informacion()  # Se obtienen los datos de el archivo

lista = [l.split(",") for l in lista]  # Se crea un split para separar los datos por coma



lista_numeros = []  # Se crea la lista para almacenar los datos

for d in lista:  # Se recorre cada linea de los datos
	for i in d:  # Se recorre cada elemento de los datos
		lista_numeros.append(int(i))  # Se agregan los elementos a la lista transformados a enteros

b = BusquedaBinaria(lista_numeros)  # Se agregan los datos al metodo para buscar de forma binaria y los ordena
print(b)  # Se imprime la lista ordenada

key = 3  # Se decalara la llave que se desea buscar

pos = b.busqueda(key)  # Se obtiene la posicion de la llave dada

# Se presentan los resultados
if pos == -1:
	print('El entero %d no se encontro\n' % (key))
else:
	print('El entero %d se encuentra en la posicion: %d' % (key, pos))