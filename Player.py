import pygame

class Player:
    def __init__(self, x, y, data, sc_width, sc_height, sprite_sheet, animation_count):
        self.SPEED = 5
        self.SCREEN_WIDTH = sc_width
        self.SCREEN_HEIGHT = sc_height
        self.image_scale = data[2]
        self.offset = data[3]
        self.animation_list = [self.load_images(sprite_sheet,animation_count)]
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.START_X = x
        self.START_Y = y
        self.WIDTH = data[0]
        self.HEIGHT = data[1]
        self.GRAVITY = 1
        self.JUMP_HEIGHT = -15
        self.HEALTH = 100
        self.attacking = False
        self.jumping = False
        self.running = False

        self.vel_y = 0
        self.jumping = False
        
        self.rect = pygame.Rect(self.START_X, self.START_Y, self.WIDTH, self.HEIGHT)

    def load_images(self, sprite_sheet, animation_count):
        #extract the sprite sheet
        animation_list = []
        for y, animation in enumerate(animation_count):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size_width, y * self.size_height, self.size_width, self.size_height)
                img_scaled = pygame.transform.scale(temp_img, (self.image_scale * self.size_width, self.image_scale * self.size_height))
                temp_img_list.append(img_scaled)
            animation_list.append(temp_img_list)
        return animation_list

    def jump(self):
        self.jumping = True
        self.vel_y = self.JUMP_HEIGHT
    
    def move(self, sc_width, sc_height, surface, target):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            dx -= self.SPEED
        if key[pygame.K_d]:
            dx += self.SPEED
        if key[pygame.K_SPACE] and self.jumping == False:
            self.jump()
        
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

        #attack
        if key[pygame.K_f]:
            self.attack(surface, target)

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  
            
        self.vel_y += self.GRAVITY
        dy += self.vel_y

        

    def draw(self, surface): 
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        surface.blit(img, (self.rect.x - self.offset[0], self.rect.y - self.offset[1]))

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


    
    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width + 50, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.HEALTH -= 10
        pygame.draw.rect(surface, (255, 0, 0), attacking_rect)