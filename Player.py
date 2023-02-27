import pygame


class Player:
    def __init__(self, x, y, data, sc_width, sc_height, sprites, flip):
        self.SPEED = 5
        self.SCREEN_WIDTH = sc_width
        self.SCREEN_HEIGHT = sc_height
        self.START_X = x
        self.START_Y = y
        self.WIDTH = data[0]
        self.HEIGHT = data[1]
        self.GRAVITY = 1
        self.JUMP_HEIGHT = -15
        self.HEALTH = 100
        self.ATTACKING = 0
        self.ATTACKING_VIA_SERVER = 0
        self.SPRITES = sprites

        self.ANIMATIONS = self.load_images(self.SPRITES, [1, 4, 4, 1, 3])
        self.ANIMATION_INDEX = 0
        self.ANIMATION_TIME = 0

        self.vel_y = 0
        self.jumping = False

        self.flip = flip
        self.offset = data[3]
        self.image_scale = data[2]

        self.attack_controll = False
        self.running = False

        self.action = 0
        self.update_time = pygame.time.get_ticks()

        self.health = 100
        self.rect = pygame.Rect(
            self.START_X, self.START_Y, self.WIDTH, self.HEIGHT)

    def load_images(self, sprite_sheet, animation_count):
        # extract the sprite sheet
        animation_list = []
        for y, animation in enumerate(animation_count):
            temp_img_list = []

            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    x * self.WIDTH, y * self.HEIGHT, self.WIDTH, self.HEIGHT)
                
                img_scaled = pygame.transform.scale(
                    temp_img, (2 * self.WIDTH, 2 * self.HEIGHT))
                
                temp_img_list.append(img_scaled)
            
            animation_list.append(temp_img_list)
        
        return animation_list

    def jump(self):
        self.jumping = True
        self.update_action(1)
        self.vel_y = self.JUMP_HEIGHT

    def move(self, sc_width, sc_height, surface, target):
        self.update()
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx -= self.SPEED
            self.update_action(2)
        if key[pygame.K_e]:
            self.health -= 10
            self.update_action(3)
        if key[pygame.K_d]:
            dx += self.SPEED
        if key[pygame.K_SPACE] and self.jumping == False:
            self.jump()
        if key[pygame.K_r]:
            self.health = 100
        # attack
        if key[pygame.K_f] and self.ATTACKING_VIA_SERVER == 0:
            self.ATTACKING = 1
        else:
            if self.ATTACKING_VIA_SERVER == 0:
                self.ATTACKING = 0

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

        if self.ATTACKING == 1:
            self.attack(surface, target)

        self.rect.x += dx
        self.rect.y += dy

        if target.rect.centerx < self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update(self):
        #checking which action the player is doing
        if self.attack_controll == True:
            self.update_action(3)
        elif self.running == True:
            self.update_action(2)
        elif self.jump == True:
            self.update_action(1)
        else:
            self.update_action(0)
            
        ANIMATION_COOLDOWN = 500
        self.image = self.ANIMATIONS[self.action][self.ANIMATION_INDEX]
        self.ANIMATION_INDEX = 0
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.ANIMATION_INDEX += 1
            self.update_time = pygame.time.get_ticks()
        if self.ANIMATION_INDEX >= len(self.ANIMATIONS[self.action]):
            self.ANIMATION_INDEX = 0
            #checking if the player is attacking
            if self.action == 3:
                self.attack_controll = False
                print ("attack")


    def draw(self, surface):
        img = pygame.transform.flip(self.ANIMATIONS[0][self.ANIMATION_INDEX], self.flip, False)
        pygame.draw.rect(surface,(0,0,0),self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y

    def set_health(self, health):
        self.health = health

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width + 50, self.rect.height)
        
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (255, 0, 0), attacking_rect)
