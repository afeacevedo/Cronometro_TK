from Tkinter import *
from threading import *
from time import sleep
from Cronometro import *

class InterfaceCronometros(Thread):

    def __init__(self):
        self.root = Tk()
        self.crono = Cronometro()
        self.crono.cambiarEstado()
        self.frame = Frame(self.root)
        self.frame.pack()

        self.cadena = StringVar()
        #self.display = Entry(self.frame, textvariable=self.cadena)
        self.display = Label(self.frame, textvariable=self.cadena, font=("Helvetica", 30))
        self.display.grid(row=0, column=1)

        self.buttonIniciar = Button(self.frame, text="Iniciar/Parar")
        self.buttonIniciar.bind("<Button-1>", self.cambio)
        self.buttonIniciar.grid(row=1, column=0)

        
        self.buttonAvanzar = Button(self.frame, text="Avanzar/Retroceder")
        self.buttonAvanzar.bind("<Button-1>", self.avanzarRetroceder)
        self.buttonAvanzar.grid(row=1, column=1)
        
        
        self.buttonBorrar = Button(self.frame, text="Borrar")
        self.buttonBorrar.bind("<Button-1>", self.borrar)
        self.buttonBorrar.grid(row=1, column=2)

        Thread.__init__(self)
        self.start()

        self.root.mainloop()



    def cambio(self, event):
        self.crono.cambiarEstado()

    def avanzarRetroceder(self, event):
        self.crono.adelanteAtras()

    def borrar(self, event):
        self.crono.borrar()

    def run(self):
        while True:
            if not self.crono.parado:
                if (self.crono.avanzando):
                    self.crono.avanzar()
                else:
                    self.crono.retroceder()
            sleep(0.1)
            self.cadena.set(self.crono.getTiempo())

    def callback(self):
        self.root.quit()


app = InterfaceCronometros()
