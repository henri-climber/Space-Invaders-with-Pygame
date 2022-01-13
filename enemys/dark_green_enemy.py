import pygame
from Constants import RED_ENEMY_IMG, BULLET_IMG, GREEN, RED, FONT, HEIGHT, WIDTH, DARK_GREEN_ENEMY_IMG
from enemys.bullets import Bullet
import random


class DarkGreenEnemy:
    VEL = 1

    def __init__(self, level, win, x, y):
        self.level = level
        self.win = win
        self.y = y
        self.x = x

        self.health = 4
        self.health_maximum = 4
        self.height = DARK_GREEN_ENEMY_IMG.get_height()
        self.width = DARK_GREEN_ENEMY_IMG.get_width()
        self.y_c = self.y
        self.name = "dark_green"
        self.move_loop = 0

    def healthbar(self):
        img_width = RED_ENEMY_IMG.get_width()
        pygame.draw.rect(self.win, RED, (self.x, self.y - 10, img_width, 10))
        pygame.draw.rect(self.win, GREEN, (self.x, self.y - 10, round(img_width / self.health_maximum * self.health), 10))

    def move(self):
        self.y += self.VEL
        if self.move_loop == 100:
            random_int = random.randint(0, 2)
            moving = random.randint(40, 60)
            if random_int == 1:
                if self.x + moving + self.width < WIDTH:
                    self.x += moving
                else:
                    self.x -= moving
            else:
                if self.x - moving > 0:
                    self.x -= moving
                else:
                    self.x += moving
            self.move_loop = 0

    def get_bullet_mask(self):
        return pygame.mask.from_surface(BULLET_IMG)

    def get_enemy_mask(self):
        return pygame.mask.from_surface(DARK_GREEN_ENEMY_IMG)

    def draw(self):
        self.win.blit(DARK_GREEN_ENEMY_IMG, (self.x, self.y))
        self.healthbar()

    def game_over(self):
        victory = FONT.render("Game Over", True, RED)
        self.win.blit(victory, (WIDTH // 2 - victory.get_width() // 2, HEIGHT // 2 - victory.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)





