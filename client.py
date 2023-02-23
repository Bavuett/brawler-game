import pygame
from Player import Player
from Network import Network

def read_status(str):
    str = str.split(",")
    return [int(str[0]), int(str[1]), int(str[2]), int(str[3])]

def make_status(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])

def main(): 
    n = Network("127.0.0.1")
    n.connect()
    startPos = read_status(n.getPos())
    print(startPos)

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

    SPRITESHEETS = [
        pygame.image.load("./content/larocca_spritesheet.png").convert_alpha(), 
        pygame.image.load("./content/micalone_spritesheet.png").convert_alpha()
    ]

    player1 = Player(startPos[0], startPos[1], LAROCCA_DATA, SCREEN_WIDTH, SCREEN_HEIGHT, SPRITESHEETS[0])
    player2 = Player(0, 0, MICALONE_DATA, SCREEN_WIDTH, SCREEN_HEIGHT, SPRITESHEETS[1])

    running = True

    clock = pygame.time.Clock()
    FPS = 60

    #health bar
    def draw_health_bar(health, x, y):
        ratio = health/100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))

    def draw_bg():
        screen.fill((0, 0, 0))

    def update_player2():
        player2status = read_status(n.send(make_status((player1.rect.x, player1.rect.y, player1.health, player1.ATTACKING))))
        player2.set_x(player2status[0])
        player2.set_y(player2status[1])
        player2.set_health(player2status[2])
        
        if (player2status[3] == 1):
            player2.attack(screen, player1)

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
