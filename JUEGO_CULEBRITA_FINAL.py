#Importamos las librerías que usaremos
import pygame
import random

#Iniciamos pygame
pygame.init()
pygame.font.init()

class  DISEÑO():
    def __init__(self):
        # ----- COLORES
        self.rojo_fuerte=(255,0,0)
        self.rojo_claro=(207,100,79)
        self.blanco=(255,255,255)
        self.negro=(0,0,0)
        self.verde=(95,230,49)    
        self.celeste=(50, 219, 216)

        # ----- FUENTES DE TEXTO
        self.fuente_numeros=pygame.font.SysFont("Snap ITC",20)
        self.fuente_titulos=pygame.font.SysFont("Cooper",40)
        self.fuente_textos=pygame.font.SysFont("Arial",20)

        # -----VARIABLES DE APOYO
        self.inicio=True
        self.ancho=600
        self.alto=650
        self.espacios=20
        self.diferencia1=int(self.ancho/self.espacios)
        self.diferencia2=int(self.alto/self.espacios)
        self.puntos=0
        self.fps=pygame.time.Clock()
        self.largo=1
        self.velocidad=20
        self.cuerpo_serpiente=[[150,150],[170,150]]
        self.direccion=random.choice(['arriba','abajo','izquierda','derecha'])
        self.bordes=[]


    def pantalla_de_juego(self):
        self.tamaño_pantalla=[self.ancho,self.alto]
        self.pantalla=pygame.display.set_mode(self.tamaño_pantalla)
        pygame.display.set_caption("CULEBRITA")

    def fondo(self):
        self.pantalla.fill(self.celeste)
        grosor=8
        alto=self.diferencia1-4
        ancho=self.diferencia2-3
        x=y=30
        for z in range(alto):
            x+=self.espacios
            if z==0 or z==alto-1:
                self.bordes.append(pygame.draw.line(self.pantalla,self.negro,(x,48),(x,self.alto-37),grosor))
            else:  
                pygame.draw.line(self.pantalla,self.negro,(x,50),(x,self.alto-40))
        
        for z in range(ancho):
            y+=self.espacios
            if z==0 or z==ancho-1:
                self.bordes.append(pygame.draw.line(self.pantalla,self.negro,(48,y),(self.ancho-47,y),grosor))
            else:  
                pygame.draw.line(self.pantalla,self.negro,(50,y),(self.ancho-50,y))

class LOGICA(DISEÑO):
    def __init__(self):
        super().__init__()

# --- Detecta hacia que dirección se está moviendo la serpiente
# --- Utiliza la función de nuevos elementos para ir eliminado la posición anterior y actualizarla
    def movimientos_serpiente(self):
        if self.direccion=="derecha":
            apoyo=self.cuerpo_serpiente[0][0]+self.velocidad
            self.nuevos_elementos(apoyo,"x")
            self.tope_bordes(apoyo)
        
        if self.direccion=="izquierda":
            apoyo=self.cuerpo_serpiente[0][0]-self.velocidad
            self.nuevos_elementos(apoyo,"x")
            self.tope_bordes(apoyo)

        if self.direccion=="abajo":
            apoyo=self.cuerpo_serpiente[0][1]+self.velocidad
            self.nuevos_elementos(apoyo,"y")
            self.tope_bordes(apoyo)

        if self.direccion=="arriba":
            apoyo=self.cuerpo_serpiente[0][1]-self.velocidad
            self.nuevos_elementos(apoyo,"y")
            self.tope_bordes(apoyo)

    def nuevos_elementos(self,val,eje):
#--- Dependiendo de su eje inserta la nueva posición en el eje x o en el eje y
        if eje=="x":
            self.cuerpo_serpiente.insert(0,[val,self.cuerpo_serpiente[0][1]])
            self.cuerpo_serpiente.pop()
            self.serpiente_pantalla()
        else:
            self.cuerpo_serpiente.insert(0,[self.cuerpo_serpiente[0][0],val])
            self.cuerpo_serpiente.pop()
            self.serpiente_pantalla()

# --- Dibuja los cuadrados en pantalla
    def serpiente_pantalla(self):
        for indice,cuerpo in enumerate(self.cuerpo_serpiente):
            if indice==0:
                # --- El cuerpo es de color verde
                pygame.draw.rect(self.pantalla,self.verde,[cuerpo[0],cuerpo[1],20,20])
                continue
            # --- La cabeza es de color rojo
            pygame.draw.rect(self.pantalla,self.rojo_fuerte,[cuerpo[0],cuerpo[1],20,20])

# --- Detecta si la cabeza ha topado con los bordes
    def tope_bordes(self,tope):
        if tope<self.espacios:
            self.inicio=False 
        pass

    def puntaje_pantalla(self):
        puntos=self.fuente_numeros.render("Puntos:"+str(self.puntos),True,self.negro)
        self.pantalla.blit(puntos,(10,10))

class JUEGO_FINAL(LOGICA):
    def __init__(self):
        super().__init__()

    def eventos_general(self):
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                self.inicio=False
            
            # TECLAS
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_DOWN:
                    if self.direccion=="arriba":
                        pass
                    else:
                        self.direccion="abajo"

                if evento.key==pygame.K_UP:
                    if self.direccion=="abajo":
                        pass
                    else:
                        self.direccion="arriba"

                if evento.key==pygame.K_LEFT:
                    if self.direccion=="derecha":
                        pass
                    else:
                        self.direccion="izquierda"

                if evento.key==pygame.K_RIGHT:
                    if self.direccion=="izquierda":
                        pass
                    else:
                        self.direccion="derecha"

    def juego_culebrita(self):
        self.pantalla_de_juego()

        while self.inicio:
            self.fps.tick(10)
            # area de dibujo
            self.eventos_general()
            self.fondo()
            self.puntaje_pantalla()
            self.movimientos_serpiente()
            self.puntos+=1
            



            #Actualizar pantalla
            pygame.display.flip()

pruebas=JUEGO_FINAL()
pruebas.juego_culebrita()


#--------------- COMENTARIOS ------------------
# Falta que detecte los bordes del área de juego
# Falta colocar comida
# Falta un menú de inicio