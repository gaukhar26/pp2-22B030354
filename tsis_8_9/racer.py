import random
import time
import pygame
import sys
from pygame.locals import *

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
SCORE_COIN = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over = font.render("Game Over", True, BLACK)
ScoreView = font.render("Score:" + str(SCORE), True, BLACK)
ScoreCoinView = font.render("Coin Score:" + str(SCORE_COIN), True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), 0)

    def move(self):
        global SCORE_COIN

        if pygame.sprite.spritecollideany(P1, bonus):
            pygame.mixer.Sound('monetka.wav').play()
            SCORE_COIN += 1
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), 0)

        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), 0)


class Mega_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin 2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), 0)

    def move(self):
        global SCORE_COIN

        if pygame.sprite.spritecollideany(P1, second_bonus):
            pygame.mixer.Sound('monetka.wav').play()
            SCORE_COIN += 5
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), -400)

        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), -400)


P1 = Player()
E1 = Enemy()
C1 = Coin()
M1 = Mega_Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

second_bonus = pygame.sprite.Group()
second_bonus.add(M1)

bonus = pygame.sprite.Group()
bonus.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(M1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 10000)

while True:
    for event in pygame.event.get():
        if SCORE_COIN > 10:
            SPEED += 0.05
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    scores_coin = font_small.render(str(SCORE_COIN), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(scores_coin, (370, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 100))
        DISPLAYSURF.blit(ScoreView, (30, 250))
        DISPLAYSURF.blit(ScoreCoinView, (30, 400))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)