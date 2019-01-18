import codecs                   # Importamos las librerias necesarias para poder leer el archivo
import sys


class MiArchivo:                # Creamos una clase MiArchivo
    """
    """
    
    def __init__(self):                                         # Abrir el archivo de la direccion 
        """
        """
        self.archivo = codecs.open("data/datos.txt", "r")       # Carga todas las lineas del archivo

    def obtener_informacion(self):                              # Devolvemos la informacion leida
        return self.archivo.readlines()

    def cerrar_archivo(self):                   # Cerramos el Archivo
        self.archivo.close()