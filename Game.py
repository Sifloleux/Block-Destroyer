import pygame

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 710
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

mouse_draging = False

clock = pygame.time.Clock()

running = True

x = [315,700]
y=[float('nan'),float('nan')]
draw_line=0

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
        elif event.type == pygame.MOUSEMOTION:
            if mouse_draging:
                mouse_x, mouse_y = event.pos
                y[0] = mouse_x
                y[1] = mouse_y

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [x[0],x[1]],4)
    if draw_line == 1:
        pygame.draw.line(screen, 'black', x, y, 2)
    pygame.display.flip()



    clock.tick(FPS)


pygame.quit()
