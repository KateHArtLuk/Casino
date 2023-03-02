from random import randint

import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        """Инициализирует мяч и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.screen_rect = ai_game.screen.get_rect()
        self.first_image = pygame.image.load('images/ball.png')
        self.first_image = pygame.transform.scale(self.first_image,
                                                  (self.settings.roulette_width, self.settings.roulette_height))
        self.rect = self.first_image.get_rect()
        self.rect.x = self.screen_rect.x + 20
        self.rect.y = self.screen_rect.y + 20
        self.agle = 0
        # self.speed = 0
        self.blitme()

    def run(self):
        self.speed = randint(5, 50)
        # self.speed = 0

    def update(self):
        if self.speed > 0:
            self.agle = (self.agle - self.speed) % 360
            self.speed /= 1.01
        if self.speed < 0.3:
            self.speed = 0
            self.stats.active_ball = False

    def blitme(self):
        self.new_image = pygame.transform.rotate(self.first_image, self.agle)
        self.new_rect = self.new_image.get_rect()
        self.new_rect.center = self.rect.center
        self.screen.blit(self.new_image, self.new_rect)
