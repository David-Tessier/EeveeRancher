import pygame


class imgManager:
    def __init__(self, screen, w, h, flip, value, sizew, sizeh):

        self.value = value
        img = pygame.image.load(value)
        img = pygame.transform.scale(img, (sizew, sizeh))
        self.flip = flip

        if flip:
            img = pygame.transform.flip(img, True, False)
        self.imgDone = img.convert_alpha()
        img.convert()
        self.w = w
        self.h = h
        self.rect = img.get_rect()
        self.rect.center = w, h
        screen.blit(img, self.rect)
