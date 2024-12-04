import pygame
import random

# Constantes
GRID_SIZE = 12
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Unit:
    """
    Classe pour représenter une unité.

    ...
    Attributs
    ---------
    x : int
        La position x de l'unité sur la grille.
    y : int
        La position y de l'unité sur la grille.
    health : int
        La santé de l'unité.
    attack_power : int
        La puissance d'attaque de l'unité.
    team : str
        L'équipe de l'unité ('player' ou 'enemy').
    is_selected : bool
        Si l'unité est sélectionnée ou non.

    Méthodes
    --------
    move(dx, dy)
        Déplace l'unité de dx, dy.
    attack(target)
        Attaque une unité cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, nom ,health, attack_power, defense ,team,move_counter,competence):
        """
        Construit une unité avec une position, une santé, une puissance d'attaque et une équipe.

        Paramètres
        ----------
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        nom : str
            nom de l'unité'
        health : int
            La santé de l'unité.
        attack_power : int
            La puissance d'attaque de l'unité.
        defense : int
            La défense de l'unité
        team : str
            L'équipe de l'unité ('player' ou 'enemy').
        move_counter : int
            nb de pas que l'unité peut faire'
        competence : str
            nom de la competence qu'utilise l'unité
        """
        self.x = x
        self.y = y
        self.nom = nom
        self.health = health
        self.attack_power = attack_power
        self.team = team# 'player' ou 'enemy'
        self.is_selected = False
        self.defense = defense
        self.move_counter = move_counter
        self.competence = competence
    def move(self, dx, dy):
        """Déplace l'unité de dx, dy."""
        
        if 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE:
            self.x += dx
            self.y += dy
          
    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power-target.defense

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        color = BLUE if self.team == 'player' else RED
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE //
                           2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
    
    
    
    def display_health(self):
        print(f"l'unité {self.nom}possède encore {self.health} points de vie.")
    
    def attack_competence(self,target):
        self.competence.attaque(target,self)

    def display_death(self):
        print(f"L'unité {self.nom} est tombé au combat.")
    