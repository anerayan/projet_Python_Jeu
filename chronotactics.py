# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:12:14 2024

@author: rayan
"""

import pygame
import random
from unit import Unit
from Cromagnon import Homme_Cromagnon_player1, soin
from Homme_futur import Homme_futur_player1
from Normal import Homme_moderne_player1
from Cromagnon import Homme_Cromagnon_player2
from Normal import Homme_moderne_player2
from Homme_futur import Homme_futur_player2

#from menu_chronotactics import handle_menu
# Constantes
GRID_SIZE = 12
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

class Game:
    """
    Classe pour gérer le jeu ChronoTactics.
    """

    def __init__(self, screen,selected_classes,choix_joueur):
        
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
        self.screen = screen
        self.selected_classes = selected_classes
        self.player_units = selected_classes[0]
        self.enemy_units =  selected_classes[1]
        self.choix_joueur = choix_joueur
        if selected_classes[0][0] == 'Cromagnon':
            self.player_units[0] = Homme_Cromagnon_player1()
        if selected_classes[0][0] == 'Homme Futur':
            self.player_units[0] = Homme_futur_player1()   
        if selected_classes[0][0] == 'Homme Moderne':
            self.player_units[0] = Homme_moderne_player1()
        if selected_classes[0][1] == 'Cromagnon':
            self.player_units[1] = Homme_Cromagnon_player1()
        if selected_classes[0][1] == 'Homme Futur':
            self.player_units[1] = Homme_futur_player1()   
        if selected_classes[0][1] == 'Homme Moderne':
            self.player_units[1] = Homme_moderne_player1()


        if selected_classes[1][0] == 'Cromagnon':
            self.enemy_units[0] = Homme_Cromagnon_player2()
        if selected_classes[1][0] == 'Homme Futur':
            self.enemy_units[0] = Homme_futur_player2()
        if selected_classes[1][0] == 'Homme Moderne':
            self.enemy_units[0] = Homme_moderne_player2()
        if selected_classes[1][1] == 'Cromagnon':
            self.enemy_units[1] = Homme_Cromagnon_player2()
        if selected_classes[1][1] == 'Homme Futur':
            self.enemy_units[1] = Homme_futur_player2()
        if selected_classes[1][1] == 'Homme Moderne':
            self.enemy_units[1] = Homme_moderne_player2()
        
        print(self.player_units)
        self.portals = [(3, 3), (6, 1)]  # Portails temporels connectés
        self.anomalies = [(2, 2), (5, 5)]  # Cases ralentissantes
        self.main()
    def handle_player_turn(self):
        """Gestion du tour des joueurs."""
        for selected_unit in self.player_units:
            has_acted = False
            selected_unit.is_selected = True
            self.render()
            cpt_move = 0
            selected_unit.display_health()  
            while not has_acted:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        dx, dy = 0, 0
                        if cpt_move<selected_unit.move_counter:
                            if event.key == pygame.K_LEFT:
                                dx = -1
                            elif event.key == pygame.K_RIGHT:
                                dx = 1
                            elif event.key == pygame.K_UP:
                                dy = -1
                            elif event.key == pygame.K_DOWN:
                                dy = 1
                            
                   
                            
                        selected_unit.move(dx, dy)
                        cpt_move+=1
                        # Portail : téléportation
                        if (selected_unit.x, selected_unit.y) in self.portals:
                            self.teleport_unit(selected_unit)

                        # Anomalie : ralentissement
                        elif (selected_unit.x, selected_unit.y) in self.anomalies:
                            if selected_unit.move_counter>2:
                                selected_unit.move_counter -=1
                            
                            print(f"⚠️ {selected_unit.nom} ralentit à cause de l'anomalie temporelle !")
                            print(f"L'unité{selected_unit.nom} ne peut plus faire que {selected_unit.move_counter} pas !")
                        self.render()

                        # Touche espace pour attaquer
                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                    selected_unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)
                                    has_acted = True
                                        
                                    
                        #touche N pour valider le tour
                        if event.key == pygame.K_n:
                            has_acted = True
                         #touche ECHAP pour quitter le jeu   
                        if event.key == pygame.K_ESCAPE:
                            pygame.display.quit()
                            pygame.quit()
                        
                        #touche C pour utiliser une attaque de loin
                        if event.key == pygame.K_c:
                            
                            if selected_unit.nom == 'Homme de Cromagnon_joueur_1':
                                     soin.methode_soin(selected_unit.health)
                                     has_acted = True
                                
                            for enemy in self.enemy_units:
    
                                selected_unit.attack_competence(enemy)
                                if enemy.health <= 0:
                                    self.enemy_units.remove(enemy)
                                    
                            has_acted = True
                        
                        # #touche H pour se soigner:
                        # if event.key == pygame.K_h:
                        #     if selected_unit.nom == 'Homme de Cromagnon_joueur_1':
                        #         selected_unit.heal()
                        #         has_acted = True
                                
                    
                         
            selected_unit.is_selected = False
            
    def handle_enemy_turn(self):
        """Gestion du tour de l'ennemi."""
        for enemy in self.enemy_units:
            enemy.display_health()  
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    enemy.display_death()
                    self.player_units.remove(target)



    def handle_player_2_turn(self):
        """Gestion du tour des joueurs."""
        for selected_unit in self.enemy_units:
            has_acted = False
            selected_unit.is_selected = True
            self.render()
            cpt_move = 0
            selected_unit.display_health()  
            while not has_acted:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        dx, dy = 0, 0
                        if cpt_move<selected_unit.move_counter:
                            if event.key == pygame.K_LEFT:
                                dx = -1
                            elif event.key == pygame.K_RIGHT:
                                dx = 1
                            elif event.key == pygame.K_UP:
                                dy = -1
                            elif event.key == pygame.K_DOWN:
                                dy = 1
                            
                   
                            
                        selected_unit.move(dx, dy)
                        cpt_move+=1
                        # Portail : téléportation
                        if (selected_unit.x, selected_unit.y) in self.portals:
                            self.teleport_unit(selected_unit)

                        # Anomalie : ralentissement
                        elif (selected_unit.x, selected_unit.y) in self.anomalies:
                            if selected_unit.move_counter>2:
                                selected_unit.move_counter -=1
                            
                            print(f"⚠️ {selected_unit.nom} ralentit à cause de l'anomalie temporelle !")
                            print(f"L'unité{selected_unit.nom} ne peut plus faire que {selected_unit.move_counter} pas !")
                        self.render()

                        # Touche espace pour attaquer
                        if event.key == pygame.K_SPACE:
                            for enemy in self.enemy_units:
                                if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                    selected_unit.attack(enemy)
                                    if enemy.health <= 0:
                                        self.enemy_units.remove(enemy)
                                    has_acted = True
                                        
                                    
                        #touche N pour valider le tour
                        if event.key == pygame.K_n:
                            has_acted = True
                         #touche ECHAP pour quitter le jeu   
                        if event.key == pygame.K_ESCAPE:
                            pygame.display.quit()
                            pygame.quit()
                        
                        #touche C pour utiliser une attaque de loin
                        if event.key == pygame.K_c:
                            
                            if selected_unit.nom == 'Homme de Cromagnon_joueur_2':
                                     soin.methode_soin(selected_unit.health)
                                     has_acted = True
                                
                            for enemy in self.player_units:
    
                                selected_unit.attack_competence(enemy)
                                if enemy.health <= 0:
                                    self.enemy_units.remove(enemy)
                                    
                            has_acted = True
                        
                        # #touche H pour se soigner:
                        # if event.key == pygame.K_h:
                        #     if selected_unit.nom == 'Homme de Cromagnon_joueur_1':
                        #         selected_unit.heal()
                        #         has_acted = True
                                
                    
                         
            selected_unit.is_selected = False
        
        
    def teleport_unit(self, unit):
        """Téléporte une unité à un portail connecté."""
        print(f"🌀 {unit.team} traverse un portail temporel !")
        for portal in self.portals:
            if portal != (unit.x, unit.y):
                unit.x, unit.y = portal
                break

    def render(self):
        """Affiche l'état actuel du jeu."""
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

        # Portails
        for px, py in self.portals:
            pygame.draw.circle(self.screen, BLUE, (px * CELL_SIZE + CELL_SIZE // 2, py * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

        # Anomalies
        for ax, ay in self.anomalies:
            pygame.draw.circle(self.screen, ORANGE, (ax * CELL_SIZE + CELL_SIZE // 2, ay * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

        # Units
        for unit in self.player_units: 
            unit.draw(self.screen)
        
        for unit in self.enemy_units:
            unit.draw(self.screen)
           

        pygame.display.flip()
        
    def set_player_classes(self, choices):
        """
        Définit les classes des joueurs en fonction des choix faits dans le menu.
        """
        p1_class, p2_class = choices

    # Mappez les choix aux classes disponibles
        player_classes = [Homme_Cromagnon_player1, Homme_moderne_player1, Homme_futur_player1]
        enemy_classes = [Homme_Cromagnon_player2, Homme_moderne_player2, Homme_futur_player2]

    # Créez les unités des joueurs
        self.player_units = [player_classes[p1_class](), player_classes[p2_class]()]
        self.enemy_units = [enemy_classes[p1_class](), enemy_classes[p2_class]()]

    def main(self):
        while True:
            if self.enemy_units != [] and self.player_units != []:
                self.render()
                self.handle_player_turn()
                
            if self.enemy_units == []:
                print("Vous avez gagné !")
                pygame.quit()
                break
            if self.choix_joueur == 0:
                self.handle_enemy_turn()
            
            elif self.choix_joueur == 1:
                self.handle_player_2_turn()
            
            if self.player_units == []:
                #print("Vous avez perdu !")
                pygame.quit()
                break
                
            
    

 
