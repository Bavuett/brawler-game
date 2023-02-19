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

    print(n.send("life"))

    pygame.init()
    
    #window
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    #character variables
    SCALE = 2
    OFFSET_LAROCCA = [48, 40]
    LAROCCA_SIZE_WIDTH = 65
    LAROCCA_SIZE_HEIGHT = 110
    LAROCCA_DATA = [LAROCCA_SIZE_WIDTH, LAROCCA_SIZE_HEIGHT, SCALE, OFFSET_LAROCCA]
    OFFSET_MICALONE = [48, 40]
    MICALONE_SIZE_WIDTH = 65
    MICALONE_SIZE_HEIGHT = 110
    MICALONE_DATA = [MICALONE_SIZE_WIDTH, MICALONE_SIZE_HEIGHT, SCALE, OFFSET_MICALONE]

    #colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)   
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Volta\'s Fighters')

    player1 = Player(startPos[0], startPos[1], LAROCCA_DATA, SCREEN_WIDTH, SCREEN_HEIGHT)
    player2 = Player(0, 0,MICALONE_DATA, SCREEN_WIDTH, SCREEN_HEIGHT)

    running = True

    clock = pygame.time.Clock()
    FPS = 60

    #health bar
    def draw_health_bar(health, x, y):
        ratio = health/100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, GREEN, (x, y, 400*ratio, 30))

    def draw_bg():
        screen.fill((0, 0, 0))

    def update_player2():
        player2pos = read_pos(n.send(make_pos((player1.rect.x, player1.rect.y))))
        player2.set_x(player2pos[0])
        player2.set_y(player2pos[1])
    
    while running:
        clock.tick(FPS)

        draw_bg()
        draw_health_bar(player1.health, 20, 20)
        draw_health_bar(player2.health, 580, 20)

        # Let the player jump until they reach the top of the screen.
        player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2)
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
