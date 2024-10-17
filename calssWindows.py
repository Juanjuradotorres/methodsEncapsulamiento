import tkinter as tk
class widow:
    __ancho=500
    __alto=500
    __titulo="test"
    __resize=True


    def setdiemnsion (self,width,height):
        self.__ancho=width
        self.__alto=height

    def getdiemnsion (self):
        return  [self.__ancho,self.__alto]
    def setresize(self,resize):
        self.__resize=resize

    def getresize(self):
        return self.__resize
    def gettitulo(self):
        return self.__titulo

    def crear_ventana(self):
        # Crear la ventana principal

        ventana = tk.Tk()

        ventana.title(self.__titulo)

        # Establecer el tamaño de la ventana (n x m píxeles)

        ventana.geometry(f"{self.__ancho}x{self.__alto}")

        # Evitar que la ventana sea redimensionable

        ventana.resizable(self.__resize, self.__resize)

        # Iniciar el bucle principal de la ventana

        ventana.mainloop()