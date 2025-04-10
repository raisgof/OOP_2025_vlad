import pygame
import sys
from typing import List, Tuple, Dict, Any

# Инициализация Pygame
pygame.init()

# Конфигурация объектов
HARE_CONFIG = {
    "body": {
        "width_ratio": 0.5,  # Отношение ширины тела к общей ширине зайца
        "height_ratio": 0.5,  # Отношение высоты тела к общей высоте зайца
        "y_offset": 0.5  # Смещение центра тела по Y относительно центра зайца
    },
    "head": {
        "size_ratio": 0.25,  # Отношение размера головы к общей высоте зайца
        "y_offset": -0.125  # Смещение головы по Y относительно центра зайца
    },
    "ears": {
        "width_ratio": 0.125,  # Отношение ширины уха к общей ширине зайца
        "height_ratio": 0.33,  # Отношение высоты уха к общей высоте зайца
        "y_offset": -0.5,  # Смещение ушей по Y относительно центра зайца
        "x_offsets": [-0.125, 0.125]  # Смещения ушей по X относительно центра зайца
    },
    "legs": {
        "width_ratio": 0.25,  # Отношение ширины ноги к общей ширине зайца
        "height_ratio": 0.0625,  # Отношение высоты ноги к общей высоте зайца
        "y_offset": 0.5,  # Смещение ног по Y относительно центра зайца
        "x_offsets": [-0.25, 0.25]  # Смещения ног по X относительно центра зайца
    },
    "face": {
        "eye_radius_ratio": 0.025,  # Радиус глаза относительно размера головы
        "eye_x_offset": 0.2,  # Смещение глаз по X относительно центра головы
        "eye_y_offset": -0.1,  # Смещение глаз по Y относительно центра головы
        "nose_points_ratio": [  # Точки носа относительно размера головы
            (0, 0.1),
            (-0.066, 0),
            (0.066, 0)
        ],
        "mouth_width_ratio": 0.33,  # Ширина рта относительно размера головы
        "mouth_y_offset": 0.2  # Смещение рта по Y относительно центра головы
    }
}

# Конфигурация сцены
SCENE_CONFIG = {
    "screen_size": (800, 600),
    "background_color": (255, 255, 255),
    "hares": [
        {
            "position": (400, 300),
            "size": (200, 400),
            "color": (200, 200, 200)
        }
        # Можно добавить больше зайцев:
        # {"position": (200, 200), "size": (100, 200), "color": (150, 150, 150)},
        # {"position": (600, 400), "size": (150, 300), "color": (180, 180, 180)}
    ]
}


def draw_ellipse(surface: pygame.Surface, x: float, y: float, 
                 width: float, height: float, color: Tuple[int, int, int]) -> None:
    """Рисует эллипс с центром в указанных координатах."""
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_circle(surface: pygame.Surface, x: float, y: float, 
                radius: float, color: Tuple[int, int, int]) -> None:
    """Рисует круг с центром в указанных координатах."""
    pygame.draw.circle(surface, color, (int(x), int(y)), int(radius))


def draw_head(surface: pygame.Surface, x: float, y: float, 
              size: float, color: Tuple[int, int, int]) -> None:
    """Рисует голову зайца с глазами, носом и ртом."""
    # Голова (основной круг)
    draw_circle(surface, x, y, size / 2, color)

    # Параметры лица на основе конфигурации
    cfg = HARE_CONFIG["face"]
    eye_radius = size * cfg["eye_radius_ratio"]
    
    # Глаза
    left_eye_x = x - size * cfg["eye_x_offset"]
    right_eye_x = x + size * cfg["eye_x_offset"]
    eye_y = y + size * cfg["eye_y_offset"]
    draw_circle(surface, left_eye_x, eye_y, eye_radius, (0, 0, 0))
    draw_circle(surface, right_eye_x, eye_y, eye_radius, (0, 0, 0))

    # Нос
    nose_points = [
        (x + size * point[0], y + size * point[1]) 
        for point in cfg["nose_points_ratio"]
    ]
    pygame.draw.polygon(surface, (255, 150, 150), nose_points)

    # Рот
    mouth_width = size * cfg["mouth_width_ratio"]
    mouth_y = y + size * cfg["mouth_y_offset"]
    mouth_start = (x - mouth_width / 2, mouth_y)
    mouth_end = (x + mouth_width / 2, mouth_y)
    pygame.draw.line(surface, (0, 0, 0), mouth_start, mouth_end, 2)


def draw_hare(surface: pygame.Surface, x: float, y: float, 
              width: float, height: float, color: Tuple[int, int, int]) -> None:
    """Рисует зайца на экране."""
    cfg = HARE_CONFIG
    
    # Тело
    body_width = width * cfg["body"]["width_ratio"]
    body_height = height * cfg["body"]["height_ratio"]
    body_y = y + height * cfg["body"]["y_offset"]
    draw_ellipse(surface, x, body_y, body_width, body_height, color)

    # Голова
    head_size = height * cfg["head"]["size_ratio"]
    head_y = y + height * cfg["head"]["y_offset"]
    draw_head(surface, x, head_y, head_size, color)

    # Уши
    ear_width = width * cfg["ears"]["width_ratio"]
    ear_height = height * cfg["ears"]["height_ratio"]
    ear_y = y + height * cfg["ears"]["y_offset"]
    for x_offset in cfg["ears"]["x_offsets"]:
        ear_x = x + width * x_offset
        draw_ellipse(surface, ear_x, ear_y, ear_width, ear_height, color)

    # Ноги
    leg_width = width * cfg["legs"]["width_ratio"]
    leg_height = height * cfg["legs"]["height_ratio"]
    leg_y = y + height * cfg["legs"]["y_offset"]
    for x_offset in cfg["legs"]["x_offsets"]:
        leg_x = x + width * x_offset
        draw_ellipse(surface, leg_x, leg_y, leg_width, leg_height, color)


def main():
    # Настройка экрана
    screen = pygame.display.set_mode(SCENE_CONFIG["screen_size"])
    pygame.display.set_caption("Рисуем зайца")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка фона
        screen.fill(SCENE_CONFIG["background_color"])

        # Отрисовка всех зайцев
        for hare in SCENE_CONFIG["hares"]:
            draw_hare(screen, *hare["position"], *hare["size"], hare["color"])

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
