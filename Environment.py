class Environment:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else []

    def is_valid_position(self, x, y):
        # Vérifie si la position est dans la grille et n'est pas un obstacle
        return (0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles)

    def add_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.obstacles.append((x, y))

    def get_obstacles(self):
        return self.obstacles
