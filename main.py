import pygame
from player import Player

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Volta\'s Fighters')

player1 = Player(150, 80)

running = True

clock = pygame.time.Clock()
FPS = 60

def draw_bg():
    screen.fill((0, 0, 0))

while running: 
    clock.tick(FPS)

    draw_bg()

    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT - SCREEN_HEIGHT // 8)
    player1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()