import pygame
from fighter import Fighter
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PY FIGHTER")
#framerate
clock = pygame.time.Clock()
FPS = 60
# background image
bg_image = pygame.image.load("assets/images/backgrounds/background.jpeg")

def draw_bg():
    scale_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0,0))

# instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)
# game loop
run = True
while run:
    clock.tick(FPS)
    #background
    draw_bg()
    #fighters move
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    #fighters draw
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
pygame.quit()
