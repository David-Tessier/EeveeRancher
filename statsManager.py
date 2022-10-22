

class stats:
    def __init__(self, value, playerEevee, status, dirt, hunger, health):
        self.dirt = dirt
        self.hunger = hunger
        self.status = status
        self.health = health

        if value == 'hunger':
            hunger = playerEevee.hunger
            hunger += 1
            if 0 <= self.hunger <= 24:
                self.status = 4
            elif self.hunger >= 25 and status == 4:
                self.status = 3
            elif self.hunger >= 50 and status == 3:
                self.status = 2
            elif self.hunger >= 75 and status == 2:
                self.status = 1
            elif self.hunger >= 100 and status == 1:
                self.status = 0

        elif value == 'dirt':

            if 0 <= self.dirt <= 24:
                self.status = 4
            elif self.dirt >= 25 and status == 4:
                self.status = 3
            elif self.dirt >= 50 and status == 3:
                self.status = 2
            elif self.dirt >= 75 and status == 2:
                self.status = 1
            elif self.dirt >= 100 and status == 1:
                self.status = 0

        elif value == 'health':
            if self.health  >= 100:
                self.status = 4
            elif self.health  <= 100 and status == 4:
                self.status = 3
            elif self.health  <= 75 and status == 3:
                self.status = 2
            elif self.health  <= 50 and status == 2:
                self.status = 1
            elif self.health  <= 25 and status == 1:
                self.status = 0
