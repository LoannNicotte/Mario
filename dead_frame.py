# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:32:45 2021

@author: Elève
"""


import pygame


import images as img


class Dead_frame(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface):
        assert isinstance(screen, pygame.Surface)
        super().__init__()
        self.mario = screen.get_rect()
        self.image = img.dead_frame
        self.source_image = img.dead_frame
        self.source_rect = self.source_image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = self.mario.center
        self.ratio = 1

    def new_ratio(self, ratio: float) -> None:
        assert 0 < ratio < 1 and isinstance(ratio, float)
        self.ratio *= ratio
        self.rect.w *= ratio
        self.rect.h *= ratio
        self.image = pygame.transform.scale(self.source_image, self.get_dim())
        self.rect.center = self.mario.center
        if self.rect.width < 5 or self.rect.h < 10:
            self.reset()

    def reset(self) -> None:
            self.ratio = 1
            self.rect = self.source_rect

    def get_dim(self) -> tuple:
        return (self.rect.width, self.rect.height)

    def __str__(self) -> str:
        return f"image : x = {self.x}; y = {self.y}; width = {self.rect.widht}; height = {self.rect.height}"

    def display(self, target_surf: pygame.Surface) -> None:
        assert isinstance(target_surf, pygame.Surface)
        target_surf.blit(self.image, self.rect)
        pygame.draw.rect(target_surf, img.BLACK, [0, 0, self.rect.x, target_surf.get_height()])
        pygame.draw.rect(target_surf, img.BLACK, [0, 0, target_surf.get_width(), self.rect.y])
        pygame.draw.rect(target_surf, img.BLACK,
                         [self.rect.right,
                          0, target_surf.get_width() - self.rect.right,
                          target_surf.get_height()])
        pygame.draw.rect(target_surf, img.BLACK,
                         [0,
                          self.rect.bottom,
                          target_surf.get_width(),
                          target_surf.get_height()])


if __name__ == "__main__":
    screen = img.screen
    run = True
    dead_frame_ = Dead_frame(screen)
    anim = False
    while run:
        screen.fill((20, 250, 250))
        if anim:
            dead_frame_.display(screen)
            dead_frame_.new_ratio(.99)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    anim = True
                elif event.key == pygame.K_ESCAPE:
                    run = False

                    pygame.quit()
