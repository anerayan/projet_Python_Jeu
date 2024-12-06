# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:23:51 2024

@author: rayan
@author: anis
"""

import pygame
import random
from unit import Unit

# Constantes de la grille
GRID_SIZE = 12
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    """
    Classe pour représenter le jeu.
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
        self.images = self.load_images()
        self.player_units = [
            Unit(0, 0, "Homme de Cromagnon", 10, 2, 1, "player", 3, None),
            Unit(1, 0, "Homme de Cromagnon", 10, 2, 1, "player", 3, None)
        ]
        self.enemy_units = [
            Unit(6, 6, "Homme Futur", 8, 1, 1, "enemy", 2, None),
            Unit(7, 6, "Homme Futur", 8, 1, 1, "enemy", 2, None)
        ]

    def load_images(self):
        """Charge les images nécessaires au jeu."""
        base_path = "images"  # Changez le chemin si nécessaire
        images = {
            "cromagnon": pygame.transform.scale(pygame.image.load(f"{base_path}/cromagnon.png"), (CELL_SIZE, CELL_SIZE)),
            "homme_futur": pygame.transform.scale(pygame.image.load(f"{base_path}/homme_futur.png"), (CELL_SIZE, CELL_SIZE)),
            "anomaly": pygame.Surface((CELL_SIZE, CELL_SIZE))  # Image de secours
        }
        images["anomaly"].fill((255, 0, 0))
        return images

    def handle_player_turn(self):
        """Gère le tour du joueur."""
        for selected_unit in self.player_units:
            has_acted = False
            selected_unit.is_selected = True
            self.flip_display()
            while not has_acted:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
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

                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                    selected_unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)

                            has_acted = True
                            selected_unit.is_selected = False

    def handle_enemy_turn(self):
        """IA simplifiée pour les ennemis."""
        for enemy in self.enemy_units:
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)

    def flip_display(self):
        """Affiche l'état actuel du jeu."""
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

        for unit in self.player_units + self.enemy_units:
            unit.draw(self.screen, self.images)  # Passe self.images ici

        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChronoTactics")

    game = Game(screen)

    while True:
        game.handle_player_turn()
        game.handle_enemy_turn()

if __name__ == "__main__":
    main()
