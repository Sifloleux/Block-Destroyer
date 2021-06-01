import time
import pygame
from pygame.locals import *
import random
import os.path
import math

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 710
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60
SHOOTING_SPEED = 16
SPEED = [0, 0]
BLOCK_MOVEMENT = SCREEN_WIDTH/10

starting_point = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
draw_line = 0
x = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
y=[float('nan'),float('nan')]
mouse_draging = False
shoot = 0
num_of_balls = 1
block_update_time = 0
shot_already = 0
difficulty = 1


def loadImage(name, useColorKey=False):
    fullname = os.path.join("data",name)
    image = pygame.image.load(fullname)  
    image = image.convert() 
    if useColorKey is True:
        colorkey = image.get_at((0,0)) 
        image.set_colorkey(colorkey,RLEACCEL) 
    return image

def get_speed(starting_point,pointer_point):
    hypotenuse = math.sqrt((abs(pointer_point[1]-starting_point[1]))**2 + \
                           (abs(pointer_point[0]-starting_point[0]))**2)
        
    if starting_point[0] > pointer_point[0]:
        speed = [(pointer_point[0]-starting_point[0])/hypotenuse \
                 ,-(starting_point[1]-pointer_point[1])/hypotenuse]
            
    elif starting_point[0] < pointer_point[0]:
         speed = [(pointer_point[0]-starting_point[0])/hypotenuse \
                 ,-(starting_point[1]-pointer_point[1])/hypotenuse]     
    else:
        speed=[0,1]
    return speed


def add_ball(mouse_position, SHOOTING_SPEED,starting_point):
    speed = get_speed(starting_point,mouse_position)
    ball1 = Ball(RED,20,20,[SHOOTING_SPEED*speed[0],SHOOTING_SPEED*speed[1]])
    ball1.rect.x = starting_point[0] - 10
    ball1.rect.y = starting_point[1] - 10
    all_balls_list.add(ball1)
    all_balls_list.draw(screen)
    pygame.display.flip()




def add_block_line(SCREEN_WIDTH,difficulty):
        if difficulty <= 5:
            print(difficulty)
            samples = random.sample(range(10),3)
            for i in samples:   
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                all_blocks_list.add(block)
        elif difficulty <= 15 and difficulty > 5 :
            print(difficulty)
            samples = random.sample(range(10),4)
            for i in samples:       
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                all_blocks_list.add(block)
        elif difficulty <= 25 and difficulty > 15 :
            print(difficulty)
            samples = random.sample(range(10),6)
            for i in samples: 
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                all_blocks_list.add(block)
        else:
            samples = random.sample(range(10),8)
            for i in samples: 
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                all_blocks_list.add(block)
    
#------------------------------------CLASSES----------------------------------  
    
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
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.kill()

class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height,hp):
        super().__init__()
        self.hp = hp
        self.font = pygame.font.SysFont('Arial', 25)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        if hp <= 5:
            pygame.draw.rect(self.image, (11, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])                 
        elif hp <= 10:
            pygame.draw.rect(self.image, (115, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 15:
            pygame.draw.rect(self.image, (206, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 20:
            pygame.draw.rect(self.image, (252, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 25:
            pygame.draw.rect(self.image, (252, 211, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 30:
            pygame.draw.rect(self.image, (252, 152, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 35:
            pygame.draw.rect(self.image, (252, 115, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 40:
            pygame.draw.rect(self.image, (252, 86, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 45:
            pygame.draw.rect(self.image, (252, 61, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 50:
            pygame.draw.rect(self.image, (252, 3, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 55:
            pygame.draw.rect(self.image, (163, 5, 5), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 60:
            pygame.draw.rect(self.image, (127, 2, 2), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 65:
            pygame.draw.rect(self.image, (103, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 70:
            pygame.draw.rect(self.image, (83, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp > 70:
            pygame.draw.rect(self.image, (73, 1, 1), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])

        self.rect = self.image.get_rect()
        #self.rect.bottom.
    
    def addText(self,screen,hp,x,y):
        if hp >50:
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(f'{hp}', True, WHITE) 
            screen.blit(text,(x , y))
        else:
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(f'{hp}', True, BLACK) 
            screen.blit(text,(x , y))
    
    def update(self):
        self.rect.y += BLOCK_MOVEMENT
        if self.hp <=0:
             self.kill()
             
    def update_color_num(self,hp):
        if hp <= 5:
            pygame.draw.rect(self.image, (11, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 10:
            pygame.draw.rect(self.image, (115, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 15:
            pygame.draw.rect(self.image, (206, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 20:
            pygame.draw.rect(self.image, (252, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 25:
            pygame.draw.rect(self.image, (252, 211, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 30:
            pygame.draw.rect(self.image, (252, 152, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 35:
            pygame.draw.rect(self.image, (252, 115, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 40:
            pygame.draw.rect(self.image, (252, 86, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 45:
            pygame.draw.rect(self.image, (252, 61, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 50:
            pygame.draw.rect(self.image, (252, 3, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 55:
            pygame.draw.rect(self.image, (163, 5, 5), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 60:
            pygame.draw.rect(self.image, (127, 2, 2), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 65:
            pygame.draw.rect(self.image, (103, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 70:
            pygame.draw.rect(self.image, (83, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp > 70:
            pygame.draw.rect(self.image, (73, 1, 1), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
            
 
  


          
class Line(pygame.sprite.Sprite):
     def __init__(self, color, width, height,hp):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height],3)        
        self.rect = self.image.get_rect()
        #self.rect.bottom.
    
     def update(self):
         self.rect.y += BLOCK_MOVEMENT
         if self.hp <=0:
             self.kill()
             
             
             
             
#----------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mouse_draging = False
all_balls_list = pygame.sprite.Group()
all_blocks_list = pygame.sprite.Group()
all_vertical_list = pygame.sprite.Group()
all_horizontal_list = pygame.sprite.Group()



carryOn = True
#-----starting blocks

row_1 = random.sample(range(10),4)
row_2 = random.sample(range(10),4)
row_3 = random.sample(range(10),4)
for i in row_1: 
    block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,1)
    block.rect.x = (SCREEN_WIDTH/10) * i
    block.rect.y = (SCREEN_WIDTH/10)
    all_blocks_list.add(block)

for i in row_2: 
    block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,1)
    block.rect.x = (SCREEN_WIDTH/10) * i
    block.rect.y = (SCREEN_WIDTH/10) * 2
    all_blocks_list.add(block)

for i in row_3: 
    block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,1)
    block.rect.x = (SCREEN_WIDTH/10) * i
    block.rect.y = (SCREEN_WIDTH/10) * 3
    all_blocks_list.add(block)
    
all_blocks_list.add(block)

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
                    add_ball([mouse_x, mouse_y],SHOOTING_SPEED,starting_point)
                shoot= 0 
                shot_already = 1
                difficulty += 1
                        
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

                                   
        elif event.type == pygame.MOUSEMOTION:
            if mouse_draging:
                mouse_x, mouse_y = event.pos
                y[0] = mouse_x
                y[1] = mouse_y
                draw_line = 1
                
        if shot_already == 1 and not all_balls_list:
            all_blocks_list.update()
            all_horizontal_list.update()
            all_vertical_list.update()
            add_block_line(SCREEN_WIDTH,difficulty)
            shot_already = 0           
            
            
    all_balls_list.update()
    
    
    
    
    
    
    
    
    if not all_balls_list and block_update_time ==1: 
        all_blocks_list.update()
        all_horizontal_list.update()
        all_vertical_list.update()
    
 
    
 
    
 
 
    

    for obj in all_balls_list:
        if obj.rect.x>=SCREEN_WIDTH:
            obj.velocity[0] = -obj.velocity[0]
        if obj.rect.x<=0:
            obj.velocity[0] = -obj.velocity[0]
        if obj.rect.y>SCREEN_HEIGHT:
            obj.velocity[1] = -obj.velocity[1]
        if obj.rect.y<0:
            obj.velocity[1] = -obj.velocity[1] 

    
    for hit in pygame.sprite.groupcollide(all_balls_list,all_blocks_list,0,0):
        hit.velocity[0] = - hit.velocity[0]
        hit.velocity[1] = - hit.velocity[1]
        
    for hit in pygame.sprite.groupcollide(all_blocks_list,all_balls_list,0,0):
        hit.hp = hit.hp -1
        if hit.hp <=0:
            hit.kill()
        hit.update_color_num(hit.hp)
            
    screen.fill(BLACK)
    all_balls_list.draw(screen) 
    all_blocks_list.draw(screen)
    
    for i in all_blocks_list:
        i.addText(screen,i.hp,i.rect.left+27 ,i.rect.top+25)
    pygame.draw.rect(screen, RED, [x[0]-10,x[1]-10,17,17])
    #if not all_balls_list:
    #if not all_blocks_list:
        
        


    if draw_line == 1:
        pygame.draw.line(screen, (200,200,200), starting_point,[mouse_x, mouse_y])
    pygame.draw.line(screen,WHITE,[0,655],[SCREEN_WIDTH,655],2)
    pygame.display.flip()

    clock.tick(60)
 

pygame.quit()