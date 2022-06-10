#Importamos las librerías que usaremos
import pygame
import random

#Iniciamos pygame
pygame.init()
pygame.font.init()


# --- Esta clase incliye toda la parte del diseño usada para la creación del juego, también las variables
class  DISEÑO():
    def __init__(self):
        # ----- COLORES
        self.corinto_claro=(184, 27, 105)
        self.rojo_claro=(207,100,79)
        self.blanco=(255,255,255)
        self.negro=(0,0,0)
        self.corinto=(104, 13, 58 )    
        self.celeste=(50, 219, 216)

        # ----- FUENTES DE TEXTO
        self.fuente_numeros=pygame.font.SysFont("Snap ITC",25)
        self.fuente_textos=pygame.font.SysFont("Cooper",25)

        # ----- IMAGENES
        self.menu_inicio=pygame.image.load("menu_inicio.png")
        self.final_salir=pygame.image.load("salir.png")
        self.final_repetir=pygame.image.load("repetir.png")

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
        self.direccion=""
        self.bordes=[]
        self.perder=False
        self.menu=0

    def pantalla_de_juego(self):
        self.tamaño_pantalla=[self.ancho,self.alto]
        self.pantalla=pygame.display.set_mode(self.tamaño_pantalla)
        pygame.display.set_caption("CULEBRITA")

# ---- Líneas guía que limitaran el área de juego
    def marco_bordes(self):
        # Bordes de ancho
        self.bordes.append(pygame.draw.rect(self.pantalla,self.negro,[40,40,520,10]))
        self.bordes.append(pygame.draw.rect(self.pantalla,self.negro,[40,610,520,10]))

        # Bordes de alto
        self.bordes.append(pygame.draw.rect(self.pantalla,self.negro,[40,47,10,568]))
        self.bordes.append(pygame.draw.rect(self.pantalla,self.negro,[550,47,10,568]))


# ---- Líneas guía que irán dentro del área de juego
    def marco_lineas(self):
        alto=self.diferencia1-4
        ancho=self.diferencia2-3
        x=y=30
        for z in range(alto):
            x+=self.espacios
            pygame.draw.line(self.pantalla,self.negro,(x,50),(x,self.alto-40))
        
        for z in range(ancho):
            y+=self.espacios
            pygame.draw.line(self.pantalla,self.negro,(50,y),(self.ancho-50,y))

# --- Nos muestra las opciones que tenemos al morir en el juego
    def menu_final(self):
        self.pantalla.blit(self.final_salir,(-5,85))
        self.pantalla.blit(self.final_repetir,(110,75))

# ---- Esta clase incluye toda la parte lógica del juego
class LOGICA(DISEÑO):
    def __init__(self):
        super().__init__()

# --- Detecta hacia que dirección se está moviendo la serpiente
# --- Utiliza la función de nuevos elementos para ir eliminado la posición anterior y actualizarla
    def movimientos_serpiente(self):
        if self.direccion=="derecha":
            apoyo=self.cuerpo_serpiente[0][0]+self.velocidad
            self.nuevos_elementos(apoyo,"x")
        
        if self.direccion=="izquierda":
            apoyo=self.cuerpo_serpiente[0][0]-self.velocidad
            self.nuevos_elementos(apoyo,"x")

        if self.direccion=="abajo":
            apoyo=self.cuerpo_serpiente[0][1]+self.velocidad
            self.nuevos_elementos(apoyo,"y")

        if self.direccion=="arriba":
            apoyo=self.cuerpo_serpiente[0][1]-self.velocidad
            self.nuevos_elementos(apoyo,"y")


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
                # --- La cabeza es de color verde
                self.cabeza=pygame.draw.rect(self.pantalla,self.corinto,[cuerpo[0],cuerpo[1],20,20])
                continue
            # --- El cuerpo es de color rojo
            pygame.draw.rect(self.pantalla,self.corinto_claro,[cuerpo[0],cuerpo[1],20,20])

# --- Detecta si la cabeza ha topado con los bordes, con ella misma o con la comida
    def colisiones(self):

        colision1=pygame.Rect.colliderect(self.cabeza,self.bordes[0])
        colision2=pygame.Rect.colliderect(self.cabeza,self.bordes[1])
        colision3=pygame.Rect.colliderect(self.cabeza,self.bordes[2])
        colision4=pygame.Rect.colliderect(self.cabeza,self.bordes[3])
        colision_comida=pygame.Rect.colliderect(self.cabeza,self.comida)
        
        if self.cuerpo_serpiente[0] in self.cuerpo_serpiente[2:]:
            self.pantalla.fill(self.corinto,self.cabeza)
            self.perder=True
            self.menu=2

        if colision1 or colision2 or colision3 or colision4:
            self.perder=True
            self.menu=2
        
        if colision_comida:
            self.puntos+=1
            posiciones=[self.x,self.y]
            self.cuerpo(posiciones)
            self.coorde_aleatorias()

# ---- Implementación de la comida
    def coorde_aleatorias(self):
        self.x=random.randrange(50,550,self.espacios)
        self.y=random.randrange(50,610,self.espacios)

# ---- Muestra la comida en pantalla aleatoriamente
    def comida_pantalla(self):
        self.comida=pygame.draw.rect(self.pantalla,self.rojo_claro,[self.x,self.y,20,20])

# --- Inserta un nuevo cuerpo luego de haber comido
    def cuerpo(self,val):
        self.cuerpo_serpiente.insert(0,val) 
        self.serpiente_pantalla()

# --- Confome la serpiente va comiendo, va aumentando el puntaje en pantalla
    def puntaje_pantalla(self):
        puntos=self.fuente_numeros.render("Puntos:"+str(self.puntos),True,self.negro)
        self.pantalla.blit(puntos,(10,5))

# --- Vuelve los valores principales a su estado original para iniciar una nueva jugada
    def reset(self):
        self.cuerpo_serpiente=[[150,150],[170,150]]
        self.direccion=""
        self.puntos=0
        self.perder=False

# --- Esta clase ya incluye la parte final del juego y los eventos de pygame utilizados.
class JUEGO_FINAL(LOGICA):
    def __init__(self):
        super().__init__()

# --- Incluye solamente los movimientos de la serpiente y la opción de salir del juego.
    def eventos_serpiente(self):
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


# --- Incluye las opciones que tenemos al momento de iniciar nuestro juego (Menú principal)
    def eventos_menu_principal(self):
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                self.inicio=False
            
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_s:
                    self.menu=1

                if evento.key==pygame.K_x:
                    self.inicio=False

# --- Incluye las opciones que tenemos al momento de morir en el juego (Menú Final)
    def eventos_menu_final(self):
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                self.inicio=False
            
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_r:
                    self.reset()
                    self.menu=1

                if evento.key==pygame.K_x:
                    self.inicio=False
                    
# --- Esta función es la principal y es la que incluye todas las funciones.
    def juego_culebrita(self):
        self.pantalla_de_juego()
        self.coorde_aleatorias()

        while self.inicio:
            self.fps.tick(10)

            # -- Fondo de la pantalla
            self.pantalla.fill(self.celeste)
            self.marco_bordes()

            # --- Juego Principal
            if self.menu==1:
                # --- Guía de colores para cabeza y cuerpo
                pygame.draw.rect(self.pantalla,self.corinto,(200,10,20,20))
                pygame.draw.rect(self.pantalla,self.corinto_claro,(400,10,20,20))
                cabeza=self.fuente_textos.render("CABEZA",True,self.negro)
                self.pantalla.blit(cabeza,(230,10))

                cuerpo=self.fuente_textos.render("CUERPO",True,self.negro)
                self.pantalla.blit(cuerpo,(430,10))

                self.eventos_serpiente()
                self.comida_pantalla()
                self.marco_lineas()
                self.puntaje_pantalla()
                if self.perder==False:
                    self.movimientos_serpiente()
                self.serpiente_pantalla()
                self.colisiones()
                if self.menu==2:
                    self.menu_final()

            #--- Marco para el menú principal
            if self.menu==0:
                self.eventos_menu_principal()
                self.pantalla.blit(self.menu_inicio,(40,40))
                self.marco_bordes()

            #--- Marco para el menú final    
            if self.menu==2:
                self.puntaje_pantalla()
                self.comida_pantalla()
                self.marco_lineas()
                self.serpiente_pantalla()
                self.colisiones()
                self.eventos_menu_final()
                self.menu_final()

            #Actualizar pantalla
            pygame.display.flip()

juego_definitivo=JUEGO_FINAL()
juego_definitivo.juego_culebrita()


#--------------- COMENTARIOS ------------------
