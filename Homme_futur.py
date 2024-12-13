# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:36:07 2024

@author: rayan
"""
import pygame 

from unit import Unit
from competences import fusil
class Homme_futur_player1(Unit):
    def __init__(self):
           
               """
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
               super().__init__(0,0,'Homme_futur_joueur_1',12,12,0,10,'player',5,fusil(),30)
    def shoot(self, screen, target_x, target_y):
        """Affiche un tir en direction de la cible."""
        pygame.draw.line(screen, (0, 255, 0), (self.x * 60 + 30, self.y * 60 + 30), (target_x, target_y), 5)

    def grenade(self, screen, target_x, target_y):
        """Affiche une explosion de grenade."""
        pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), 30)   

class Homme_futur_player2(Unit):
    def __init__(self):
           
               """
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
               super().__init__(10,11,'Homme_futur_joueur_2',12,12,0,8,'enemy',5,fusil(),30)
    def shoot(self, screen, target_x, target_y):
        """Affiche un tir en direction de la cible."""
        pygame.draw.line(screen, (0, 255, 0), (self.x * 60 + 30, self.y * 60 + 30), (target_x, target_y), 5)

    def grenade(self, screen, target_x, target_y):
        """Affiche une explosion de grenade."""
        pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), 30)
