import pygame
from pygame.constants import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((720, 480))
    pygame.display.set_caption('Basic')

    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill((0, 0, 0))

    font = pygame.font.Font(None, 32)
    text = font.render("Hello", 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    screen.blit(text, textpos)
    pygame.display.flip()

    print dir(pygame.constants)

    text_display = True
    while 1:
        keys = set([])
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                keys.add(event.key)
                if event.key == K_ESCAPE:
                    return
                

        if K_SPACE in keys:
            text_display = text_display != True

        if text_display:
            screen.blit(text, textpos)
        else:
            screen.blit(background, (0, 0))

        pygame.display.flip()

if __name__ == '__main__':
    main()