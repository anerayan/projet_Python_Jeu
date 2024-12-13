# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:19:46 2024

@author: rayan
"""
from unit import Unit
from competences import soin
class Homme_Cromagnon_player1(Unit):
    #unité du passé
   
    def __init__(self) :
        """
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        nom : str
            nom de l'unité'
        health : int
            La santé de l'unité.
        max_health : int
            Vie max de l'unité
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
        esquive : int
            precision d'attaque
        """
        super().__init__(0,1,'Homme de Cromagnon_joueur_1',20,20,13,10,'player',7,soin(),30)
    
    
    
 
    
class Homme_Cromagnon_player2(Unit):
    #unité du passé
   
    def __init__(self) :
        """
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        nom : str
            nom de l'unité'
        health : int
            La santé de l'unité.
        max_health : int
            Vie max de l'unité
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
        super().__init__(11,11,'Homme de Cromagnon_joueur_2',20,20,13,10,'enemy',7,soin(),30)
        
        

        
         