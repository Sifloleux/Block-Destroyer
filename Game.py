
import pygame
from pygame.locals import *
import random
import os.path

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 710
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
FPS = 60
SPEED = [0, 0]
x = [315,650]
y=[float('nan'),float('nan')]

def loadImage(name, useColorKey=False):
    fullname = os.path.join("data",name)
    image = pygame.image.load(fullname)  
    image = image.convert() 
    if useColorKey is True:
        colorkey = image.get_at((0,0)) 
        image.set_colorkey(colorkey,RLEACCEL) 
    return image

def get_speed(starting_point,pointer_point):
    if starting_point[0] > pointer_point[0]:
        speed = [-(pointer_point[0]-starting_point[0])/(starting_point[0]-pointer_point[0]) \
                 ,(starting_point[0]-pointer_point[0])/(pointer_point[0]-starting_point[0])]
    elif starting_point[0] < pointer_point[0]:
         speed = [(pointer_point[0]-starting_point[0])/(starting_point[0]-pointer_point[0]) \
                 ,(starting_point[0]-pointer_point[0])/(pointer_point[0]-starting_point[0])]   
    else:
        speed = [0,1]
    return speed

class Balls(pygame.sprite.Sprite):

    def __init__(self,startpos):
        #inicjalizuj klasę bazową Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("ball.png",True)
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.speed = SPEED

    def update(self):
        if self.rect.bottom <= SCREEN_HEIGHT:
            self.kill()


#----------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

mouse_draging = False

clock = pygame.time.Clock()

running = True
shoot=0


draw_line=0

Balls_container = pygame.sprite.RenderClear()

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                mouse_draging = True
                mouse_x, mouse_y = event.pos             
                draw_line = 1
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                mouse_draging = False
                y[0] = y[0]
                y[1] = y[1]
                draw_line = 0
                if  shoot !=1:
                    shoot = 1
                                
        elif event.type == pygame.MOUSEMOTION:
            if mouse_draging:
                mouse_x, mouse_y = event.pos
                y[0] = mouse_x
                y[1] = mouse_y
                draw_line = 1
        else:
            draw_line = 0
            
            
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [x[0],x[1]],5)
   # if shoot ==1:
    #    draw
    if draw_line == 1:
        pygame.draw.line(screen, 'black', x, y, 2)
    pygame.draw.line(screen,'black',[0,655],[SCREEN_WIDTH,655])
    pygame.display.flip()



    clock.tick(FPS)


pygame.quit()
