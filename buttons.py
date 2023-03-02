import pygame.font


class Button():
    def __init__(self, ai_game, rect, text, color, ratio, agle=0):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, self.settings.size_font)
        self.rect = rect
        self.button_color = color
        self.text = text
        self.ratio = ratio
        self.agle = agle
        if self.button_color == (0, 0, 0):
            self.color = 0
        elif self.button_color == (178, 34, 34):
            self.color = 1
        else:
            self.color = 3
        self.prep_msg()

    def prep_msg(self):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""

        self.msg_image = self.font.render(self.text,
                                          True,
                                          self.text_color,
                                          self.button_color)
        self.msg_image =pygame.transform.rotate(self.msg_image, self.agle)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)