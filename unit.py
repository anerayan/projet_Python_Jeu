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

    def move(self, dx, dy):
        """Déplace l'unité de dx et dy si possible."""
        self.x += dx
        self.y += dy

    def attack(self, target):
        """Attaque une autre unité."""
        if random.randint(0, 100) < target.esquive:
            damage = max(0, (self.attaque - target.defense))
            target.health -= damage

    def draw(self, screen, images):
        """Affiche l'unité sur l'écran avec une image ou un cercle si l'image est manquante."""
        if self.nom == 'Homme de Cromagnon':
            image = images.get("cromagnon")
        elif self.nom == 'Homme Futur':
            image = images.get("homme_futur" 
        else:
            image = images.get("anomaly")  # Image par défaut si le nom ne correspond pas

        if image:
            screen.blit(image, (self.x * 60, self.y * 60))
    def draw_health_bar(self, screen):
           """Affiche une barre de vie au-dessus de l'unité."""
           bar_width = 50
           bar_height = 5
           fill = (self.health / 100) * bar_width
           pygame.draw.rect(screen, (255, 0, 0), (self.x * 60, self.y * 60 - 10, bar_width, bar_height))  # Barre rouge
           pygame.draw.rect(screen, (0, 255, 0), (self.x * 60, self.y * 60 - 10, fill, bar_height))  # Barre verte
