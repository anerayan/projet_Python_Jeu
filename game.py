# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:54:32 2024

@author: rayan
@author: anis
"""

# -*- coding: utf-8 -*-
"""
Game logic for ChronoTactics.
"""

# -*- coding: utf-8 -*-
"""
Game logic for ChronoTactics.
"""

import pygame
import random
import os
from unit import Unit

GRID_SIZE = 12
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.images = self.load_images()

        # Initialisation des unités avec esquive
        self.player_units = [
            Unit(0, 0, "Homme de Cromagnon", 10, 2, 1, "player", 3, None, 30),
            Unit(1, 0, "Homme de Cromagnon", 10, 2, 1, "player", 3, None, 30)
        ]
        self.enemy_units = [
            Unit(6, 6, "Homme Futur", 8, 1, 1, "enemy", 2, None, 20),
            Unit(7, 6, "Homme Futur", 8, 1, 1, "enemy", 2, None, 20)
        ]

    def load_images(self):
        base_path = os.path.join(os.path.dirname(__file__), 'images')
        images = {}
        try:
            images['cromagnon'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'cromagnon.png')), (CELL_SIZE, CELL_SIZE))
            images['homme_futur'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'homme_futur.png')), (CELL_SIZE, CELL_SIZE))
            images['anomaly'] = pygame.Surface((CELL_SIZE, CELL_SIZE))
            images['anomaly'].fill((255, 0, 0))
        except FileNotFoundError as e:
            print(f"Erreur : Fichier image manquant - {e.filename}")
            exit()
        return images

    def display_competence_zone(self, unit):
        """Affiche la zone de compétence autour d'une unité."""
        range_zone = unit.competence.range if unit.competence else 1  # Portée de la compétence
        for dx in range(-range_zone, range_zone + 1):
            for dy in range(-range_zone, range_zone + 1):
                x = unit.x + dx
                y = unit.y + dy
                if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.screen, (0, 0, 255), rect, 2)  # Zone en bleu

    def handle_player_turn(self):
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

                        # Gestion des déplacements
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

                        # Touche 'C' pour afficher la zone de compétence
                        if event.key == pygame.K_c:
                            self.display_competence_zone(selected_unit)
                            pygame.display.flip()

                        # Attaque normale
                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                    selected_unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)
                            has_acted = True
                            selected_unit.is_selected = False

                        # Validation du tour
                        if event.key == pygame.K_RETURN:
                            has_acted = True

    def handle_enemy_turn(self):
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
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

        for unit in self.player_units + self.enemy_units:
            unit.draw(self.screen, self.images)

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
