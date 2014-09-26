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
        self.map = [0]*1000
        def createList (self):                   #Generiert random Zahlen um die Map Random zu Generieren
            for i in range (0,1000):
                self.map[i] = random.randint(0,2)

            print(self.map)
        createList(self)

        self.img1 = pygame.image.load("tilesets/derek/HeroBase.png")
        self.img2 = pygame.image.load("tilesets/derek/Dirt.png")
        self.img3 = pygame.image.load("tilesets/fegon/Wall.png")
        self.imgGolem = pygame.image.load("tilesets/fegon/Golem.png")
        self.imgVampire = pygame.image.load("tilesets/fegon/Vampire.png")
        self.imgGoblin = pygame.image.load("tilesets/fegon/Goblin.png")
        self.imgDragon = pygame.image.load("tilesets/fegon/Dragon.png")

        self.anzahlMobs = 5
        self.Mob1skin = random.randint(1, 4)
        self.Mob1pos = vec2d(random.randint(1,28), random.randint(1, 28))
        while self.map [(self.Mob1pos[0]-1) *28+ self.Mob1pos[1]] == 0: # or self.Mob1pos == 0:
            print ("1")
            self.Mob1pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[self.Mob1pos[0]*28+self.Mob1pos[1]] = 10 + self.Mob1skin

        self.Mob2skin = random.randint(1, 4)
        self.Mob2pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        while self.map [(self.Mob2pos[0]-1) *28+ self.Mob2pos[1]] <= 0: # or self.Mob2pos == 0:
            print ("2")
            self.Mob2pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        self.map[self.Mob2pos[0]-1*28+self.Mob2pos[1]] = 10 + self.Mob2skin

        self.Mob3skin = random.randint (1, 4)
        self.Mob3pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        while self.map[(self.Mob3pos[0]-1) *28+ self.Mob3pos[1]] <= 0: # or self.Mob3pos == 0:
            print ("3")
            self.Mob3pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        self.map[self.Mob3pos[0]*28+self.Mob3pos[1]] = 10 + self.Mob3skin

        self.Mob4skin = random.randint(1, 4)
        self.Mob4pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        while self.map [(self.Mob4pos[0]-1) *28+ self.Mob4pos[1]] <= 0: # or self.Mob4pos == 0:
            print ("4")
            self.Mob4pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[self.Mob4pos[0]*28+self.Mob4pos[1]] = 10 + self.Mob4skin
        print (self.Mob1pos)
        print (self.Mob2pos)
        print (self.Mob3pos)
        print (self.Mob4pos)
        print (self.map)

        self.maximallebenspieler = 100                                  #Maximalleben
        self.lebenspieler = 100                                    #Aktuelles Leben
        self.ErstschlagSpieler = 10
        self.StaerkeSpieler = 10
        self.GeschicklichkeitSpieler = 10
        self.AusdauerSpieler = 10
        self.MagieSpieler = 10

    def keyDown(self,key):
            print (self.SpielerVec)
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
        self.screen.fill((220,180,130))
        for temp in range (0,30,):                  #Lädt die obere Begrenzungslinie
            self.screen.blit(self.img2, (20*temp, 0))
        for temp in range (0,30,):                  #Lädt die untere Begrenzungslinie
            self.screen.blit(self.img2, (20*temp, 580))
        for temp in range (0,30):                   #Lädt die linke Begrenzungslinie
            self.screen.blit(self.img2, (0, 20*temp))
        for temp in range (0,30):                   #Lädt die rechte Begrenzungslinie
            self.screen.blit(self.img2, (580, 20*temp))
        for temp3 in range (0,28):       #Lädt das innere der Map
            temp4 = 0
            #print (temp3)
            for temp4 in range (0,28):
                #print (temp4)
                if self.map[temp3*28+temp4] == 0:
                    self.screen.blit(self.img3, (temp4* 20+20,temp3*20+20))
        self.screen.blit(self.img1, (self.SpielerVec))
        if self.Mob1skin == 1:
            self.screen.blit(self.imgGolem, (self.Mob1pos*20))
        elif self.Mob1skin == 2:
            self.screen.blit(self.imgVampire, (self.Mob1pos*20))
        elif self.Mob1skin == 3:
            self.screen.blit(self.imgGoblin, (self.Mob1pos*20))
        elif self.Mob1skin == 4:
            self.screen.blit(self.imgDragon, (self.Mob1pos*20))
        if self.Mob2skin == 1:
            self.screen.blit(self.imgGolem, (self.Mob2pos*20))
        elif self.Mob2skin == 2:
            self.screen.blit(self.imgVampire, (self.Mob2pos*20))
        elif self.Mob2skin == 3:
            self.screen.blit(self.imgGoblin, (self.Mob2pos*20))
        elif self.Mob2skin == 4:
            self.screen.blit(self.imgDragon, (self.Mob2pos*20))
        if self.Mob3skin == 1:
            self.screen.blit(self.imgGolem, (self.Mob3pos*20))
        elif self.Mob3skin == 2:
            self.screen.blit(self.imgVampire, (self.Mob3pos*20))
        elif self.Mob3skin == 3:
            self.screen.blit(self.imgGoblin, (self.Mob3pos*20))
        elif self.Mob3skin == 4:
            self.screen.blit(self.imgDragon, (self.Mob3pos*20))
        if self.Mob4skin == 1:
            self.screen.blit(self.imgGolem, (self.Mob4pos*20))
        elif self.Mob4skin == 2:
            self.screen.blit(self.imgVampire, (self.Mob4pos*20))
        elif self.Mob4skin == 3:
            self.screen.blit(self.imgGoblin, (self.Mob4pos*20))
        elif self.Mob4skin == 4:
            self.screen.blit(self.imgDragon, (self.Mob4pos*20))
        pygame.display.flip()




s = Starter()
s.mainLoop(120)
