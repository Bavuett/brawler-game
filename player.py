import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.SPEED = 5
        self.WIDTH = width
        self.HEIGHT = height
        self.GRAVITY = 1
        self.JUMP_HEIGHT = -15

        self.vel_y = 0
        self.jumping = False
        
        self.rect = pygame.Rect(x, y, self.HEIGHT, self.WIDTH)
    
    def move(self, sc_width, sc_height):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx -= self.SPEED
        if key[pygame.K_d]:
            dx += self.SPEED
        if key[pygame.K_SPACE] and self.jumping == False:
            self.jumping = True
            self.vel_y = self.JUMP_HEIGHT
        
        self.vel_y += self.GRAVITY
        dy += self.vel_y

        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > sc_width:
            self.rect.right = sc_width
        if self.rect.bottom + dy > sc_height - 50:
            self.rect.bottom = sc_height - 50
            dy = 0
            self.jumping = False
            
        
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface): 
        pygame.draw.rect(surface, (255, 255, 255), self.rect)