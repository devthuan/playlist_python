import pygame
import random


pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("test")
running = True
GREEN = (23, 168, 60)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE =(255, 255, 255)
BLACK =  (0, 0, 0)
clock = pygame.time.Clock()
background = GREEN
text = str("hello word!")
font = pygame.font.SysFont('sans', 30)
text = font.render(text, True, BLACK)
text_box = text.get_rect()
text_pos = (50,50)



while running:
    clock.tick(60) # HZ
    screen.fill(background)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # or
    # mouse = pygame.mouse.get_pos()
    # mouse_x = mouse[0]
    # mouse_y = mouse[1]
    # print(mouse_x , mouse_y)

    pygame.draw.rect(screen, RED, (text_pos[0], text_pos[1], text_box[2], text_box[3]))    
    screen.blit(text, text_pos)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (50 < mouse_x) and (mouse_x < 200) and (mouse_y > 50) and (mouse_y < 200): 
                    background = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()