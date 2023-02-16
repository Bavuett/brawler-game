import pygame

class Fighter():

    def __init__(self, x, y, flip, data, sprite_sheet, animation_count):
        self.size_width = data[0]
        self.image_scale = data[2]
        self.size_height = data[1]
        self.animation_list = self.load_images(sprite_sheet, animation_count)
        self.action = 0 #0idle #1jump #2run #3attack 
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.running = False
        self.offset = data[3]
        self.flip = flip
        self.rect = pygame.Rect(x,y,80,180)
        self.vel_y = 0
        self.jump = False
        self.attack_controll = False
        self.health = 100
    
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
            print(animation_list)
        return animation_list

    def draw(self, surface):

        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface,(0,0,0),self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    def move(self,SCREEN_WIDTH,SCREEN_HEIGHT, surface, target):
        SPEED = 10
        GRAVITY = 2
        self.running = False
        dx = 0
        dy = 0

        # Get all the keys currently pressed
        keys = pygame.key.get_pressed()

        if self.attack_controll == False:

            #movement
            if keys[pygame.K_LEFT]:
                dx -= SPEED
                self.running = True
            if keys[pygame.K_RIGHT]:
                dx += SPEED
                self.running = True
            if keys[pygame.K_UP] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            
            #gravity
            self.vel_y += GRAVITY
            dy += self.vel_y
            
            #ensure player stays on screen
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > SCREEN_WIDTH:
                dx = SCREEN_WIDTH - self.rect.right
            if self.rect.bottom + dx > SCREEN_HEIGHT-110:
                self.jump = False
                dy = SCREEN_HEIGHT - 110 - self.rect.bottom
                self.vel_y = 0
            
            #update position
            self.rect.x += dx
            self.rect.y += dy 

            #attack

            if keys[pygame.K_c]:
                self.attacking(surface, target)

        #ensure player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True  

    #animation update
    def update(self):
        #checking which action the player is doing
        if self.attack_controll == True:
            self.update_action(3)
            print(self.action)
        elif self.running == True:
            self.update_action(2)
            print(self.action)
        elif self.jump == True:
            self.update_action(1)
            print(self.action)
        else:
            self.update_action(0)
            print(self.action)
    
        ANIMATION_COOLDOWN = 500
        self.image = self.animation_list[self.action][self.frame_index]
        self.frame_index = 0
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            #checking if the player is attacking
            if self.action == 3:
                self.attack_controll = False
                print ("attack")

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def attacking(self,surface, target):
        self.attack_controll = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2*self.rect.width, self.rect.height)  

        if attacking_rect.colliderect(target.rect):
            target.health -= 10 

        pygame.draw.rect(surface, (0,255,0), attacking_rect)
        