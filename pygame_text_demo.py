import pygame
from pygame.locals import *


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 400))
    font = pygame.font.Font(None, 24)
    running = True
    typed = ''
    while running:
        surface.fill('white')
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    typed = typed[:-1]
                else:
                    typed += event.unicode
        text = font.render(typed, True, 'black')
        surface.blit(text, (20, 200))
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
