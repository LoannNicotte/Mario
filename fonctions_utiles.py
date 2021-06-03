# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:39:02 2021

@author: loann
"""

import pygame
import images as img

def convert(x: int)-> int:
    return round(x * img.screen.get_width() / 1920)

def convert_plan(x: int)-> int:
    return round(x / img.screen.get_height() * 240)

def get_pos_screen(x: int)->int:
    return round(x*16 / 240 *  img.screen.get_height())

def same_surf(surf1: pygame.Surface, surf2: pygame.Surface)-> bool:
    if not (surf1.get_width() == surf2.get_width()) or not (surf1.get_height() == surf2.get_height()):
        return False
    else:
        array = pygame.surfarray.pixels2d(surf1) == pygame.surfarray.pixels2d(surf2)
        return (array.tolist() == [[True for i in range(surf1.get_height())] for j in range(surf1.get_width())])

def get_lvl_plan(lvl: tuple) -> list:
    if lvl == (1, 1):
        lvl = img.lvl_1_1
    plan = []
    for i in range(15):
        plan.append([])
        for j in range((lvl.get_width() // 16)):
            block = lvl.subsurface(16*j, 16*i, 16, 16)
            if same_surf(block, img.ground):
                plan[i].append("G")
            elif same_surf(block, img.lucky_block):
                plan[i].append("L")
            elif same_surf(block, img.breakable):
                plan[i].append("B")
            elif same_surf(block, img.unbreakable):
                plan[i].append("U")
            elif same_surf(block, img.pipe_top_left):
                plan[i].append("T")
            elif same_surf(block, img.pipe_top_right):
                plan[i].append("T")
            elif same_surf(block, img.pipe_left):
                plan[i].append("P")
            elif same_surf(block, img.pipe_right):
                plan[i].append("P")
            else:
                plan[i].append("-")

    return plan

def get_spawnpoint(lvl: tuple)-> tuple:
    if lvl == (1, 1):
        return (convert(365), convert(923))
