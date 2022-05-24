#Definimos las diferentes librerías que utilizaremos. 
from re import purge
import pygame
import random

pygame.init()
pygame.font.init()

#Clase Principal
class DISEÑO(pygame.sprite.Sprite):
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
        self.comida=pygame.image.load("comida.png").convert()
        self.comida.set_colorkey(self.blanco)
        self.rect=self.comida.get_rect()
        #self.icono=pygame.image.load("icono.png")

        #-------------------FUENTES DE TEXTO
        self.fuente_numeros=pygame.font.SysFont("Cooper",40)
        self.fuente_titulos=pygame.font.SysFont("Snap ITC",80)
        self.fuente_textos=pygame.font.SysFont("Arial",20)
        
        #-------------------VARIABLES DE APOYO
        self.inicio=True
        self.cuadritos=50
        self.x=random.randrange(self.cuadritos,self.tamaño_pantalla[0]-self.cuadritos,self.cuadritos)
        self.y=random.randrange(self.cuadritos*2,self.tamaño_pantalla[1]-self.cuadritos,self.cuadritos)

    def pantalla_de_juego(self):

        self.tamaño_pantalla=[900,650]
        self.pantalla=pygame.display.set_mode(self.tamaño_pantalla)
        pygame.display.set_caption("CULEBRITA")
        #pygame.display.set_icon(self.icono) ---> AÚN FALTA EL ÍCONO

    def marco(self):
        grosor = 8
        
        # Líneas horizontales del área de juego
        pygame.draw.line(self.pantalla,self.negro,(50,100),(850,100), grosor)
        pygame.draw.line(self.pantalla,self.negro,(50,600),(850,600), grosor)

        # Líneas verticales del área de juego.
        pygame.draw.line(self.pantalla,self.negro,(50,97),(50,604), grosor)
        pygame.draw.line(self.pantalla,self.negro,(850,97),(850,604), grosor)       
        
class LOGICA(DISEÑO):
    def __init__(self):
        super().__init__()

    def comida_aleatoria(self):
        self.x=random.randrange(self.cuadritos,self.tamaño_pantalla[0]-self.cuadritos,self.cuadritos)
        self.y=random.randrange(self.cuadritos*2,self.tamaño_pantalla[1]-self.cuadritos,self.cuadritos)

class JUEGO_FINAL(LOGICA):
    def __init__(self):
        super().__init__()

    def eventos_general(self):
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                self.inicio=False
            
            # TECLAS
            if evento.type==pygame.KEYDOWN:
                #SOLAMENTE EJEMPLO DE COMIDA ALEATORIA
                if evento.key==pygame.K_DOWN:
                    self.comida_aleatoria()
        self.marco()

    def juego_culebrita(self):
        self.pantalla_de_juego()
        self.variables()
        while self.inicio:
            self.pantalla.blit(self.fondo,(0,0))

            self.eventos_general()
            self.pantalla.blit(self.comida,(self.x,self.y))
            
            #Actualizar pantalla
            pygame.display.flip()

pruebas=JUEGO_FINAL()
pruebas.juego_culebrita()


#-------------------COMENTARIOS------------------
# Quitar la comida con la tecla de abajo, solo fue ejemplo
# Pensar como colocar a la culebrita. 
# Diseñar ícono para la pantalla de juego
# Pensar en el menú.