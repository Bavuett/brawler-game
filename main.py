import pygame

from Fighter import Fighter

pygame.init()

#window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#fighter variables
SCALE = 2
OFFSET_LAROCCA = [48, 40]
LAROCCA_SIZE_WIDTH = 65
LAROCCA_SIZE_HEIGHT = 110
LAROCCA_DATA = [LAROCCA_SIZE_WIDTH, LAROCCA_SIZE_HEIGHT, SCALE, OFFSET_LAROCCA]
OFFSET_MICALONE = [48, 40]
MICALONE_SIZE_WIDTH = 65
MICALONE_SIZE_HEIGHT = 110
MICALONE_DATA = [MICALONE_SIZE_WIDTH, MICALONE_SIZE_HEIGHT, SCALE, OFFSET_MICALONE]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Volta\'s Fighters')

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#background
bg = pygame.image.load('content/background/background.png')

#load sprite
larocca_sheet = pygame.image.load("content/sprites/LaRocca/larocca.png").convert_alpha()
micalone_sheet = pygame.image.load("content/sprites/Micalone/micalone.png").convert_alpha()
#find number of sprites in each animation
larocca_animation_count = [1,4,4,3]
micalone_animation_count = [1,4,4,3]


#draw health bar
def draw_health_bar(health, x, y):
    ratio = health/100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400*ratio, 30))
   


#drawing background
def draw_bg():
    screen.blit(bg, (0, 0))
    scaled_bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#fighter
fighter_1 = Fighter(200, 310,LAROCCA_DATA, larocca_sheet, larocca_animation_count)
fighter_2 = Fighter(700, 310, MICALONE_DATA, micalone_sheet, micalone_animation_count)

#loop
run = True
while run:

    clock.tick(FPS)

    draw_bg()

    #health bar
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #drawing fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #movement
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()


#exit
pygame.quit()