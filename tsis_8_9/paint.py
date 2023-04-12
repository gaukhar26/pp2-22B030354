import pygame
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
RAD = 15

# инициализация картинок
rectangle = pygame.image.load("./img/rect.png")
circle = pygame.image.load("./img/circ.png")
eras = pygame.image.load("./img/eraser.png")
brush = pygame.image.load("./img/brush.png")
clrs = pygame.image.load("./img/clrscr.png")
triangle = pygame.image.load("./img/triangle.png")
truetriangle = pygame.image.load("./img/truetriangle.png")
rhombus = pygame.image.load("./img/rhombus.png")
square = pygame.image.load("./img/square.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

finished = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

drawing = False
color = BLACK

screen.fill(WHITE)

start_pos = 0
end_pos = 0

# режим рисования
mode = 4

# массив цветов
COLORS = []

for _ in range(17):
    COLORS.append((randint(0, 255), randint(0, 255), randint(0, 255)))


def brushka(srf, color, start, end, radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)


while not finished:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # если нажимать кнопку мыши, начинается отсчет координат х и у
            drawing = True
            start_pos = pos
            # позиция кнопок для нажатия
            if pos[0] > 765 and pos[0] < 800 and pos[1] > 0 and pos[1] < HEIGHT:
                color = screen.get_at(pos)
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 0 and pos[1] < 35:
                mode = 1
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 35 and pos[1] < 70:
                mode = 2
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 70 and pos[1] < 105:
                mode = 3
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 105 and pos[1] < 140:
                mode = 0
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 140 and pos[1] < 175:
                mode = 4
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 175 and pos[1] < 210:
                mode = 5
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 210 and pos[1] < 245:
                mode = 6
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 245 and pos[1] < 280:
                mode = 7
            if pos[0] > 0 and pos[0] < 35 and pos[1] > 280 and pos[1] < 315:
                screen.fill(WHITE)

        if event.type == pygame.MOUSEBUTTONUP:
            # если отпускать кнопку мыши, отсчет заканчивается и находим разницу х и у чтобы определить width и height
            global x, y
            drawing = False
            end_pos = pos
            x = abs(start_pos[0] - end_pos[0])
            y = abs(start_pos[1] - end_pos[1])

            # режимы для рисования
            if mode == 1:
                pygame.draw.rect(screen, color, (pos[0], pos[1], x, y), 4)
            elif mode == 2:
                pygame.draw.circle(screen, color, pos, x, 4)
            elif mode == 4:
                pygame.draw.rect(screen, color, (pos[0], pos[1], x, x), 4)
            elif mode == 5:
                pygame.draw.polygon(screen, color, [pos, [pos[0] - x, pos[1] + y], [pos[0] + x, pos[1] + y]], 4)
            elif mode == 6:
                pygame.draw.polygon(screen, color, [pos, [pos[0] - x, pos[1] + x], [pos[0] + x, pos[1] + x]], 4)
            elif mode == 7:
                pygame.draw.polygon(screen, color,
                                    [pos, [pos[0] + x, pos[1] + x], [pos[0] + 2 * x, pos[1]], [pos[0] + x, pos[1] - x]],
                                    4)

        if event.type == pygame.MOUSEMOTION:
            if mode == 0:
                # pygame.draw.circle(screen, WHITE, pos, RAD)
                if drawing:
                    pygame.draw.circle(screen, color, pos, RAD)
                    brushka(screen, color, pos, end_pos, RAD)
                end_pos = pos
            if mode == 3:
                pygame.draw.circle(screen, WHITE, pos, 20)

    # расположение палитр
    each = 35
    for i, col in enumerate(COLORS):
        pygame.draw.rect(screen, col, (765, i * each, each, 35))

    # отрисовка кнопок
    rectangle_size = rectangle.get_rect()
    screen.blit(rectangle, rectangle_size)

    circle_size = rectangle.get_rect()
    screen.blit(circle, (circle_size[0], circle_size[1] + 35))

    eras_size = eras.get_rect()
    screen.blit(eras, (eras_size[0], eras_size[1] + 70))

    brush_size = brush.get_rect()
    screen.blit(brush, (brush_size[0], brush_size[1] + 105))

    sq_size = square.get_rect()
    screen.blit(square, (sq_size[0], sq_size[1] + 140))

    trian_size = triangle.get_rect()
    screen.blit(triangle, (trian_size[0], trian_size[1] + 175))

    truetrian_size = truetriangle.get_rect()
    screen.blit(truetriangle, (truetrian_size[0], truetrian_size[1] + 210))

    rhombus_size = rhombus.get_rect()
    screen.blit(rhombus, (rhombus_size[0], rhombus_size[1] + 245))

    clrs_size = clrs.get_rect()
    screen.blit(clrs, (clrs_size[0], clrs_size[1] + 280))

    pygame.display.flip()
pygame.quit()