import pygame, sys
from pygame import KEYDOWN


class Circle(pygame.sprite.Sprite):
    def __init__(self, size=(50, 50), init_pos=(50, 50), color=(255, 0, 0)):
        self.size = size
        self.init_pos = init_pos
        self.color = color


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    x_pos = 50
    y_pos = 50

    while True:
        for event in pygame.event.get((KEYDOWN)):
            match event.type:
                case pygame.QUIT:
                    pygame.exit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            if y_pos < 45:
                                y_pos += 0
                            else:
                                y_pos -= 20
                        case pygame.K_DOWN:
                            if y_pos > 555:
                                y_pos += 0
                            else:
                                y_pos += 20
                        case pygame.K_LEFT:
                            if x_pos < 45:
                                x_pos -= 0
                            else:
                                x_pos -= 20
                        case pygame.K_RIGHT:
                            if x_pos > 755:
                                x_pos += 0
                            else:
                                x_pos += 20

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 25)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
