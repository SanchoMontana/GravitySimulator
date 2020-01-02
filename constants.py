import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
FPS = 100

DEEP_BLUE = (10, 10, 30)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 10)
GREEN = (0, 255, 0)
G = 6.67E-11
COLLISION_DISTANCE = 3
DELTA_DILATION = 0.05

# Pygame display initialization and setup
pygame.init()
pygame.mouse.set_visible(True)
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
