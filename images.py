# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:19:24 2021

@author: loann
"""

import pygame

pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1366, 768))
#screen = pygame.display.set_mode((1920, 1080))


def convert(x):
    return round(x * screen.get_width() / 1920)

lvl_1_1 = pygame.image.load("assets/levels/1/1.png").convert()
bg_lvl_1_1 = pygame.transform.scale(lvl_1_1, (round(lvl_1_1.get_width() * screen.get_height() / 240) , screen.get_height())).convert()

lucky_block = pygame.image.load("assets/blocks/lucky_block.png").convert()
breakable = pygame.image.load("assets/blocks/breakable.png").convert()
unbreakable = pygame.image.load("assets/blocks/unbreakable.png").convert()
ground = pygame.image.load("assets/blocks/ground.png").convert()
pipe_top_left = pygame.image.load("assets/blocks/pipe_top_left.png").convert()
pipe_top_right = pygame.image.load("assets/blocks/pipe_top_right.png").convert()
pipe_left = pygame.image.load("assets/blocks/pipe_left.png").convert()
pipe_right = pygame.image.load("assets/blocks/pipe_right.png").convert()
dead_frame = pygame.image.load("assets/dead_frame.png").convert_alpha()

BLACK = (0, 0, 0)

mario = pygame.transform.scale(pygame.image.load("assets/mario/tall/mario.png"), (convert(16 * screen.get_height() / 240), convert(32 * screen.get_height() / 240)))

fps_font = pygame.font.SysFont(None, 14)
