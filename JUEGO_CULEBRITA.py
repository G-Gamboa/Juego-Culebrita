#Definimos las diferentes librerías que utilizaremos. 
import pygame
import random

pygame.init()
pygame.font.init()

#Clase Principal
class DISEÑO():
    def __init__(self):
        pass

    def variables(self):
        
        #-------------------COLORES
        self.rojo=(255,0,0)
        self.blanco=(255,255,255)
        self.negro=(0,0,0)
        self.verde=(95,230,49)

        #-------------------IMÁGENES
        self.fondo=pygame.image.load("fondo.png")
        #self.icono=pygame.image.load("icono.png")

        #-------------------PANTALLA
        self.tamaño_pantalla=[900,650]
        self.pantalla=pygame.display.set_mode(self.tamaño_pantalla)
        pygame.display.set_caption("CULEBRITA")
        #pygame.display.set_icon(self.icono) ---> AÚN FALTA EL ÍCONO

        #-------------------FUENTES DE TEXTO
        self.fuente_numeros=pygame.font.SysFont("Cooper",40)
        self.fuente_titulos=pygame.font.SysFont("Snap ITC",80)
        self.fuente_textos=pygame.font.SysFont("Arial",20)
        
        #-------------------VARIABLES DE APOYO
        self.inicio=True

    def marco(self):
        grosor = 8
        
        # Líneas horizontales del área de juego
        pygame.draw.line(self.pantalla,self.negro,(50,100),(850,100), grosor)
        pygame.draw.line(self.pantalla,self.negro,(50,600),(850,600), grosor)

        # Líneas verticales del área de juego.
        pygame.draw.line(self.pantalla,self.negro,(50,97),(50,604), grosor)
        pygame.draw.line(self.pantalla,self.negro,(850,97),(850,604), grosor)

        
class JUEGO_FINAL(DISEÑO):
    def __init__(self):
        super().__init__()

    def eventos_general(self):
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                self.inicio=False
        self.marco()
        

    def juego_culebrita(self):
        self.variables()
        while self.inicio:
            self.pantalla.blit(self.fondo,(0,0))
            #self.pantalla.fill(self.blanco)
            self.eventos_general()

            #Actualizar pantalla
            pygame.display.flip()

pruebas=JUEGO_FINAL()
pruebas.juego_culebrita()
