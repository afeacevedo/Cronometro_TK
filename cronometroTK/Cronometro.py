from Hora import *
from Minuto import *
from Segundo import *

class Cronometro:
        def __init__(self):
                self.h = Hora()
                self.m = Minuto()
                self.s = Segundo()
                self.parado = True; #OJO SELF.PARADO
                self.avanzando = True;

        def avanzar(self):
                self.s.avanzar()
                if(self.s.getValor()==0):
                        self.m.avanzar()
                        if(self.m.getValor()==0):
                                self.h.avanzar()

        def getTiempo(self):
                return "{:02d}:{:02d}:{:02d}".format(self.h.getValor(), self.m.getValor(), self.s.getValor())
                # str(self.h.getValor())+":"+str(self.m.getValor())+":"+str(self.s.getValor())

        def cambiarEstado(self):
                self.parado = not self.parado

        def adelanteAtras(self):
		self.avanzando = not self.avanzando	
         
        def retroceder(self):
                self.s.retroceder()
                if self.s.getValor() == self.s.getTope():
                        self.m.retroceder()
                        if self.m.getValor() == self.m.getTope():
                                self.h.retroceder()

        def borrar(self):
                self.h.borrar()
                self.m.borrar()
                self.s.borrar()
