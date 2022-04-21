import sys
import pygame
from pygame.locals import *
from oop.platform import Platform
from oop.player import Player
import oop.asset_module as am

pygame.init()
WIDTH  = 1280
HEIGHT = 600
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game OOP")

PT1 = Platform(WIDTH, HEIGHT)
P1 = Player((WIDTH, HEIGHT), image_path=am.santa_path())

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

while True:
    P1.update(platforms)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump(platforms)
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()  
    
    displaysurface.fill((255,255,255))
    
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    
    pygame.display.update()
    FramePerSec.tick(FPS)