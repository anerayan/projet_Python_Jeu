# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:23:51 2024

@author: rayan
"""

import pygame
import random
from unit import Unit
from competences import competence

# Constantes pour la grille et la fenêtre
GRID_SIZE = 12
CELL_SIZE = 60  # Taille de chaque cellule
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

class Game:
    """
    Classe pour représenter le jeu.
    ...
    Attributs
    ---------
    screen: pygame.Surface
        La surface de la fenêtre du jeu.
    player_units : list[Unit]
        La liste des unités du joueur.
    enemy_units : list[Unit]
        La liste des unités de l'adversaire.
    """

    def __init__(self, screen):
        """
        Construit le jeu avec la surface de la fenêtre.

        Paramètres
        ----------
        screen : pygame.Surface
            La surface de la fenêtre du jeu.
        """
        self.screen = screen
        self.player_units = [
            Unit(0, 0, 'Soldat Joueur 1', 10, 2, 1, 'player', 3, competence(5, 0, 2)),
            Unit(1, 0, 'Soldat Joueur 2', 10, 2, 1, 'player', 3, competence(5, 0, 2))
        ]

        self.enemy_units = [
            Unit(6, 6, 'Soldat Ennemi 1', 8, 1, 1, 'enemy', 2, competence(3, 0, 1)),
            Unit(7, 6, 'Soldat Ennemi 2', 8, 1, 1, 'enemy', 2, competence(3, 0, 1))
        ]

    def handle_player_turn(self):
        """Tour du joueur"""
        for selected_unit in self.player_units:
            # Tant que l'unité n'a pas terminé son tour
            has_acted = False
            selected_unit.is_selected = True
            self.flip_display()
            while not has_acted:
                # Gestion des événements Pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        # Déplacement
                        dx, dy = 0, 0
                        if event.key == pygame.K_LEFT:
                            dx = -1
                        elif event.key == pygame.K_RIGHT:
                            dx = 1
                        elif event.key == pygame.K_UP:
                            dy = -1
                        elif event.key == pygame.K_DOWN:
                            dy = 1

                        selected_unit.move(dx, dy)
                        self.flip_display()

                        # Attaque
                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                    selected_unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)

                            has_acted = True
                            selected_unit.is_selected = False

    def handle_enemy_turn(self):
        """IA très simple pour les ennemis."""
        for enemy in self.enemy_units:
            # Déplacement aléatoire vers une unité du joueur
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

            # Attaque
            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)

    def flip_display(self):
        """Affiche le jeu."""
        self.screen.fill((0, 0, 0))
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)

        # Affiche les unités
        for unit in self.player_units + self.enemy_units:
            unit.draw(self.screen)

        # Rafraîchit l'écran
        pygame.display.flip()

def main():
    # Initialisation de Pygame
    pygame.init()

    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChronoTactics")

    # Instanciation du jeu
    game = Game(screen)

    # Boucle principale du jeu
    running = True
    while running:
        game.handle_player_turn()
        game.handle_enemy_turn()

    pygame.quit()

if __name__ == "__main__":
    main()
