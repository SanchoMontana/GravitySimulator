import pygame
from constants import *
from operator import add
from math import e

translation_old = [0, 0]
translation = [0, 0]
delta_translation = [0, 0]
dilation = 1
dilation_old = 1
delta_dilation_iterator = 0
dilation_iterator = 0
trail_toggle = True
# ctrl is either True or False, depending on whether the LCTRL key is being held.
ctrl = 0


# Keyboard event checker: called check_view because so far, all the keyboard inputs change the view by translation,
# dilation, or maybe soon rotation.
def check_view():
    global ctrl, translation, delta_translation, dilation, delta_dilation_iterator, trail_toggle

    for event in pygame.event.get():
        # If the 'X' in the top right corner is clicked.
        if event.type == pygame.QUIT:
            quit()

        # If a key is pressed.
        if event.type == pygame.KEYDOWN:
            if ctrl:
                if event.key == pygame.K_UP:
                    delta_dilation_iterator = DELTA_DILATION
                elif event.key == pygame.K_DOWN:
                    delta_dilation_iterator = -DELTA_DILATION
            else:
                if event.key == pygame.K_UP:
                    delta_translation[1] = 1
                elif event.key == pygame.K_DOWN:
                    delta_translation[1] = -1
                elif event.key == pygame.K_LEFT:
                    delta_translation[0] = 1
                elif event.key == pygame.K_RIGHT:
                    delta_translation[0] = -1
                elif event.key == pygame.K_SPACE:
                    trail_toggle = not trail_toggle
                elif event.key == pygame.K_LCTRL:
                    ctrl = 1
                    delta_translation = [0, 0]

        # If a key is lifted
        if event.type == pygame.KEYUP:
            if ctrl:
                if event.key == pygame.K_UP and delta_dilation_iterator != -DELTA_DILATION:
                    delta_dilation_iterator = 0
                elif event.key == pygame.K_DOWN and delta_dilation_iterator != DELTA_DILATION:
                    delta_dilation_iterator = 0
                elif event.key == pygame.K_LCTRL:
                    ctrl = 0
                    delta_dilation_iterator = 0
            else:
                if event.key == pygame.K_UP and delta_translation[1] != -1:
                    delta_translation[1] = 0
                elif event.key == pygame.K_DOWN and delta_translation[1] != 1:
                    delta_translation[1] = 0
                elif event.key == pygame.K_LEFT and delta_translation[0] != -1:
                    delta_translation[0] = 0
                elif event.key == pygame.K_RIGHT and delta_translation[0] != 1:
                    delta_translation[0] = 0


def translate():
    global translation, translation_old
    translation_old = translation
    translation = list(map(add, translation, delta_translation))


def dilate():
    global dilation, dilation_old, dilation_iterator
    dilation_iterator += delta_dilation_iterator
    dilation_old = dilation
    dilation = e ** dilation_iterator
