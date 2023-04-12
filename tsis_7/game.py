import pygame
import datetime

pygame.init()

clock = pygame.time.Clock()

background = pygame.image.load('/Users/gaukhar/tsis_7/img/mickeyclock.png')
second = pygame.image.load('/Users/gaukhar/tsis_7/img/sec.png')
minute = pygame.image.load('/Users/gaukhar/tsis_7/img/min.png')

WIDTH = 1400
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey clock's")

t = datetime.datetime.now()
ang_S = -(int(t.strftime("%S")) * 6) - 6
ang_M = -(int(t.strftime("%M")) * 6 + (int(t.strftime("%S")) * 6 / 60)) - 54


def rotate(img, rect, ang):
    new_img = pygame.transform.rotate(img, ang)
    rect = new_img.get_rect(center=rect.center)
    return new_img, rect


image = pygame.Surface((60, HEIGHT), pygame.SRCALPHA)
image.blit(second, (0, 0))
orig_image = image
rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

imagem = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
imagem.blit(minute, (0, 0))
orig_imagem = imagem
rect1 = imagem.get_rect(center=(WIDTH // 2, HEIGHT // 2))

finished = True

while finished:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = False

    screen.blit(background, (0, 0))
    screen.blit(image, rect)
    screen.blit(imagem, rect1)
    image, rect = rotate(orig_image, rect, ang_S)
    imagem, rect1 = rotate(orig_imagem, rect1, ang_M)

    ang_S -= 0.099
    ang_M -= 0.099 / 60

    pygame.display.flip()

pygame.quit()