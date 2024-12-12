import pygame
import random

class Unit:
    def __init__(self, x, y, nom, health, attaque, defense, team, move_counter, competence, esquive):
        self.x = x
        self.y = y
        self.nom = nom
        self.health = health
        self.attaque = attaque
        self.defense = defense
        self.team = team
        self.move_counter = move_counter
        self.competence = competence
        self.is_selected = False
        self.esquive = esquive

    def move(self, dx, dy, grid_size=12):
        """Déplace l'unité de dx et dy si elle reste dans les limites de la grille."""
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
            self.x = new_x
            self.y = new_y

    def attack(self, target):
        """Attaque une autre unité."""
        if random.randint(0, 100) >= target.esquive:
            damage = max(0, self.attaque - target.defense)
            target.health -= damage
            print(f"{self.nom} inflige {damage} dégâts à {target.nom}.")
        else:
            print(f"{self.nom} rate son attaque contre {target.nom}.")

    def draw(self, screen, images):
        """Affiche l'unité sur l'écran avec une image ou un cercle si l'image est manquante."""
        if self.nom == 'Homme de Cromagnon':
            image = images.get("cromagnon")
        elif self.nom == 'Homme Futur':
            image = images.get("homme_futur")
        else:
            image = images.get("anomaly")  # Image par défaut si le nom ne correspond pas

        if image:
            screen.blit(image, (self.x * 60, self.y * 60))
        else:
            pygame.draw.circle(screen, (255, 0, 0), (self.x * 60 + 30, self.y * 60 + 30), 30)

    def draw_health_bar(self, screen):
        """Affiche une barre de vie au-dessus de l'unité."""
        bar_width = 50
        bar_height = 5
        fill = (self.health / 100) * bar_width
        pygame.draw.rect(screen, (255, 0, 0), (self.x * 60, self.y * 60 - 10, bar_width, bar_height))  # Barre rouge
        pygame.draw.rect(screen, (0, 255, 0), (self.x * 60, self.y * 60 - 10, fill, bar_height))  # Barre verte

class Terrain:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.portals = self.generate_random_positions(2)
        self.anomalies = self.generate_random_positions(2)

    def generate_random_positions(self, count):
        """Génère des positions aléatoires uniques sur la grille."""
        positions = set()
        while len(positions) < count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            positions.add((x, y))
        return list(positions)

    def draw_terrain(self, screen):
        """Affiche les portails et anomalies sur l'écran."""
        for x, y in self.portals:
            pygame.draw.circle(screen, (0, 0, 255), (x * 60 + 30, y * 60 + 30), 20)  # Portail en bleu
        for x, y in self.anomalies:
            pygame.draw.circle(screen, (255, 165, 0), (x * 60 + 30, y * 60 + 30), 20)  # Anomalie en orange
