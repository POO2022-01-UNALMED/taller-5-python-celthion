class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return ("Mamiferos : " + str(Mamifero.totalMamiferos) + "\nAves : " + str(Ave.totalAves) +
                "\nReptiles : " + str(Reptil.totalReptiles) + "\nPeces : " + str(
                    Pez.totalPeces) + "\nAnfibios : " + str(Anfibio.totalAnfibios))

    def toString(self):
        if self._zona == None:
            return ("Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(
                self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero))
        else:
            return ("Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(
                self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(
                self._genero) + " la zona en la que me ubico es " + str(self._zona))

    @classmethod
    def setTotalAnimales(cls, num):
        Animal._totalAnimales = num

    def getTotalAnimales(self):
        return Animal._totalAnimales

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setGenero(self, genero):
        self._genero = genero

    def getGenero(self):
        return self._genero

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getHabitat(self):
        return self._habitat