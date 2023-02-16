import pygame

class Player:
    def __init__(self, x, y, width, height, sc_width, sc_height):
        self.SPEED = 5
        self.SCREEN_WIDTH = sc_width
        self.SCREEN_HEIGHT = sc_height
        self.START_X = x
        self.START_Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.GRAVITY = 1
        self.JUMP_HEIGHT = -15

        self.vel_y = 0
        self.jumping = False
        
        self.rect = pygame.Rect(self.START_X, self.START_Y, self.HEIGHT, self.WIDTH)

    def jump(self):
        self.jumping = True
        self.vel_y = self.JUMP_HEIGHT
    
    def move(self, sc_width, sc_height):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            dx -= self.SPEED
        if key[pygame.K_d]:
            dx += self.SPEED
        if key[pygame.K_SPACE] and self.jumping == False:

            self.jump()
            
        self.vel_y += self.GRAVITY
        dy += self.vel_y

        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.bottom + dy > self.SCREEN_HEIGHT - 50:
            self.rect.bottom = self.SCREEN_HEIGHT - 50
            dy = 0
            self.jumping = False
        
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface): 
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y