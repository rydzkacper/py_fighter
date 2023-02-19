import pygame
from fighter import Fighter
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PY FIGHTER")

# background image
bg_image = pygame.image.load("assets/images/backgrounds/background.jpeg")

def draw_bg():
    scale_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0,0))

# instances of fighters

# game loop
run = True
while run:
    #background
    draw_bg()
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
pygame.quit()
