# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:34:23 2024

@author: rayan
"""
from unit import Unit
from competences import grenade
class Homme_moderne_player1(Unit):
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
            super().__init__(0,1,'Homme_moderne_joueur_1',15,8,9,'player',9,grenade(),70)
    

class Homme_moderne_player2(Unit):
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
            super().__init__(8,7,'Homme_moderne_joueur_2',15,8,9,'Enemy',9,grenade(),70)
       