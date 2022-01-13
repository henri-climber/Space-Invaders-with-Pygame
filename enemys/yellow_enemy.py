import pygame
from Constants import RED_ENEMY_IMG, BULLET_IMG, GREEN, RED, FONT, HEIGHT, WIDTH, YELLOW_ENEMY_IMG
from enemys.bullets import Bullet


class YellowEnemy:
    VEL = 1

    def __init__(self, level, win, x, y):
        self.level = level
        self.win = win
        self.y = y
        self.x = x

        self.shootloop = 0
        self.bullets = []
        self.reloading_time = 300
        self.health = 4
        self.health_maximum = 4
        self.height = RED_ENEMY_IMG.get_height()
        self.width = RED_ENEMY_IMG.get_width()
        self.name = "red"
        self.shoot_burst_time = 10

    def healthbar(self):
        img_width = RED_ENEMY_IMG.get_width()
        pygame.draw.rect(self.win, RED, (self.x, self.y - 10, img_width, 10))
        pygame.draw.rect(self.win, GREEN, (self.x, self.y - 10, round(img_width / self.health_maximum * self.health), 10))
        self.get_hit()

    def move(self):
        self.y += self.VEL

    def get_hit(self):
        pass

    def get_bullet_mask(self):
        return pygame.mask.from_surface(BULLET_IMG)

    def get_enemy_mask(self):
        return pygame.mask.from_surface(RED_ENEMY_IMG)

    def shoot(self):
        if self.shootloop == 0:
            self.bullets.append(Bullet(self.win, self.x + 30, self.y + 50, BULLET_IMG, 3))
            self.shootloop += 1
        elif self. shootloop == self.shoot_burst_time:
            self.bullets.append(Bullet(self.win, self.x + 30, self.y + 50, BULLET_IMG, 3))
            self.shootloop += 1
        elif self. shootloop == self.shoot_burst_time * 2:
            self.bullets.append(Bullet(self.win, self.x + 30, self.y + 50, BULLET_IMG, 3))
            self.shootloop += 1
        elif self. shootloop == self.shoot_burst_time * 3:
            self.bullets.append(Bullet(self.win, self.x + 30, self.y + 50, BULLET_IMG, 3))
            self.shootloop += 1
        elif self. shootloop == self.shoot_burst_time * 4:
            self.bullets.append(Bullet(self.win, self.x + 30, self.y + 50, BULLET_IMG, 3))
            self.shootloop += 1

        else:
            self.shootloop += 1
            if self.shootloop > self.reloading_time:
                self.shootloop = 0

    def draw(self):
        self.win.blit(YELLOW_ENEMY_IMG, (self.x, self.y))

        for bullet in self.bullets:
            bullet.draw()
            bullet.move()
            if bullet.y > HEIGHT:
                self.bullets.remove(bullet)
        self.healthbar()

    def game_over(self):
        victory = FONT.render("Game Over", True, RED)
        self.win.blit(victory, (WIDTH // 2 - victory.get_width() // 2, HEIGHT // 2 - victory.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)



