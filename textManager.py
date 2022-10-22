import pygame


class textManager:
    def __init__(self, Value, font, screen, w, h):
        text = font.render(Value, True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (w, h)
        screen.blit(text, textRect)
