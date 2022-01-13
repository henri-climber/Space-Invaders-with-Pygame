import pygame


class Level:

    def __init__(self):
        pass

    def levl1(self):
        return [10, ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
                [100, 150, 100, 150, 100, 50, 100, 100, 100, 150]]

    def level2(self):
        return [14,
                ["green", "green", "green", "red", "red", "red", "green", "red", "red", "green", "red", "red", "red"],
                [100, 100, 150, 130, 150, 100, 180, 110, 110, 110, 150, 100, 150]]

    def level3(self):
        return [13,
                ["red", "red", "dark_green", "dark_green", "dark_green", "dark_green", "red", "red", "red",
                 "dark_green", "red", "dark_green", "red"],
                [10, 150, 150, 150, 100, 200, 100, 150, 110, 110, 10, 100, 50]]

    def level4(self):
        return [13,
                ["dark_green", "dark_green", "dark_green", "dark_green", "dark_green", "dark_green", "dark_green", "dark_green", "dark_green",
                 "dark_green", "dark_green", "dark_green", "dark_green"],
                [120, 130, 130, 130, 130, 130, 120, 120, 120, 120, 120, 120, 120]]

    def level5(self):
        return [16,
                ["green", "green", "green", "yellow", "yellow", "green", "yellow", "green", "green", "yellow",
                 "yellow", "yellow", "yellow", "green", "yellow", "yellow"],
                [10, 10, 10, 170, 80, 820, 200, 100, 150, 120, 120, 120, 120, 180, 120, 130]]

    def level6(self):
        return [16,
                ["red", "red", "red", "red", "green", "green", "yellow", "red", "red", "yellow",
                 "dark_green", "dark_green", "red", "red", "yellow", "dark_green"],
                [10, 30, 30, 30, 200, 50, 100, 100, 100, 150, 200, 100, 120, 80, 150, 150]]

    def level7(self):
        return [16,
                ["green", "green", "green", "green", "red", "red", "red", "red", "red", "yellow",
                 "yellow", "green", "red", "yellow", "yellow", "red"],
                [10, 50, 50, 50, 100, 120, 250, 100, 100, 150, 100, 100, 150, 100, 100, 100]]

    def level8(self):
        return [16,
                ["dark_green", "dark_green", "dark_green", "dark_green", "yellow", "red", "yellow", "red", "yellow", "yellow",
                 "dark_green", "green", "green", "red", "red", "red"],
                [10, 100, 100, 100, 220, 100, 100, 100, 100, 100, 100, 100, 150, 100, 100, 100]]

    def level9(self):
        return [16,
                ["green", "green", "red", "red", "red", "red", "yellow", "yellow", "yellow", "dark_green",
                 "dark_green", "dark_green", "green", "green", "yellow", "yellow", "yellow"],
                [10, 100, 100, 100, 100, 100, 150, 100, 100, 250, 100, 100, 100, 100, 100, 100, 100]]

    def handle_level(self, level):
        if level == 1:
            return self.levl1()
        elif level == 2:
            return self.level2()
        elif level == 3:
            return self.level3()
        elif level == 4:
            return self.level4()
        elif level == 5:
            return self.level5()
        elif level == 6:
            return self.level6()
        elif level == 7:
            return self.level7()
        elif level == 8:
            return self.level8()
        elif level == 9:
            return self.level9()

