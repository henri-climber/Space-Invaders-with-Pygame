import pygame

from enemys.red_enemy import RedEnemy
from enemys.green_enemy import GreenEnemy
from Constants import WIDTH, HEIGHT, WHITE, BG_IMG, RED_ENEMY_IMG, GREEN_ENEMY_IMG, YELLOW_ENEMY_IMG
from Home_menü.menu_constants import HOME_Play_HOVER_IMG, HOME_SHOP_HOVER_IMG, MENU_BG_IMG, HOME_LEVEL_HOVER_IMG, \
    HOME_LEVEL_SELECT_IMG, LELVEL1_HOVER_IMG, LELVEL2_HOVER_IMG, LELVEL3_HOVER_IMG, LELVEL4_HOVER_IMG, \
    LELVEL5_HOVER_IMG, \
    LELVEL6_HOVER_IMG, LELVEL7_HOVER_IMG, LELVEL8_HOVER_IMG, LELVEL9_HOVER_IMG
from Home_menü.Button import Button
from SpaceInvaders.Player import Player
from SpaceInvaders.level import Level
from SpaceInvaders.collision import Collision
from enemys.yellow_enemy import YellowEnemy
from enemys.dark_green_enemy import DarkGreenEnemy
import random

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# classes
level = 1
level_handler = Level()


def redraw_menuwindow(win, bg_img, home_screen=False):
    win.blit(bg_img, (0, 0))

    if home_screen:
        font = pygame.font.SysFont("Berlin Sans FB Demi", 100, True)
        level_text = font.render(f"Level: {level}", True, WHITE)
        win.blit(level_text, (880 // 2 - level_text.get_width() // 2, 270))

    pygame.display.update()


def menu(win):
    global level
    run = True

    home_screen = True
    level_screen = False

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if home_screen:
                    if Button(win).create_button(x, y, 320, 560, 425, 565):
                        redraw_menuwindow(win, HOME_Play_HOVER_IMG, home_screen=True)

                    elif Button(win).create_button(x, y, 300, 590, 750, 840):
                        redraw_menuwindow(win, HOME_SHOP_HOVER_IMG, home_screen=True)

                    elif Button(win).create_button(x, y, 335, 550, 600, 709):
                        redraw_menuwindow(win, HOME_LEVEL_HOVER_IMG, home_screen=True)

                    else:
                        redraw_menuwindow(win, MENU_BG_IMG, home_screen=True)
                if level_screen:
                    if Button(win).create_button(x, y, 76, 283, 353, 444):
                        redraw_menuwindow(win, LELVEL1_HOVER_IMG)

                    elif Button(win).create_button(x, y, 328, 549, 353, 444):
                        redraw_menuwindow(win, LELVEL2_HOVER_IMG)

                    elif Button(win).create_button(x, y, 584, 802, 353, 444):
                        redraw_menuwindow(win, LELVEL3_HOVER_IMG)

                    elif Button(win).create_button(x, y, 76, 283, 542, 641):
                        redraw_menuwindow(win, LELVEL4_HOVER_IMG)

                    elif Button(win).create_button(x, y, 328, 549, 542, 641):
                        redraw_menuwindow(win, LELVEL5_HOVER_IMG)

                    elif Button(win).create_button(x, y, 584, 802, 542, 641):
                        redraw_menuwindow(win, LELVEL6_HOVER_IMG)

                    elif Button(win).create_button(x, y, 76, 283, 749, 841):
                        redraw_menuwindow(win, LELVEL7_HOVER_IMG)

                    elif Button(win).create_button(x, y, 328, 549, 749, 841):
                        redraw_menuwindow(win, LELVEL8_HOVER_IMG)

                    elif Button(win).create_button(x, y, 584, 802, 749, 841):
                        redraw_menuwindow(win, LELVEL9_HOVER_IMG)

                    else:
                        redraw_menuwindow(win, HOME_LEVEL_SELECT_IMG)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if level_screen:
                    if Button(win).create_button(x, y, 75, 280, 350, 440):
                        home_screen = True
                        level_screen = False
                        level = 1

                    elif Button(win).create_button(x, y, 328, 549, 353, 444):
                        home_screen = True
                        level_screen = False
                        level = 2

                    elif Button(win).create_button(x, y, 584, 802, 353, 444):
                        home_screen = True
                        level_screen = False
                        level = 3

                    elif Button(win).create_button(x, y, 76, 283, 542, 641):
                        home_screen = True
                        level_screen = False
                        level = 4

                    elif Button(win).create_button(x, y, 328, 549, 542, 641):
                        home_screen = True
                        level_screen = False
                        level = 5

                    elif Button(win).create_button(x, y, 584, 802, 542, 641):
                        home_screen = True
                        level_screen = False
                        level = 6

                    elif Button(win).create_button(x, y, 76, 283, 749, 841):
                        home_screen = True
                        level_screen = False
                        level = 7

                    elif Button(win).create_button(x, y, 328, 549, 749, 841):
                        home_screen = True
                        level_screen = False
                        level = 8

                    elif Button(win).create_button(x, y, 584, 802, 749, 841):
                        home_screen = True
                        level_screen = False
                        level = 9

                elif home_screen:
                    if Button(win).create_button(x, y, 320, 560, 425, 565):
                        run = False
                    elif Button(win).create_button(x, y, 300, 590, 750, 840):
                        redraw_menuwindow(win, HOME_SHOP_HOVER_IMG)

                    elif Button(win).create_button(x, y, 335, 550, 600, 709):
                        redraw_menuwindow(win, HOME_LEVEL_SELECT_IMG)
                        home_screen = False
                        level_screen = True

    return True


def main(level):
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    shoot_loop = 0
    run = True
    enemy_list = level_handler.handle_level(level)
    enemys = []
    spaceshuttle = Player(750, 70, 70, 6, WIN)

    def redraw_gamewindow(win):
        win.blit(BG_IMG, (0, 0))
        spaceshuttle.draw()
        for enemy in enemys:
            enemy.draw()

        font = pygame.font.SysFont("comicsans", 50, True)
        level_text = font.render(f"Level: {level}", True, WHITE)
        win.blit(level_text, (10, 30))

        pygame.display.update()

    while run:
        pygame.init()
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        shoot_loop += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_LEFT] and spaceshuttle.x > spaceshuttle.vel:
            spaceshuttle.x -= spaceshuttle.vel
        elif keys[pygame.K_RIGHT] and spaceshuttle.x + spaceshuttle.vel + spaceshuttle.width < WIDTH:
            spaceshuttle.x += spaceshuttle.vel
        if keys[pygame.K_SPACE] and len(spaceshuttle.bullets) < 4:
            spaceshuttle.shoot(space=True)

        # level
        if len(enemy_list[1]) == 0 and len(enemys) == 0:
            spaceshuttle.victory()
            run = False
        elif len(enemy_list[1]) != 0:

            if enemy_list[1] and shoot_loop == enemy_list[2][0]:
                if enemy_list[1][0] == "red":
                    enemys.append(
                        RedEnemy(level, WIN, random.randint(0, WIDTH - RED_ENEMY_IMG.get_width()), 0))
                if enemy_list[1][0] == "yellow":
                    enemys.append(
                        YellowEnemy(level, WIN, random.randint(0, WIDTH - YELLOW_ENEMY_IMG.get_width()), 0))
                elif enemy_list[1][0] == "green":
                    enemys.append(GreenEnemy(level, WIN, random.randint(0, WIDTH - GREEN_ENEMY_IMG.get_width()),
                                             0))
                elif enemy_list[1][0] == "dark_green":
                    enemys.append(DarkGreenEnemy(level, WIN, random.randint(0, WIDTH - GREEN_ENEMY_IMG.get_width()),
                                                 0))

                enemy_list[1].pop(0)
                enemy_list[2].pop(0)
                shoot_loop = 0

        # enemy
        for enemy in enemys:
            if enemy.health <= 0:
                enemys.remove(enemy)
            if enemy.y + enemy.height > 900:
                enemy.game_over()
                run = False

            if enemy.name == "red" or enemy.name == "yellow":
                enemy.shoot()

                for bullet in enemy.bullets:
                    if Collision().collide(spaceshuttle.x, spaceshuttle.y, bullet.x, bullet.y,
                                           spaceshuttle.get_player_mask(), enemy.get_bullet_mask()):
                        spaceshuttle.health -= 1
                        enemy.bullets.remove(bullet)
                enemy.move()

            elif enemy.name == "green":
                if shoot_loop % 2 == 0:
                    enemy.move()

            elif enemy.name == "dark_green":
                enemy.move()
                enemy.move_loop += 1

            if Collision().collide(spaceshuttle.x, spaceshuttle.y, enemy.x, enemy.y,
                                   spaceshuttle.get_player_mask(),
                                   enemy.get_enemy_mask()):
                enemy.game_over()
                run = False

        # Player
        for bullet in spaceshuttle.bullets:
            for enemy in enemys:
                if Collision().collide(enemy.x, enemy.y, bullet.x - bullet.width // 2, bullet.y - bullet.height,
                                       enemy.get_enemy_mask(), bullet.get_player_bullet_mask()):
                    enemy.health -= 1
                    spaceshuttle.bullets.remove(bullet)
                    break

        spaceshuttle.shoot()
        redraw_gamewindow(WIN)
        pygame.display.update()
        if spaceshuttle.game_over():
            run = False


def runn(menu_play=True, main_play=False):
    if menu_play:
        if not menu(pygame.display.set_mode((880, 1125))):
            pygame.quit()
            return
        runn(menu_play=False, main_play=True)

    elif main_play:
        main(level)
        runn()


runn()
