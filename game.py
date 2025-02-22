import pygame
import os
import sys
import random



pygame.init()
font = pygame.font.SysFont('aria', 40)
current_path = os.path.dirname(__file__)
os.chdir(current_path)

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
from loade import *
def game():
    screen.fill('grey')


    kaktus_group.update()
    kaktus_group.draw(screen)
    dino_group.update()
    dino_group.draw(screen)
    pygame.display.update()

def restart():
    global dino_group, kaktus_group
    dino_group = pygame.sprite.Group()
    kaktus_group = pygame.sprite.Group()
    player = Player()
    dino_group.add(player)

class Kaktus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = kaktus_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 500)
        self.rect.bottom = HEIGHT - 60
        self.speed = 10
    def update(self):
        self.rect.x -= self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = dino_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.bottom = HEIGHT - 60
        self.jump = False
        self.jump_step = -22
        self.timer_spawn = 0
    def update(self):
        global FPS
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 22:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -22
        self.timer_spawn +=  1
        if self.timer_spawn / FPS > 2:
            kaktus = Kaktus()
            kaktus_group.add(kaktus)
            self.timer_spawn = 0
        if pygame.sprite.spritecollide(self, kaktus_group, True):
            self.kill()
            FPS = 0






restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()
    clock.tick(FPS)