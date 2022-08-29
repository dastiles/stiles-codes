class Knight(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.type = 'Knight'
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return "Type: {0}\n" \
            "Life: {1}\n" \
            "Speed: {2}\n" \
            "Attack Power: {3}\n" \
            "Attack Range: {4}\n" \
            "Weapon: {5}".format(self.type,
                                 self.life, self.speed, self.attack_power, self.attack_range, self.weapon)


class Archer(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.type = 'Archer'
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return "Type: {0}\n" \
            "Life: {1}\n" \
            "Speed: {2}\n" \
            "Attack Power: {3}\n" \
            "Attack Range: {4}\n" \
            "Weapon: {5}".format(
                self.type,
                self.life, self.speed, self.attack_power, self.attack_range, self.weapon)


class Barracks(object):
    def generate_knight(self):
        return Knight(400, 5, 3, 1, "short sword")

    def generate_archer(self):
        return Knight(800, 3, 2, 4, "bow and arrows")


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer = barracks.generate_archer()
    print("[Knight] {}".format(knight1))
    print("[Archer] {}".format(archer))
