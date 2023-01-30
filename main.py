import pygame
from player import Player

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

CHARACTER_WIDTH = 150
CHARACTER_HEIGHT = 80

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Volta\'s Fighters')

player1 = Player(CHARACTER_WIDTH, SCREEN_HEIGHT - 50 + CHARACTER_HEIGHT, CHARACTER_WIDTH, CHARACTER_HEIGHT)

running = True

clock = pygame.time.Clock()
FPS = 60

def draw_bg():
    screen.fill((0, 0, 0))

while running: 
    clock.tick(FPS)

    draw_bg()

    # Let the player jump until they reach the top of the screen.
    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    player1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()