import pygame

class Fighter():

    def __init__(self,x,y, data, sprite_sheet, animation_count):
        self.size_width = data[0]
        self.image_scale = data[2]
        self.size_height = data[1]
        self.animation_list = self.load_images(sprite_sheet, animation_count)
        self.action = 0 #0idle #1run #2jump #3attack #4hit #5dead
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.offset = data[3]
        self.flip = False
        self.rect = pygame.Rect(x,y,80,180)
        self.vel_y = 0
        self.jump = False
        self.attack_controll = False
        self.attack_type = ''
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

    def draw(self,surface):
        pygame.draw.rect(surface,(0,0,0),self.rect)
        surface.blit(self.image, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    def move(self,SCREEN_WIDTH,SCREEN_HEIGHT, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Get all the keys currently pressed
        keys = pygame.key.get_pressed()

        if self.attack_controll == False:

            #movement
            if keys[pygame.K_LEFT]:
                dx -= SPEED
            if keys[pygame.K_RIGHT]:
                dx += SPEED
            if keys[pygame.K_UP] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            #attack

            if keys[pygame.K_c] or keys[pygame.K_v]:

                self.attacking(surface, target)

                #attack type
                if keys[pygame.K_c]:
                    attack_type = 'punch'
                if keys[pygame.K_v]:
                    attack_type = 'kick'

        
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

        #ensure player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #update position
        self.rect.x += dx
        self.rect.y += dy   
    def attacking(self,surface, target):
        self.attack_controll = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2*self.rect.width, self.rect.height)  

        if attacking_rect.colliderect(target.rect):
            target.health -= 10 

        pygame.draw.rect(surface, (0,255,0), attacking_rect)
        