import pygame
from constants import *
from operator import add
from math import e

translation_old = [0, 0]
translation = [0, 0]
delta_translation = [0, 0]
dilation_index = 1
dilation_index_old = 1
delta_dilation_iterator = 0
dilation_iterator = 0
ctrl = 0


def check_view():
    global ctrl, translation, dilation_index, delta_dilation_iterator
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
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
                elif event.key == pygame.K_LCTRL:
                    ctrl = 1

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
    global dilation_index, dilation_index_old, dilation_iterator
    dilation_iterator += delta_dilation_iterator
    dilation_index_old = dilation_index
    dilation_index = e ** dilation_iterator
