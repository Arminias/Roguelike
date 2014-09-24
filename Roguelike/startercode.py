from pygame import *
import math
from pygamehelper import *
from vec2d import *


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=(255, 255, 255))


        self.pos = vec2d(400,300)
        self.target = vec2d(300,300)


        self.img = pygame.image.load("tilesets/derek/HeroBase.png")
        #self.screen.blit(img, (-2, -2))

        self.drawcolor = (0, 0, 0)
        self.x =  0

    def update(self):
        dir = self.target - self.pos        #Direction
        if dir.length>3:
            dir.length = 3
        self.pos = self.pos + dir





    def keyUp(self, key):

        pass

    def mouseUp(self, button, pos):
        #pygame.draw.circle(self.screen, (0, 0, 0), pos, 20)
        #pygame.draw.circle(self.screen, (0, 0, 0), (pos[0], pos[1] + 20) , 20)
        self.target = vec2d( pos)



        #pass

    def mouseMotion(self, buttons, pos, rel):
        pass
       # if pos[1] >= 25 or pos[0] >= 25:
       # print (buttons, self, pos, rel)
       #  if buttons[0] == 1:
            #pygame.draw.circle(self.screen, (0, 0, 0), pos, 20)
        #    pygame.draw.line(self.screen, self.drawcolor, pos, (pos[0] - rel[0],pos[1] - rel[1]), 5)
       # else:
       #     if pos[0]<20:
      #          if buttons[0] == 1:
       #             self.drawcolor = self.screen.get_at(pos)
       #             pygame.draw.circle(self.screen, self.drawcolor, (200,100), 30)

       # if buttons[2] == 1:
            #RAINBOW MODE (Rechte Maustaste)
       #     color = self.screen.get_at((self.x, 0))
        #    pygame.draw.line(self.screen, color, pos, (pos[0] - rel[0],pos[1] - rel[1]), 5)

   #         self.x += 1
 #           if self.x >= 21:
  #              self.x = 0







#pygame.draw.line(self.screen, (0,0,0), (pos[0] + 20, pos[1] + 20), (pos[0] - rel[0] + 20,pos[1] - rel[1] + 20), 5)


     #   if buttons[1]==1:
      #      pygame.draw.circle(self.screen, (255,255,255),pos, 25)

    def quit (self, key):
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw(self):
        #pass
       # self.screen.fill((255, 255, 255))
       # pygame.draw.circle(self.screen, (255,0,0), self.target, 30, 1)
        self.screen.blit(self.img, self.target)

       # pygame.draw.circle(self.screen, (0,0,0), self.pos.inttup(), 21, 2)

      #  pygame.draw.circle(self.screen, (200,200,255), self.pos.inttup(), 20)


        #pygame.draw.circle(self.screen, (0, 0, 0), (50, 100), 20)


s = Starter()
s.mainLoop(60)
