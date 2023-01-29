import pygame

class Player:
    def __init__(self, x, y):
        self.SPEED = 5
        self.WIDTH = x
        self.HEIGHT = y
        self.GRAVITY = 2
        
        self.rect = pygame.Rect(x, y, self.HEIGHT, self.WIDTH)
    
    def move(self, max_width, max_height):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx -= self.SPEED
        if key[pygame.K_d]:
            dx += self.SPEED
        if key[pygame.K_w]:
            dy -= self.SPEED
        if key[pygame.K_s]:
            dy += self.SPEED

        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > max_width:
            dx = 0
        if self.rect.top + dy < 0:
            dy = 0
        if self.rect.bottom + dy > max_height:
            dy = 0
        
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface): 
        pygame.draw.rect(surface, (255, 255, 255), self.rect)