# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:35:06 2021

@author: loann
"""

import pygame
import jeu

play = True
game = jeu.Jeu()
plan = game.player.lvl_plan

while play:
    game.clock.tick(60)
    pygame.display.update()
    game.display_all()
    game.update_entity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        elif event.type == pygame.KEYDOWN:
            if event.key not in game.key_pressed:
                game.key_pressed.append(event.key)

            if event.key == pygame.K_ESCAPE:
                play = False

            if event.key == pygame.K_SPACE:
                game.player.jump()

            if event.key == pygame.K_m:
                game.player.no_clip = not game.player.no_clip

        elif event.type == pygame.KEYUP:
            if event.key in game.key_pressed:
                game.key_pressed.remove(event.key)

pygame.quit()
