import time
import pygame
from pygame.locals import *
import random
import os.path
import math

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 710
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60
SHOOTING_SPEED = 6
SPEED = [0, 0]
starting_point = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
draw_line = 0
x = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
y=[float('nan'),float('nan')]
mouse_draging = False
shoot = 0
num_of_balls = 1
def loadImage(name, useColorKey=False):
    fullname = os.path.join("data",name)
    image = pygame.image.load(fullname)  
    image = image.convert() 
    if useColorKey is True:
        colorkey = image.get_at((0,0)) 
        image.set_colorkey(colorkey,RLEACCEL) 
    return image

def get_speed(starting_point,pointer_point):
    hypotenuse = math.sqrt((abs(pointer_point[1]-starting_point[1]))**2+(abs(pointer_point[0]-starting_point[0]))**2)
    if starting_point[0] > pointer_point[0]:
        speed = [(pointer_point[0]-starting_point[0])/hypotenuse \
                 ,-(starting_point[1]-pointer_point[1])/hypotenuse]
        print(speed)
    elif starting_point[0] < pointer_point[0]:
         speed = [(pointer_point[0]-starting_point[0])/hypotenuse \
                 ,-(starting_point[1]-pointer_point[1])/hypotenuse]  
         print(speed)
    return speed


def add_ball(mouse_position, SHOOTING_SPEED,starting_point):
    speed = get_speed(starting_point,mouse_position)
    ball1 = Ball(RED,20,20,[SHOOTING_SPEED*speed[0],SHOOTING_SPEED*speed[1]])
    ball1.rect.x = starting_point[0] - 10
    ball1.rect.y = starting_point[1] - 10
    all_sprites_list.add(ball1)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    
class Ball(pygame.sprite.Sprite):

    
    def __init__(self, color, width, height,velocity):
        super().__init__()
        self.velocity = velocity
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.bottom >= SCREEN_HEIGHT - 55:
            self.kill()

#----------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

mouse_draging = False

all_sprites_list = pygame.sprite.Group()
 
carryOn = True
 

clock = pygame.time.Clock()
 

while carryOn:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     carryOn=False

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and shoot ==1:
                mouse_x, mouse_y = event.pos 
                mouse_draging = False
                y[0] = y[0]
                y[1] = y[1]
                draw_line = 0
                for i in range(num_of_balls):
                    print(mouse_x, mouse_y)
                    add_ball([mouse_x, mouse_y],SHOOTING_SPEED,starting_point)
                shoot= 0 
                
                        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                mouse_draging = False
                y[0] = y[0]
                y[1] = y[1]
                draw_line = 0 
                shoot = 0
                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_draging = True
            mouse_x, mouse_y = event.pos             
            draw_line = 1
            shoot = 1
            all_sprites_list.draw(screen)  
            pygame.display.flip()
                                   
        elif event.type == pygame.MOUSEMOTION:
            if mouse_draging:
                mouse_x, mouse_y = event.pos
                y[0] = mouse_x
                y[1] = mouse_y
                draw_line = 1
 

    all_sprites_list.update()
 

    for obj in all_sprites_list:
        if obj.rect.x>=SCREEN_WIDTH:
            obj.velocity[0] = -obj.velocity[0]
        if obj.rect.x<=0:
            obj.velocity[0] = -obj.velocity[0]
        if obj.rect.y>SCREEN_HEIGHT:
            obj.velocity[1] = -obj.velocity[1]
        if obj.rect.y<0:
            obj.velocity[1] = -obj.velocity[1] 
 
    screen.fill(BLACK)
    

    all_sprites_list.draw(screen) 
    pygame.draw.circle(screen, RED, [x[0],x[1]],5)

    if draw_line == 1:
        pygame.draw.line(screen, 'blue', starting_point,[mouse_x, mouse_y] , 2)
    pygame.draw.line(screen,WHITE,[0,655],[SCREEN_WIDTH,655],2)
    pygame.display.flip()

    clock.tick(60)
 

pygame.quit()