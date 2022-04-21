import pygame
from pygame.locals import *
import oop.asset_module as am

class Player(pygame.sprite.Sprite):
    vec = pygame.math.Vector2
    ACC = 2
    FRIC = -0.12
    
    def __init__(self, resolution, image_path = am.dino_path()):
        super().__init__()
        self.width = resolution[0]
        self.height = resolution[1]
        self.image_path = image_path
        self.step = 0
        self.state = 'walk'
        self.sprites = self.sprites()
        self.surf = self.sprites[0]
        # self.surf.fill((244, 50, 40))
        self.rect = self.surf.get_rect()
        self.pos = Player.vec((20, 30))
        self.vel = Player.vec(0,0)
        self.acc = Player.vec(0,0)
        self.jumping = False
    
    def move(self):
        self.acc = Player.vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -Player.ACC
            self.steps(1)
            self.surf = pygame.transform.flip(self.sprites[self.step//3], True, False)
        if pressed_keys[K_RIGHT]:
            self.acc.x = Player.ACC
            self.steps(1)
            self.surf = pygame.transform.flip(self.sprites[self.step//3], False, False)
                 
        self.acc.x += self.vel.x * Player.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width
             
        self.rect.midbottom = self.pos
    
    def jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15
           
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
    
    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
    
    def steps(self, speed):
        #if(speed < 0):
        #    if self.step < 0:
        #        self.step = 9*3
        #else:
        if self.step >= 9*3:
            self.step = 0
        
        self.step += speed
    
    def sprites(self):
        return [
            pygame.image.load(f'{self.image_path}Walk (1).png'),
            pygame.image.load(f'{self.image_path}Walk (2).png'),
            pygame.image.load(f'{self.image_path}Walk (3).png'),
            pygame.image.load(f'{self.image_path}Walk (4).png'),
            pygame.image.load(f'{self.image_path}Walk (5).png'),
            pygame.image.load(f'{self.image_path}Walk (6).png'),
            pygame.image.load(f'{self.image_path}Walk (7).png'),
            pygame.image.load(f'{self.image_path}Walk (8).png'),
            pygame.image.load(f'{self.image_path}Walk (9).png'),
            pygame.image.load(f'{self.image_path}Walk (10).png'),
            ]