from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import random

class Starter(PygameHelper):
    def __init__(self):
        print ("Initialisiere das Spiel...")
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=(255, 255, 255))
        self.size = [800,600]
        self.screen = pygame.display.set_mode(self.size)

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
        if self.map[0] == 0:
            self.map[0] = 1
        self.red = [255, 0, 0]
        self.blue = [0, 0, 255]
        self.myfont = pygame.font.SysFont("monospace", 20)
        self.Leveldesign = pygame.font.SysFont("monospace", 40)
        self.Ausdauerimg = pygame.image.load ("tilesets/EigeneBilder/Ausdauer.png")
        self.Verteidigungimg = pygame.image.load ("tilesets/EigeneBilder/Verteidigung.png")
        self.Staerkeimg = pygame.image.load ("tilesets/EigeneBilder/Staerke3.png")
        self.Geschicklichkeitimg = pygame.image.load ("tilesets/EigeneBilder/Geschicklichkeit.png")
        self.Magicimg = pygame.image.load ("tilesets/EigeneBilder/Magic.png")
        self.Attackimg1 = pygame.image.load ("tilesets/fegon/Attackboost.png")
        self.Attackimg2 = pygame.image.load ("tilesets/EigeneBilder/sword2.png")
        self.ItemSlots = pygame.image.load ("tilesets/EigeneBilder/itemslots.png")
        self.img1 = pygame.image.load("tilesets/derek/HeroBase.png")
        self.img2 = pygame.image.load("tilesets/derek/Dirt.png")
        self.img3 = pygame.image.load("tilesets/fegon/Wall.png")
        self.imgGolem = pygame.image.load("tilesets/fegon/Golem.png")
        self.imgVampire = pygame.image.load("tilesets/fegon/Vampire.png")
        self.imgGoblin = pygame.image.load("tilesets/fegon/Goblin.png")
        self.imgDragon = pygame.image.load("tilesets/fegon/Dragon.png")

        self.Mob1Liste = [0]*11
        self.Mob2Liste = [0]*11
        self.Mob3Liste = [0]*11
        self.Mob4Liste = [0]*11
        self.Mob5Liste = [0]*11
        self.Mob6Liste = [0]*11
        self.Mob7Liste = [0]*11
        self.Mob8Liste = [0]*11
        self.Mob1inventory1 = [0] * 13
        self.Mob1inventory2 = [0] * 13
        self.Mob2inventory1 = [0] * 13
        self.Mob2inventory2 = [0] * 13
        self.Mob3inventory1 = [0] * 13
        self.Mob3inventory2 = [0] * 13
        self.Mob4inventory1 = [0] * 13
        self.Mob4inventory2 = [0] * 13
        self.Mob5inventory1 = [0] * 13
        self.Mob5inventory2 = [0] * 13
        self.Mob6inventory1 = [0] * 13
        self.Mob6inventory2 = [0] * 13
        self.Mob7inventory1 = [0] * 13
        self.Mob7inventory2 = [0] * 13
        self.Mob8inventory1 = [0] * 13
        self.Mob8inventory1 = [0] * 13



        self.anzahlMobs = 5
        self.Mob1Liste[0] = random.randint (1,8)
        self.Mob1Liste[1] = random.randint(1, 4)
        self.Mob1Liste[2] = self.Mob1Liste[0]* self.Mob1Liste[0]*self.Mob1Liste[1]
        self.Mob1Liste[3] = self.Mob1Liste[2]
        self.Mob1Liste[4] = random.randint(1, self.Mob1Liste[0]) * self.Mob1Liste[0] + random.randint (0,5)
        self.Mob1Liste[5] = 0
        self.Mob1Liste[6] = random.randint(1, self.Mob1Liste[0]) * self.Mob1Liste[0] + random.randint (0,5)
        self.Mob1Liste[7] = random.randint(1, self.Mob1Liste[0]) * self.Mob1Liste[0] + random.randint (0,5)
        self.Mob1Liste[8] = random.randint(1, self.Mob1Liste[0]) * self.Mob1Liste[0] + random.randint (0,5)
        self.Mob1Liste[9] = random.randint(1, self.Mob1Liste[0]) * self.Mob1Liste[0] + random.randint (0,5)
        self.Mob1pos = vec2d(random.randint(1,28), random.randint(1, 28))
        while self.map [(self.Mob1pos[1]-1)* 28 + self.Mob1pos[0] - 1] <= 0 or self.map [(self.Mob1pos[1]-1)* 28 + self.Mob1pos[0] - 1] > 10: # or self.Mob1pos == 0:
            self.Mob1pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[(self.Mob1pos[1]-1)*28+self.Mob1pos[0] - 1] = 10 + self.Mob1Liste[1]

        self.Mob2Liste[0] = random.randint (1,8)
        self.Mob2Liste[1] = random.randint(1, 4)
        self.Mob2Liste[2] = self.Mob2Liste[0]* self.Mob2Liste[0]*self.Mob2Liste[1]
        self.Mob2Liste[3] = self.Mob2Liste[2]
        self.Mob2Liste[4] = random.randint(1, self.Mob2Liste[0]) * self.Mob2Liste[0] + random.randint (0,5)
        self.Mob2Liste[5] = 0
        self.Mob2Liste[6] = random.randint(1, self.Mob2Liste[0]) * self.Mob2Liste[0] + random.randint (0,5)
        self.Mob2Liste[7] = random.randint(1, self.Mob2Liste[0]) * self.Mob2Liste[0] + random.randint (0,5)
        self.Mob2Liste[8] = random.randint(1, self.Mob2Liste[0]) * self.Mob2Liste[0] + random.randint (0,5)
        self.Mob2Liste[9] = random.randint(1, self.Mob2Liste[0]) * self.Mob2Liste[0] + random.randint (0,5)
        self.Mob2pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        while self.map [(self.Mob2pos[1]-1) *28 + self.Mob2pos[0] - 1] <= 0 or self.map [(self.Mob2pos[1]-1) *28 + self.Mob2pos[0] - 1] > 10: # or self.Mob2pos == 0:
            self.Mob2pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        self.map[(self.Mob2pos[1]-1)*28 + self.Mob2pos[0] - 1] = 10 + self.Mob2Liste[1]

        self.Mob3Liste[0] = random.randint (1,8)
        self.Mob3Liste[1] = random.randint (1, 4)
        self.Mob3Liste[2] = self.Mob3Liste[0]* self.Mob3Liste[0]*self.Mob1Liste[1]
        self.Mob3Liste[3] = self.Mob3Liste[2]
        self.Mob3Liste[4] = random.randint(1, self.Mob3Liste[0]) * self.Mob3Liste[0] + random.randint (0,5)
        self.Mob3Liste[5] = 0
        self.Mob3Liste[6] = random.randint(1, self.Mob3Liste[0]) * self.Mob3Liste[0] + random.randint (0,5)
        self.Mob3Liste[7] = random.randint(1, self.Mob3Liste[0]) * self.Mob3Liste[0] + random.randint (0,5)
        self.Mob3Liste[8] = random.randint(1, self.Mob3Liste[0]) * self.Mob3Liste[0] + random.randint (0,5)
        self.Mob3Liste[9] = random.randint(1, self.Mob3Liste[0]) * self.Mob3Liste[0] + random.randint (0,5)
        self.Mob3pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        while self.map[(self.Mob3pos[1]-1) *28+ self.Mob3pos[0] - 1] <= 0 or self.map[(self.Mob3pos[1]-1) *28+ self.Mob3pos[0] - 1] > 10: # or self.Mob3pos == 0:
            self.Mob3pos = vec2d(random.randint(1, 28), random.randint(1, 28))
        self.map[(self.Mob3pos[1]-1)*28 + self.Mob3pos[0] - 1] = 10 + self.Mob3Liste[1]

        self.Mob4Liste[0] = random.randint (1,8)
        self.Mob4Liste[1] = random.randint(1, 4)
        self.Mob4Liste[2] = self.Mob4Liste[0]* self.Mob4Liste[0]*self.Mob4Liste[1]
        self.Mob4Liste[3] = self.Mob4Liste[2]
        self.Mob4Liste[4] = random.randint(1, self.Mob4Liste[0]) * self.Mob4Liste[0] + random.randint (0,5)
        self.Mob4Liste[5] = 0
        self.Mob4Liste[6] = random.randint(1, self.Mob4Liste[0]) * self.Mob4Liste[0] + random.randint (0,5)
        self.Mob4Liste[7] = random.randint(1, self.Mob4Liste[0]) * self.Mob4Liste[0] + random.randint (0,5)
        self.Mob4Liste[8] = random.randint(1, self.Mob4Liste[0]) * self.Mob4Liste[0] + random.randint (0,5)
        self.Mob4Liste[9] = random.randint(1, self.Mob4Liste[0]) * self.Mob4Liste[0] + random.randint (0,5)
        self.Mob4pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        while self.map [(self.Mob4pos[1]-1) *28+ self.Mob4pos[0] - 1] <= 0 or self.map [(self.Mob4pos[1]-1) *28+ self.Mob4pos[0] - 1] > 10: # or self.Mob4pos == 0:
            self.Mob4pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[(self.Mob4pos[1]-1)*28 + self.Mob4pos[0] - 1] = 10 + self.Mob4Liste[1]

        self.Mob5Liste[0] = random.randint (1,8)
        self.Mob5Liste[1] = random.randint(1, 4)
        self.Mob5Liste[2] = self.Mob5Liste[0]* self.Mob5Liste[0]*self.Mob5Liste[1]
        self.Mob5Liste[3] = self.Mob5Liste[2]
        self.Mob5Liste[4] = random.randint(1, self.Mob5Liste[0]) * self.Mob5Liste[0] + random.randint (0,5)
        self.Mob5Liste[5] = 0
        self.Mob5Liste[6] = random.randint(1, self.Mob5Liste[0]) * self.Mob5Liste[0] + random.randint (0,5)
        self.Mob5Liste[7] = random.randint(1, self.Mob5Liste[0]) * self.Mob5Liste[0] + random.randint (0,5)
        self.Mob5Liste[8] = random.randint(1, self.Mob5Liste[0]) * self.Mob5Liste[0] + random.randint (0,5)
        self.Mob5Liste[9] = random.randint(1, self.Mob5Liste[0]) * self.Mob5Liste[0] + random.randint (0,5)
        self.Mob5pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        while self.map [(self.Mob5pos[1]-1) *28+ self.Mob5pos[0] - 1] <= 0 or self.map [(self.Mob5pos[1]-1) *28+ self.Mob5pos[0] - 1] > 10: # or self.Mob4pos == 0:
            self.Mob5pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[(self.Mob5pos[1]-1)*28 + self.Mob5pos[0] - 1] = 10 + self.Mob5Liste[1]

        self.Mob6Liste[0] = random.randint (1,8)
        self.Mob6Liste[1] = random.randint(1, 4)
        self.Mob6Liste[2] = self.Mob6Liste[0]* self.Mob6Liste[0]*self.Mob6Liste[1]
        self.Mob6Liste[3] = self.Mob6Liste[2]
        self.Mob6Liste[4] = random.randint(1, self.Mob6Liste[0]) * self.Mob6Liste[0] + random.randint (0,5)
        self.Mob6Liste[5] = random.randint(1, self.Mob6Liste[0]) * self.Mob6Liste[0] + random.randint (0,5)
        self.Mob6Liste[6] = random.randint(1, self.Mob6Liste[0]) * self.Mob6Liste[0] + random.randint (0,5)
        self.Mob6Liste[7] = random.randint(1, self.Mob6Liste[0]) * self.Mob6Liste[0] + random.randint (0,5)
        self.Mob6pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        while self.map [(self.Mob6pos[1]-1) *28+ self.Mob6pos[0] - 1] <= 0 or self.map [(self.Mob6pos[1]-1) *28+ self.Mob6pos[0] - 1] <= 0 > 10: # or self.Mob4pos == 0:
            self.Mob6pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[(self.Mob6pos[1]-1)*28 + self.Mob6pos[0] - 1] = 10 + self.Mob6Liste[1]

        self.Mob7Liste[0] = random.randint (1,8)
        self.Mob7Liste[1] = random.randint(1, 4)
        self.Mob7Liste[2] = self.Mob7Liste[0]* self.Mob7Liste[0]*self.Mob7Liste[1]
        self.Mob7Liste[3] = self.Mob7Liste[2]
        self.Mob7Liste[4] = random.randint(1, self.Mob7Liste[0]) * self.Mob7Liste[0] + random.randint (0,5)
        self.Mob7Liste[5] = 0
        self.Mob7Liste[6] = random.randint(1, self.Mob7Liste[0]) * self.Mob7Liste[0] + random.randint (0,5)
        self.Mob7Liste[7] = random.randint(1, self.Mob7Liste[0]) * self.Mob7Liste[0] + random.randint (0,5)
        self.Mob7Liste[8] = random.randint(1, self.Mob7Liste[0]) * self.Mob7Liste[0] + random.randint (0,5)
        self.Mob7Liste[9] = random.randint(1, self.Mob7Liste[0]) * self.Mob7Liste[0] + random.randint (0,5)
        self.Mob7pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        while self.map [(self.Mob7pos[1]-1) *28+ self.Mob7pos[0] - 1] <= 0 or self.map [(self.Mob7pos[1]-1) *28+ self.Mob7pos[0] - 1] > 10: # or self.Mob4pos == 0:
            self.Mob7pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[(self.Mob7pos[1]-1)*28 + self.Mob7pos[0] - 1] = 10 + self.Mob7Liste[1]

        self.Mob8Liste[0] = random.randint (1,8)
        self.Mob8Liste[1] = random.randint(1, 4)
        self.Mob8Liste[2] = self.Mob8Liste[0]* self.Mob8Liste[0]*self.Mob8Liste[1]
        self.Mob8Liste[3] = self.Mob8Liste[2]
        self.Mob8Liste[4] = random.randint(1, self.Mob8Liste[0]) * self.Mob8Liste[0] + random.randint (0,5)
        self.Mob8Liste[5] = 0
        self.Mob8Liste[6] = random.randint(1, self.Mob8Liste[0]) * self.Mob8Liste[0] + random.randint (0,5)
        self.Mob8Liste[7] = random.randint(1, self.Mob8Liste[0]) * self.Mob8Liste[0] + random.randint (0,5)
        self.Mob8Liste[8] = random.randint(1, self.Mob8Liste[0]) * self.Mob8Liste[0] + random.randint (0,5)
        self.Mob8Liste[9] = random.randint(1, self.Mob8Liste[0]) * self.Mob8Liste[0] + random.randint (0,5)
        self.Mob8pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        while self.map [(self.Mob8pos[1]-1) *28+ self.Mob8pos[0] - 1] <= 0 or self.map [(self.Mob8pos[1]-1) *28+ self.Mob8pos[0] - 1] > 10: # or self.Mob4pos == 0:
            self.Mob8pos = vec2d(random.randint (1, 28), random.randint(1, 28))
        self.map[(self.Mob8pos[1]-1)*28 + self.Mob8pos[0] - 1] = 10 + self.Mob8Liste[1]
        print (self.Mob1pos)
        print (self.Mob2pos)
        print (self.Mob3pos)
        print (self.Mob4pos)
        print (self.Mob5pos)
        print (self.Mob6pos)
        print (self.Mob7pos)
        print (self.Mob8pos)
        print (self.Mob1Liste)
        print (self.Mob2Liste)
        print (self.Mob3Liste)
        print (self.Mob4Liste)
        print (self.Mob5Liste)
        print (self.Mob6Liste)
        print (self.Mob7Liste)
        print (self.Mob8Liste)

        print (self.map)

        self.MobimFocus = 0
        self.SpielerListe = [0] * 30
        self.SpielerListe[0] = 1
        self.SpielerListe[1] = 1
        self.SpielerListe[2] = "Hero"
        self.SpielerListe[3] = 0
        self.SpielerListe[4] = 10
        self.SpielerListe[5] = 10
        self.SpielerListe[6] = 5
        self.SpielerListe[7] = 5
        self.SpielerListe[8] = 5
        self.SpielerListe[9] = 5
        self.SpielerListe[10] = 5
        self.SpielerListe[11] = 5
        self.SpielerListe[12] = 10
        self.SpielerListe[13] = 10

        self.Spielerinventory1 = 15 * [0]
        self.Spielerinventory2 = 15 * [0]
        self.Spielerinventory3 = 15 * [0]
        self.Spielerinventory4 = 15 * [0]
        self.Spielerinventory5 = 15 * [0]
        self.Spielerinventory6 = 15 * [0]
        self.Spielerinventory7 = 15 * [0]
        self.Spielerinventory8 = 15 * [0]
        self.Spielerinventory9 = 15 * [0]
        self.Spielerinventory10 = 15 * [0]
        print ("Initialisierung abgeschlossen")

    def keyDown(self,key):
            print (self.SpielerVec)
            def Kampf (self,Richtung):
                if Richtung == 1:
                    if self.SpielerVec[0] // 20 == self.Mob1pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob1pos[1]: self.MobimFocus = 1
                    elif self.SpielerVec[0] // 20 == self.Mob2pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob2pos[1]: self.MobimFocus = 2
                    elif self.SpielerVec[0] // 20 == self.Mob3pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob3pos[1]: self.MobimFocus = 3
                    elif self.SpielerVec[0] // 20 == self.Mob4pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob4pos[1]: self.MobimFocus = 4
                    elif self.SpielerVec[0] // 20 == self.Mob5pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob5pos[1]: self.MobimFocus = 5
                    elif self.SpielerVec[0] // 20 == self.Mob6pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob6pos[1]: self.MobimFocus = 6
                    elif self.SpielerVec[0] // 20 == self.Mob7pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob7pos[1]: self.MobimFocus = 7
                    elif self.SpielerVec[0] // 20 == self.Mob8pos[0] and (self.SpielerVec[1]-1) // 20 == self.Mob8pos[1]: self.MobimFocus = 8
                elif Richtung == 2:
                    if (self.SpielerVec[0]+20) // 20 == self.Mob1pos[0] and self.SpielerVec[1] // 20 == self.Mob1pos[1]: self.MobimFocus = 1
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob2pos[0] and self.SpielerVec[1] // 20 == self.Mob2pos[1]: self.MobimFocus = 2
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob3pos[0] and self.SpielerVec[1] // 20 == self.Mob3pos[1]: self.MobimFocus = 3
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob4pos[0] and self.SpielerVec[1] // 20 == self.Mob4pos[1]: self.MobimFocus = 4
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob5pos[0] and self.SpielerVec[1] // 20 == self.Mob5pos[1]: self.MobimFocus = 5
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob6pos[0] and self.SpielerVec[1] // 20 == self.Mob6pos[1]: self.MobimFocus = 6
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob7pos[0] and self.SpielerVec[1] // 20 == self.Mob7pos[1]: self.MobimFocus = 7
                    elif (self.SpielerVec[0]+20) // 20 == self.Mob8pos[0] and self.SpielerVec[1] // 20 == self.Mob8pos[1]: self.MobimFocus = 8
                elif Richtung == 3:
                    if self.SpielerVec[0] // 20 == self.Mob1pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob1pos[1]: self.MobimFocus = 1
                    elif self.SpielerVec[0] // 20 == self.Mob2pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob2pos[1]: self.MobimFocus = 2
                    elif self.SpielerVec[0] // 20 == self.Mob3pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob3pos[1]: self.MobimFocus = 3
                    elif self.SpielerVec[0] // 20 == self.Mob4pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob4pos[1]: self.MobimFocus = 4
                    elif self.SpielerVec[0] // 20 == self.Mob5pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob5pos[1]: self.MobimFocus = 5
                    elif self.SpielerVec[0] // 20 == self.Mob6pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob6pos[1]: self.MobimFocus = 6
                    elif self.SpielerVec[0] // 20 == self.Mob7pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob7pos[1]: self.MobimFocus = 7
                    elif self.SpielerVec[0] // 20 == self.Mob8pos[0] and (self.SpielerVec[1]+20) // 20 == self.Mob8pos[1]: self.MobimFocus = 8
                elif Richtung == 4:
                    if (self.SpielerVec[0]-20) // 20 == self.Mob1pos[0] and self.SpielerVec[1] // 20 == self.Mob1pos[1]: self.MobimFocus = 1
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob2pos[0] and self.SpielerVec[1] // 20 == self.Mob2pos[1]: self.MobimFocus = 2
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob3pos[0] and self.SpielerVec[1] // 20 == self.Mob3pos[1]: self.MobimFocus = 3
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob4pos[0] and self.SpielerVec[1] // 20 == self.Mob4pos[1]: self.MobimFocus = 4
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob5pos[0] and self.SpielerVec[1] // 20 == self.Mob5pos[1]: self.MobimFocus = 5
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob6pos[0] and self.SpielerVec[1] // 20 == self.Mob6pos[1]: self.MobimFocus = 6
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob7pos[0] and self.SpielerVec[1] // 20 == self.Mob7pos[1]: self.MobimFocus = 7
                    elif (self.SpielerVec[0]-20) // 20 == self.Mob8pos[0] and self.SpielerVec[1] // 20 == self.Mob8pos[1]: self.MobimFocus = 8
                print (self.MobimFocus)
                print ("Kampf")
                if self.MobimFocus == 1:
                    if self.Mob1Liste[4] > self.SpielerListe[6]:
                        pass

            if key == K_w and self.map[(self.SpielerVec[1]//20-2)*28 + self.SpielerVec[0]//20-1] > 0 and self.SpielerVec [1] != 20:
                if self.map[(self.SpielerVec[1]//20-2)*28 + self.SpielerVec[0]//20-1] > 10:
                    Kampf (self,1)
                else:
                    self.SpielerVec +=  (0,-20)
            elif key == K_a and self.map[(self.SpielerVec[1]//20-1)*28 + self.SpielerVec[0]//20-2] > 0 and self.SpielerVec [0] != 20:
                if self.map[(self.SpielerVec[1]//20-1)*28 + self.SpielerVec[0]//20-2] > 10:
                    Kampf (self,4)
                else:
                    self.SpielerVec += (-20,0)
            elif key == K_s and self.map[(self.SpielerVec[1]//20)*28 + self.SpielerVec[0]//20-1] > 0 and self.SpielerVec [1] != 560:
                if self.map[(self.SpielerVec[1]//20)*28 + self.SpielerVec[0]//20-1] > 10:
                    Kampf (self,3)
                else:
                    self.SpielerVec += (0,20)
            elif key == K_d and self.map[(self.SpielerVec[1]//20-1)*28 + self.SpielerVec[0]//20] > 0 and self.SpielerVec [0] != 560:
                if self.map[(self.SpielerVec[1]//20-1)*28 + self.SpielerVec[0]//20] > 10:
                    Kampf (self,2)
                else:
                    self.SpielerVec += (20,0)
    def update(self):
        self.SpielerListe[4] = 10 + self.Spielerinventory1[5] + self.Spielerinventory2[5] + self.Spielerinventory3[5] + self.Spielerinventory4[5] + self.Spielerinventory5[5] + self.Spielerinventory6[5] + self.Spielerinventory7[5] + self.Spielerinventory8[5] + self.Spielerinventory9[5] + self.Spielerinventory10[5]
        self.SpielerListe[6] = 5 + self.Spielerinventory1[7] + self.Spielerinventory2[7] + self.Spielerinventory3[7] + self.Spielerinventory4[7] + self.Spielerinventory5[7] + self.Spielerinventory6[7] + self.Spielerinventory7[7] + self.Spielerinventory8[7] + self.Spielerinventory9[7] + self.Spielerinventory10[7]
        self.SpielerListe[7] = 5 + self.Spielerinventory1[8] + self.Spielerinventory2[8] + self.Spielerinventory3[8] + self.Spielerinventory4[8] + self.Spielerinventory5[8] + self.Spielerinventory6[8] + self.Spielerinventory7[8] + self.Spielerinventory8[8] + self.Spielerinventory9[8] + self.Spielerinventory10[8]
        self.SpielerListe[8] = 5 + self.Spielerinventory1[9] + self.Spielerinventory2[9] + self.Spielerinventory3[9] + self.Spielerinventory4[9] + self.Spielerinventory5[9] + self.Spielerinventory6[9] + self.Spielerinventory7[9] + self.Spielerinventory8[9] + self.Spielerinventory9[9] + self.Spielerinventory10[9]
        self.SpielerListe[9] = 5 + self.Spielerinventory1[10] + self.Spielerinventory2[10] + self.Spielerinventory3[10] + self.Spielerinventory4[10] + self.Spielerinventory5[10] + self.Spielerinventory6[10] + self.Spielerinventory7[10] + self.Spielerinventory8[10] + self.Spielerinventory9[10] + self.Spielerinventory10[10]
        self.SpielerListe[10] = 5 + self.Spielerinventory1[11] + self.Spielerinventory2[11] + self.Spielerinventory3[11] + self.Spielerinventory4[11] + self.Spielerinventory5[11] + self.Spielerinventory6[11] + self.Spielerinventory7[11] + self.Spielerinventory8[11] + self.Spielerinventory9[11] + self.Spielerinventory10[11]
        self.SpielerListe[11] = 5 + self.Spielerinventory1[12] + self.Spielerinventory2[12] + self.Spielerinventory3[12] + self.Spielerinventory4[12] + self.Spielerinventory5[12] + self.Spielerinventory6[12] + self.Spielerinventory7[12] + self.Spielerinventory8[12] + self.Spielerinventory9[12] + self.Spielerinventory10[12]
        self.SpielerListe[12] = 10 + self.Spielerinventory1[13] + self.Spielerinventory2[13] + self.Spielerinventory3[13] + self.Spielerinventory4[13] + self.Spielerinventory5[13] + self.Spielerinventory6[13] + self.Spielerinventory7[13] + self.Spielerinventory8[13] + self.Spielerinventory9[13] + self.Spielerinventory10[13]
        if self.SpielerListe[5] > self.SpielerListe[4]:
            self.SpielerListe[5] = self.SpielerListe[4]
        if self.SpielerListe[13] > self.SpielerListe[12]:
            self.SpielerListe[13] = self.SpielerListe[12]
    def mouseUp(self, button, pos):
        self.target = vec2d( pos)
        if self.target[0] >= self.Mob1pos[0] and self.target[0] <= self.Mob1pos[0] +20 and self.target[1] >= self.Mob1pos[1] and self.target[1] <= self.Mob1pos[1] +20:
            print ("MOb1")



    def mouseMotion(self, buttons, pos, rel):
        pass

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
            for temp4 in range (0,28):
                if self.map[temp3*28+temp4] == 0:
                    self.screen.blit(self.img3, (temp4* 20+20,temp3*20+20))
        self.screen.blit(self.img1, (self.SpielerVec))
        if self.Mob1Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob1pos*20))
        elif self.Mob1Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob1pos*20))
        elif self.Mob1Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob1pos*20))
        elif self.Mob1Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob1pos*20))
        if self.Mob2Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob2pos*20))
        elif self.Mob2Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob2pos*20))
        elif self.Mob2Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob2pos*20))
        elif self.Mob2Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob2pos*20))
        if self.Mob3Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob3pos*20))
        elif self.Mob3Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob3pos*20))
        elif self.Mob3Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob3pos*20))
        elif self.Mob3Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob3pos*20))
        if self.Mob4Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob4pos*20))
        elif self.Mob4Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob4pos*20))
        elif self.Mob4Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob4pos*20))
        elif self.Mob4Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob4pos*20))
        if self.Mob5Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob5pos*20))
        elif self.Mob5Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob5pos*20))
        elif self.Mob5Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob5pos*20))
        elif self.Mob5Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob5pos*20))
        if self.Mob6Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob6pos*20))
        elif self.Mob6Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob6pos*20))
        elif self.Mob6Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob6pos*20))
        elif self.Mob6Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob6pos*20))
        if self.Mob7Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob7pos*20))
        elif self.Mob7Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob7pos*20))
        elif self.Mob7Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob7pos*20))
        elif self.Mob7Liste[1] == 4:
            self.screen.blit(self.imgGolem, (self.Mob7pos*20))
        if self.Mob8Liste[1] == 1:
            self.screen.blit(self.imgVampire, (self.Mob8pos*20))
        elif self.Mob8Liste[1] == 2:
            self.screen.blit(self.imgGoblin, (self.Mob8pos*20))
        elif self.Mob8Liste[1] == 3:
            self.screen.blit(self.imgDragon, (self.Mob8pos*20))
        elif self.Mob8Liste[1] == 4:
            self.screen.blit(self.imgDragon, (self.Mob8pos*20))

        if self.MobimFocus == 1:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob1Liste[2] / self.Mob1Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob1Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob1Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 2:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob2Liste[2] / self.Mob2Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob2Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob2Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 3:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob3Liste[2] / self.Mob3Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob3Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob3Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 4:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob4Liste[2] / self.Mob4Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob4Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob4Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 5:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob5Liste[2] / self.Mob5Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob5Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob5Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 6:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob6Liste[2] / self.Mob6Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob6Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob6Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 7:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob7Liste[2] / self.Mob7Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob7Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob7Liste[9])), 1, (255, 0, 0)), (750, 350))
        elif self.MobimFocus == 8:
            pygame.draw.rect(self.screen, self.red, [610, 407, self.Mob8Liste[2] / self.Mob8Liste[3]*140, 30])
            self.screen.blit(self.Leveldesign.render(str(int(self.Mob8Liste[0])), 1, (0, 0, 0)), (765, 400))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[3])), 1, (0, 0, 0)), (710, 440))
            self.screen.blit(self.myfont.render("\\\\", 1, (0, 0, 0)), (660, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[2])), 1, (0, 0, 0)), (610, 440))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[4])), 1, (255, 0, 0)), (610, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[5])), 1, (255, 0, 0)), (680, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[6])), 1, (255, 0, 0)), (750, 260))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[7])), 1, (255, 0, 0)), (610, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob8Liste[8])), 1, (255, 0, 0)), (680, 350))
            self.screen.blit(self.myfont.render(str(int(self.Mob82Liste[9])), 1, (255, 0, 0)), (750, 350))

        pygame.draw.rect(self.screen, self.red, [610, 45, self.SpielerListe[5] / self.SpielerListe[4]*140, 30])
        pygame.draw.rect(self.screen, self.blue, [610, 30, self.SpielerListe[13] / self.SpielerListe[12]*140, 15])
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[5])) + "  \\\\", 1, (0, 0, 0)), (610, 75))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[12])), 1, (0, 0, 0)), (715, 10))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[13])) + "  \\\\", 1, (0, 0, 0)), (610, 10))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[4])), 1, (0, 0, 0)), (715, 75))
        self.screen.blit(self.Leveldesign.render(str(int(self.SpielerListe[0])), 1, (0, 0, 0)), (765, 30))

        self.screen.blit(self.ItemSlots, (610,110))
        self.screen.blit(self.Attackimg2, (610,200))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[6])), 1, (0, 0, 0)), (610, 240))
        self.screen.blit(self.Magicimg, (680,200))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[10])), 1, (0, 0, 0)), (680, 240))
        self.screen.blit(self.Staerkeimg, (750,200))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[7])), 1, (0, 0, 0)), (750, 240))
        self.screen.blit(self.Geschicklichkeitimg, (610,290))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[8])), 1, (0, 0, 0)), (610, 330))
        self.screen.blit(self.Verteidigungimg, (680,290))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[11])), 1, (0, 0, 0)), (680, 330))
        self.screen.blit(self.Ausdauerimg, (750,290))
        self.screen.blit(self.myfont.render(str(int(self.SpielerListe[9])), 1, (0, 0, 0)), (750, 330))

        pygame.draw.rect(self.screen, self.red, [610, 560, 180, 30])
        self.screen.blit(self.myfont.render("Beenden", 1, (0, 0, 0)), (630, 560))

        pygame.display.flip()




s = Starter()
s.mainLoop(120)

