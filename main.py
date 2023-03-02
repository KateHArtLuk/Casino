import pygame
import sys

from settings import Settings
from roulette import Roulette
from ball import Ball
from buttons import Button
from game_status import Game_status
from user import User
from information import Information


class Casino:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Casino")

        self.settings = Settings()
        self.stats = Game_status()
        self.clock = pygame.time.Clock()
        self.user = User()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.roulette = Roulette(self)
        self.ball = Ball(self)
        self.inf = Information(self)
        self.list_red_color = (32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3)
        self.gen_num_colors()
        self._create_buttons()

    def gen_num_colors(self):
        self.num_colors = []
        for num in range(1, 37):
            color = (178, 34, 34) if num in self.list_red_color else (0, 0, 0)
            self.num_colors.append((str(num), color))

    def run(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self.clock.tick(self.settings.FPS)
            self._check_events()
            if self.stats.active_ball:
                self.ball.update()
            if self.stats.active_roulette:
                self.roulette.update()
            if self.stats.need_chek_res and not self.stats.active_ball and not self.stats.active_roulette:
                self._chec_res()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not (self.stats.active_ball and self.stats.active_roulette):
                    self._chek_press_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        pass

    def _create_buttons(self):
        """Создаем кнопки"""
        self.buttons = []

        x0 = self.settings.buttons_first_indent_x
        y0 = self.settings.buttons_first_indent_y + self.roulette.rect.bottom

        for line in range(5):
            for column in range(14):
                x = x0 + column * (self.settings.buttons_width + self.settings.buttons_intermediate_indent_x)
                y = y0 + line * (self.settings.buttons_height + self.settings.buttons_intermediate_indent_y)
                c = 0

                if column == 0 and line == 0:
                    rect = pygame.Rect(x, y, self.settings.buttons_width,
                                       self.settings.buttons_height * 3 + self.settings.buttons_intermediate_indent_y * 2)
                    self.buttons.append(
                        Button(self,
                               rect=rect,
                               text='0',
                               color=(124, 252, 0),
                               ratio=35)
                    )

                elif column == 13 and line < 3:
                    if line == 0:
                        rect = pygame.Rect(x, y, self.settings.buttons_width, self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '1-34', color=(0, 128, 0), agle=90, ratio=3))
                    elif line == 1:
                        rect = pygame.Rect(x, y, self.settings.buttons_width, self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '2-35', color=(0, 128, 0), agle=90, ratio=3))
                    elif line == 2:
                        rect = pygame.Rect(x, y, self.settings.buttons_width, self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '3-36', color=(0, 128, 0), agle=90, ratio=3))


                elif line == 3 and column in (1, 5, 9):
                    if column == 1:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 4 + self.settings.buttons_intermediate_indent_x * 3,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '1-12', color=(0, 128, 0), agle=0, ratio=3))
                    elif column == 5:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 4 + self.settings.buttons_intermediate_indent_x * 3,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '13-24', color=(0, 128, 0), agle=0, ratio=3))
                    elif column == 9:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 4 + self.settings.buttons_intermediate_indent_x * 3,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '25-36', color=(0, 128, 0), agle=0, ratio=3))

                elif line == 4 and column in (1, 3, 5, 7, 9, 11):
                    if column == 1:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 2 + self.settings.buttons_intermediate_indent_x * 1,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '1-18', color=(0, 128, 0), agle=0, ratio=2))
                    elif column == 3:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 2 + self.settings.buttons_intermediate_indent_x * 1,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, 'четн', color=(0, 128, 0), agle=0, ratio=2))
                    elif column == 5:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 2 + self.settings.buttons_intermediate_indent_x * 1,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '', color=(178, 34, 34), agle=0, ratio=2))
                    elif column == 7:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 2 + self.settings.buttons_intermediate_indent_x * 1,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '', color=(0, 0, 0), agle=0, ratio=2))
                    elif column == 9:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 2 + self.settings.buttons_intermediate_indent_x * 1,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, 'не четн', color=(0, 128, 0), agle=0, ratio=2))
                    elif column == 11:
                        rect = pygame.Rect(x, y,
                                           self.settings.buttons_width * 2 + self.settings.buttons_intermediate_indent_x * 1,
                                           self.settings.buttons_height)
                        self.buttons.append(Button(self, rect, '19-36', color=(0, 128, 0), agle=0, ratio=2))

                elif line in (0, 1, 2) and 0 < column < 13:
                    text, color = self.num_colors[line + 3 * (column - 1)]
                    rect = pygame.Rect(x, y, self.settings.buttons_width,
                                       self.settings.buttons_height)
                    self.buttons.append(Button(self, rect, text, color=color, ratio=35))

    def _chec_res(self):
        ls = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9,
              22, 18, 29, 7, 28, 12, 35, 3, 26]
        agle_rul = self.roulette.agle
        agle_ball = self.ball.agle
        agle = agle_rul - agle_ball
        if agle < 0:
            agle = 360 + agle
        a = 360 / 37
        res = round(agle / a)
        if res == 37:
            res = 0
        print(f'Выпало: {ls[res]}')
        self._chek_win(ls[res])
        self.stats.need_chek_res = False

    def _chek_win(self, res_num):
        text, color, ratio = self.user.bet
        win = True
        if text.isdecimal() and int(text) == res_num:
            self.user.money += self.user.bet_money * ratio
        elif text == '1-12' and 0 < res_num < 13:
            self.user.money += self.user.bet_money * ratio
        elif text == '13-24' and 12 < res_num < 25:
            self.user.money += self.user.bet_money * ratio
        elif text == '25-36' and 24 < res_num < 37:
            self.user.money += self.user.bet_money * ratio
        elif text == '1-18' and 0 < res_num < 19:
            self.user.money += self.user.bet_money * ratio
        elif text == '19-36' and 18 < res_num < 37:
            self.user.money += self.user.bet_money * ratio
        elif text == 'четн' and res_num % 2 == 0:
            self.user.money += self.user.bet_money * ratio
        elif text == 'не четн' and res_num % 2 != 0:
            self.user.money += self.user.bet_money * ratio
        elif text == '1-34' and (res_num - 1) % 3 == 0:
            self.user.money += self.user.bet_money * ratio
        elif text == '2-35' and (res_num - 2) % 3 == 0:
            self.user.money += self.user.bet_money * ratio
        elif text == '3-36' and res_num % 3 == 0:
            self.user.money += self.user.bet_money * ratio
        elif text == '' and color == 1 and res_num in self.list_red_color:
            self.user.money += self.user.bet_money * ratio
        elif text == '' and color == 0 and res_num not in self.list_red_color:
            self.user.money += self.user.bet_money * ratio
        else:
            self.user.money -= self.user.bet_money
            win = False
        if win:
            print('Победа!')
        else:
            print('Проигрыш')
        print(f'Счет: {self.user.money}')
        self.inf.prep_score()

    def _chek_press_buttons(self, mouse_pos):
        """Проверяем нажание на кнопки"""
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                print(f'Ставка на: {button.text}')
                self.user.bet = (button.text, button.color, button.ratio)
                self.stats.active_roulette = True
                self.stats.active_ball = True
                self.stats.need_chek_res = True
                self.roulette.run()
                self.ball.run()
                break

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.roulette.blitme()
        self.ball.blitme()
        self.inf.show_score()
        for button in self.buttons:
            button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = Casino()
    ai.run()
