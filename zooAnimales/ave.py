from zooAnimales.animal import Animal


class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    totalAves = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.totalAves += 1
        Ave._listado.append(self)

    def cantidadAves(self):
        return Ave.totalAves

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getListado(cls):
        return cls._listado

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self._colorPlumas