# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:36:07 2024

@author: rayan
"""


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
               super().__init__(0,0,'Homme_futur_joueur_1',12,0,10,'player',9,fusil(),80)
       

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
               super().__init__(7,8,'Homme_futur_joueur_2',12,0,10,'enemy',9,fusil(),80)