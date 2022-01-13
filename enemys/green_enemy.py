import pygame
from Constants import RED_ENEMY_IMG, BULLET_IMG, GREEN, RED, FONT, HEIGHT, WIDTH, GREEN_ENEMY_IMG
from enemys.bullets import Bullet


class GreenEnemy:
    WIDTH = 30
    HEIGHT = 40
    VEL = 1

    def __init__(self, level, win, x, y):
        self.level = level
        self.win = win
        self.y = y

        self.x = x

        self.health = 10
        self.health_maximum = 10
        self.height = GREEN_ENEMY_IMG.get_height()
        self.width = GREEN_ENEMY_IMG.get_width()
        self.y_c = self.y
        self.name = "green"

    def healthbar(self):
        img_width = RED_ENEMY_IMG.get_width()
        pygame.draw.rect(self.win, RED, (self.x, self.y - 10, img_width, 10))
        pygame.draw.rect(self.win, GREEN, (self.x, self.y - 10, round(img_width / self.health_maximum * self.health), 10))
        self.get_hit()

    def move(self):
        self.y += 1

    def get_hit(self):
        pass

    def shoot(self):
        pass

    def get_bullet_mask(self):
        return pygame.mask.from_surface(BULLET_IMG)

    def get_enemy_mask(self):
        return pygame.mask.from_surface(GREEN_ENEMY_IMG)

    def draw(self):
        self.win.blit(GREEN_ENEMY_IMG, (self.x, self.y))
        self.healthbar()

    def game_over(self):
        victory = FONT.render("Game Over", True, RED)
        self.win.blit(victory, (WIDTH // 2 - victory.get_width() // 2, HEIGHT // 2 - victory.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)





