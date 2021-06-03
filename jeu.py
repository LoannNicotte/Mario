# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:39:12 2021

@author: loann
"""
import images as img
import fonctions_utiles as FU
import player
import pygame

class Jeu:
    def __init__(self):
        self.screen = img.screen
        self.clock = pygame.time.Clock()
        self.level = (1, 1)

        self.player = player.Mario(self, self.level)

        self.pos_bg = 0

        self.key_pressed = []

        self.level_flag = [(1, 1)]
        self.level_finish = False
        self.time_finish = None


    def display_background(self):
        self.screen.fill((107, 140, 255))
        self.screen.blit(img.bg_lvl_1_1, (self.pos_bg, 0))

    def display_entity(self):
        self.player.display()

    def update_entity(self):
        self.player.update()

    def display_fps(self):
        self.screen.blit(img.fps_font.render(f"{int(self.clock.get_fps())}", True, (0, 0, 0)), (2, 2))

    def display_all(self):
        self.display_background()
        self.display_entity()
        self.display_fps()

    def reset(self):
        self.player.reset()
        self.pos_bg = 0
        self.level_finish = False
        self.time_finish = None

    def check_finish(self):
        if self.level in self.level_flag:
            if self.player.rect.right > FU.convert(1160):
                self.level_finish = True
                self.player.on_flag = True
