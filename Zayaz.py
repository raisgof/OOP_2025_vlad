import pygame
import sys

pygame.init()

def draw_body(surface, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - цвет в формате pygame.Color
    '''
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца с глазами, носом и ртом.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    # Голова (основной круг)
    pygame.draw.circle(surface, color, (x, y), size // 2)

    eye_radius = size // 10
    left_eye_x = x - size // 5
    right_eye_x = x + size // 5
    eye_y = y - size // 10
    pygame.draw.circle(surface, (0, 0, 0), (left_eye_x, eye_y), eye_radius)
    pygame.draw.circle(surface, (0, 0, 0), (right_eye_x, eye_y), eye_radius)


    nose_points = [
        (x, y + size // 10),
        (x - size // 15, y),
        (x + size // 15, y)
    ]
    pygame.draw.polygon(surface, (255, 150, 150), nose_points)


    mouth_start = (x - size // 6, y + size // 5)
    mouth_end = (x + size // 6, y + size // 5)
    pygame.draw.line(surface, (0, 0, 0), mouth_start, mouth_end, 2)

    # Можно добавить улыбку в виде дуги:
    # pygame.draw.arc(surface, (0, 0, 0),
    #                (x - size//4, y + size//8, size//2, size//3),
    #                0.2, 2.9, 2)
def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - цвет в формате pygame.Color
    '''
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - цвет в формате pygame.Color
    '''
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_hare(surface, x, y, width, height, color):
    '''
    Рисует зайца на экране.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - цвет в формате pygame.Color
    '''

    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)


    head_size = height // 4
    draw_head(surface, x, y - head_size // 2, head_size, color)


    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(surface, ear_x, ear_y, width // 8, ear_height, color)


    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(surface, leg_x, leg_y, width // 4, leg_height, color)



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Рисуем зайца")


background_color = (255, 255, 255)

hare_color = (200, 200, 200)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    draw_hare(screen, 400, 300, 200, 400, hare_color)
    pygame.display.flip()

pygame.quit()
sys.exit()