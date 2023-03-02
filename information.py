import pygame.font


class Information():
    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчета очков."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счета.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        self.money = self.ai_game.user.money
        rounded_score = round(self.money)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,
                                            True,
                                            self.text_color,
                                            self.settings.bg_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет на экран."""
        self.blit = self.screen.blit(self.score_image, self.score_rect)
        