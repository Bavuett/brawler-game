import pygame
from Player import Player
from Network import Network

def read_pos(str):
    str = str.split(",")
    return [int(str[0]), int(str[1])]

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def main(): 
    n = Network("127.0.0.1")
    n.connect()
    startPos = read_pos(n.getPos())

    pygame.init()

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    CHARACTER_WIDTH = 150
    CHARACTER_HEIGHT = 80

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Volta\'s Fighters')

    player1 = Player(startPos[0], startPos[1], CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
    player2 = Player(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)

    running = True

    clock = pygame.time.Clock()
    FPS = 60

    def draw_bg():
        screen.fill((0, 0, 0))

    def update_player2():
        player2pos = read_pos(n.send(make_pos((player1.rect.x, player1.rect.y))))
        player2.set_x(player2pos[0])
        player2.set_y(player2pos[1])
    
    while running:
        clock.tick(FPS)

        draw_bg()

        # Let the player jump until they reach the top of the screen.
        player1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        player1.draw(screen)
        
        
        player2.draw(screen)
        update_player2()
        # Collision with other player
        # if player1.rect.colliderect(player2.rect):
        #     player1.rect.x -= player1.SPEED
        #     player2.rect.x += player2.SPEED

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
