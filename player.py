# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:14:13 2021

@author: loann
"""
import pygame
import images as img
import fonctions_utiles as FU

class Mario():
    def __init__(self, jeu, level):
        self.jeu = jeu
        self.level = level

        self.image = img.mario
        self.rect = self.image.get_rect()
        self.rect.bottomleft = FU.get_spawnpoint(level)
        self.direction = 1

        self.lvl_plan = FU.get_lvl_plan(self.level)

        self.speed = FU.convert(10)
        self.speedy = FU.convert(40)
        self.gravity = FU.convert(1.2)
        self.velocity = 0
        self.in_air = False

        self.on_flag = False

        self.no_clip = False


    def display(self):
        if self.rect.centerx < FU.convert(1600):
            self.jeu.screen.blit(self.image, self.rect.topleft)

    def update(self):
        if not self.jeu.level_finish:
            self.jeu.check_finish()
            if pygame.K_d in self.jeu.key_pressed or pygame.K_RIGHT in self.jeu.key_pressed:
                self.direction = 1
                if (not self.check_colide_right() or self.no_clip) and self.rect.right < self.jeu.screen.get_width() - 10:
                    if (self.rect.centerx < self.jeu.screen.get_width() / 2 or
                        img.bg_lvl_1_1.get_width() - self.jeu.screen.get_width() + self.jeu.pos_bg < 10):
                        self.rect.centerx += self.speed

                    else:
                        self.jeu.pos_bg -= self.speed

            if pygame.K_q in self.jeu.key_pressed or pygame.K_LEFT in self.jeu.key_pressed:
                self.direction = 0
                if (not self.check_colide_left() or self.no_clip) and self.rect.left > 10:
                    self.rect.centerx -= self.speed

            self.speed_sprint_crouch()

            if not self.no_clip:
                self.fall()



            if self.rect.top > self.jeu.screen.get_height() + 10:
                self.jeu.reset()

        else:
            if self.on_flag:
                if not self.check_colide_bottom():
                    self.rect.bottom += FU.convert(7)
                else:
                    self.on_flag = False

            elif self.rect.centerx < FU.convert(1600):
                self.rect.right += FU.convert(7)
                self.fall()

            elif not self.jeu.time_finish:
                self.jeu.time_finish = pygame.time.get_ticks()

            elif self.jeu.time_finish + 1000 < pygame.time.get_ticks():
                self.jeu.reset()



    def check_colide_bottom(self):
        x1 = FU.convert_plan(self.rect.left + abs(self.jeu.pos_bg))
        x2 = FU.convert_plan(self.rect.right + abs(self.jeu.pos_bg))
        y = FU.convert_plan(self.rect.bottom + 3)
        try:
            return (self.lvl_plan[y // 16][x1 // 16] != "-" or
                    self.lvl_plan[y // 16][x2 // 16] != "-")

        except:
            return False

    def check_colide_top(self):
        x1 = FU.convert_plan(self.rect.left + abs(self.jeu.pos_bg))
        x2 = FU.convert_plan(self.rect.right + abs(self.jeu.pos_bg))
        y = FU.convert_plan(self.rect.top)
        try:
            return (self.lvl_plan[y // 16][x1 // 16] != "-" or
                    self.lvl_plan[y // 16][x2 // 16] != "-")

        except:
            return False

    def check_colide_left(self):
        x = FU.convert_plan(self.rect.left + abs(self.jeu.pos_bg) - self.speed - 4)
        y1 = FU.convert_plan(self.rect.top) + 3
        y2 = FU.convert_plan(self.rect.centery)
        y3 = FU.convert_plan(self.rect.bottom) - 3
        try:
            return (self.lvl_plan[y1 // 16][x // 16] != "-" or
                    self.lvl_plan[y2 // 16][x // 16] != "-" or
                    self.lvl_plan[y3 // 16][x // 16] != "-")

        except:
            return False

    def check_colide_right(self):
        x = FU.convert_plan(self.rect.right + abs(self.jeu.pos_bg) + self.speed + 4)
        y1 = FU.convert_plan(self.rect.top) + 3
        y2 = FU.convert_plan(self.rect.centery)
        y3 = FU.convert_plan(self.rect.bottom) - 3
        try:
            return (self.lvl_plan[y1 // 16][x // 16] != "-" or
                    self.lvl_plan[y2 // 16][x // 16] != "-" or
                    self.lvl_plan[y3 // 16][x // 16] != "-")
        except:
            return False

    def fall(self):
        if not self.check_colide_bottom():
            self.in_air = True
            self.velocity += self.gravity
            self.velocity *= 0.95


        elif  0 < self.velocity < 30:
            self.velocity = 0
            self.in_air = False
            self.rect.bottom = FU.get_pos_screen(FU.convert_plan(self.rect.bottom + 2) // 16)

        else:
            self.in_air = False

        if self.check_colide_top() and self.velocity < 0:
            self.velocity = 0


        self.rect.bottom += int(self.velocity)

    def speed_sprint_crouch(self):
        if self.no_clip:
            if pygame.K_SPACE in self.jeu.key_pressed:
                self.rect.top -= FU.convert(10)

            elif pygame.K_LSHIFT in self.jeu.key_pressed:
                self.speed = FU.convert(17)

            elif pygame.K_LCTRL in self.jeu.key_pressed:
                self.rect.bottom += FU.convert(10)

            else:
                self.speed = FU.convert(10)

        else:
            if pygame.K_LSHIFT in self.jeu.key_pressed:
                self.speed = FU.convert(13)
                self.speedy = FU.convert(40)

            elif pygame.K_LCTRL in self.jeu.key_pressed:
                self.speed = FU.convert(7)
                self.speedy = FU.convert(28)

            else:
                self.speed = FU.convert(10)
                self.speedy = FU.convert(40)


    def jump(self):
        if not self.in_air and not self.no_clip:
            self.velocity -= self.speedy

    def reset(self):
        self.rect.bottomleft = FU.get_spawnpoint(self.level)
        self.on_flag = False

