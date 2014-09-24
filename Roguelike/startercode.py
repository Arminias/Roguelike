from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import random

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=(255, 255, 255))

        self.SpielerVec = vec2d(20, 20)                           #X Koordinate des Spielers (von links nach rechts)self.SpielerY = 20 Y Koordinate des Spielers (von oben nach unten)
        self.pos = vec2d(20,20)
        self.target = vec2d(20,20)
        self.drawcolor = (0, 0, 0)
        def placeWall (self, koordinateX, koordinateY):                   #Generiert random Zahlen um die Map Random zu Generieren
            randomnumber = random.randint(0,2)
            if randomnumber == 0:
                self.screen.blit(self.img3, (koordinateX, koordinateY))

        self.img1 = pygame.image.load("tilesets/derek/HeroBase.png")
        self.img2 = pygame.image.load("tilesets/derek/Dirt.png")
        self.img3 = pygame.image.load("tilesets/fegon/Wall.png")
        for temp in range (0,29,):                  #Lädt die obere Begrenzungslinie
            self.screen.blit(self.img2, (20*temp, 0))
        for temp in range (0,30,):                  #Lädt die untere Begrenzungslinie
            self.screen.blit(self.img2, (20*temp, 580))
        for temp in range (0,29):                   #Lädt die linke Begrenzungslinie
            self.screen.blit(self.img2, (0, 20*temp))
        for temp in range (0,29):                   #Lädt die rechte Begrenzungslinie
            self.screen.blit(self.img2, (580, 20*temp))
        self.screen.blit(self.img1, (20, 20))
        self.screen.blit(self.img3, (20, 40))

        for temp1 in range (1,29):                  #Generiert die Map und geht alle Felder durch
            for temp2 in range (1,29):
                placeWall (self,temp1*20,temp2*20)

        self.maximallebenspieler = 100                                  #Maximalleben
        self.lebenspieler = 100                                    #Aktuelles Leben
        self.ErstschlagSpieler = 10
        self.StaerkeSpieler = 10
        self.GeschicklichkeitSpieler = 10
        self.AusdauerSpieler = 10
        self.MagieSpieler = 10

    def keyDown(self,key):
            if key == K_w:
                 self.SpielerVec +=  (0,-20)
            elif key == K_a:
                self.SpielerVec += (-20,0)
            elif key == K_s:
                self.SpielerVec += (0,20)
            elif key == K_d:
                self.SpielerVec += (20,0)
    def update(self):

        self.screen.blit(self.img1, (self.SpielerVec))#, self.SpielerY))
        if self.lebenspieler < self.maximallebenspieler:
            self.lebenspieler += 0.0001
        elif self.lebenspieler > self.maximallebenspieler:
            self.lebenspieler = self.maximallebenspieler1
        pass






    def mouseUp(self, button, pos):
        self.target = vec2d( pos)


    def mouseMotion(self, buttons, pos, rel):
        pass

    def quit (self, key):
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw(self):
        self.screen.blit(self.img1, (self.SpielerVec))
        pygame.display.flip()
        pass



s = Starter()
s.mainLoop(120)
