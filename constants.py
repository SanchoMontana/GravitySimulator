import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
FPS = 50

DEEP_BLUE = (10, 10, 30)
RED = (255, 0, 0)
GRAY = (50, 50, 50)

pygame.init()
pygame.mouse.set_visible(True)
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
