import random
from imgManager import imgManager


class feedingManager:

    def __init__(self, screen, w, h):
        self.objs = []
        for i in range(3):
            chance = [0, 1]
            result = random.choice(chance)
            x = random.randint(20, w-20)
            y = h + 20

            if result == 0:
                self.objs.append(imgManager(screen, x, y, False, 'assets/fruits/bomb.png', 96 / 3, 96 / 3))
            elif result == 1:
                self.objs.append(imgManager(screen, x, y, False, 'assets/fruits/oran_berry.png', 96 / 3, 96 / 3))







