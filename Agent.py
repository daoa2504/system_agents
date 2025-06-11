import random

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, env, visited):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        random.shuffle(directions)  # pour un peu d’aléa

        # Priorité aux cases non visitées et valides
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if env.is_valid_position(nx, ny) and (nx, ny) not in visited:
                self.x, self.y = nx, ny
                return

        # Si rien de mieux, déplacement aléatoire parmi les positions valides
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if env.is_valid_position(nx, ny):
                self.x, self.y = nx, ny
                return

    def get_position(self):
        return self.x, self.y
