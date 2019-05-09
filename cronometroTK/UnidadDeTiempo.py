class UnidadDeTiempo:
        def __init__(self):
                valor = 0
                tope = 59

        def borrar(self):
                self.valor = 0

        def avanzar(self):
                if self.valor < self.tope:
                        self.valor = self.valor+1
                else:
                        self.valor = 0;

        def resetear(self):
                self.valor = 0

        def getValor(self):
                return self.valor

        def getTope(self):
                return self.tope

        def retroceder (self):
                if self.valor > 0:
                        self.valor = self.valor-1
                else:
                        self.valor = self.tope;
