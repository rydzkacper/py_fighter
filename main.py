import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PY FIGHTER")
# framerate
clock = pygame.time.Clock()
FPS = 60

# colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# background image
bg_image = pygame.image.load("assets/images/backgrounds/background.jpeg")

warrior_sheet = pygame.image.load("assets/images/warrior/sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/sprites/wizard.png").convert_alpha()

# steps of each animation

warrior_animation_steps = [10, 8, 1, 7, 7, 3, 7]
wizard_animation_steps = [8, 8, 1, 8, 8, 3, 7]


def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))


# health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# instances of fighters
fighter_1 = Fighter(200, 310, warrior_sheet, warrior_animation_steps)
fighter_2 = Fighter(700, 310, wizard_sheet, wizard_animation_steps)
# game loop
run = True
while run:
    clock.tick(FPS)
    # background
    draw_bg()
    # show players health
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    # fighters move
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    # fighters draw
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update display
    pygame.display.update()
pygame.quit()
