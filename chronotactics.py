# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:12:14 2024

@author: rayan
"""

import pygame
import random
import os

from Cromagnon import Homme_Cromagnon_player1
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
        self.images = self.load_images()
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
        self.anomalies = [(6, 6), (7, 7),(6,7),(7,6)] # Cases ralentissantes
        self.portals = self.generate_random_positions(5) # Portails temporels connectés
         
        self.main()
    
    def generate_random_positions(self,count):
        """Génère des positions aléatoires uniques sur la grille."""
        positions = set()
        while len(positions) < count:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if (x,y)!=(0,0) and (x,y) not in self.anomalies:
                positions.add((x, y))
        return list(positions)
    
    def display_competence_zone(self, unit):
        """Affiche la zone de compétence autour d'une unité."""
        range_zone = unit.competence.portee if unit.competence else 1  # Portée de la compétence
        for dx in range(-range_zone, range_zone + 1):
            for dy in range(-range_zone, range_zone + 1):
                x = unit.x + dx
                y = unit.y + dy
                if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.screen, (0, 0, 255), rect, 2)  # Zone en bleu
                    
    def handle_player_turn(self):
        """Gestion du tour des joueurs."""
        for selected_unit in self.player_units:
            has_acted = False
            selected_unit.is_selected = True
            self.render()
            cpt_move = 0
            #selected_unit.display_health()  
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
                                    print(enemy)
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
                          
                            selected_unit.competence.attack(self.enemy_units,selected_unit)
                            for enemy in self.enemy_units:
                                if enemy.health <= 0:
                                    self.enemy_units.remove(enemy)
                                    
                            has_acted = True
                        
                        if event.key == pygame.K_d:
                            self.display_competence_zone(selected_unit)
                           
                            
                                
                    
                         
            selected_unit.is_selected = False
            
    def handle_enemy_turn(self):
        """Gestion du tour de l'ennemi."""
        for enemy in self.enemy_units:
            #enemy.display_health()  
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
            #selected_unit.display_health()  
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
                            
                            selected_unit.competence.attack(self.enemy_units,selected_unit)
                            for enemy in self.enemy_units:
                                if enemy.health <= 0:
                                    self.enemy_units.remove(enemy)
                                    
                            has_acted = True
                        
                      
                                
                    
                         
            selected_unit.is_selected = False
        
        
    def teleport_unit(self, unit):
        """Téléporte une unité à un portail connecté."""
        print(f"🌀 {unit.team} traverse un portail temporel !")
        
        portal = self.portals[random.randint(0,len(self.portals)-1)]
        if portal != (unit.x, unit.y):
            unit.x, unit.y = portal
        else:
            portal = self.portals[random.randint(0,len(self.portals)-1)]
       

    def render(self):
        """Affiche l'état actuel du jeu."""
        self.screen.fill(BLACK)
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

        # Portails
        image = self.images.get("portal")
        for ax, ay in self.portals:
            self.screen.blit(image, (ax * 60, ay * 60))

        # Anomalies
        image = self.images.get("anomaly")
        for ax, ay in self.anomalies:
            self.screen.blit(image, (ax * 60, ay * 60))

        # Units
        for unit in self.player_units: 
            unit.draw(self.screen,self.images)
        
        for unit in self.enemy_units:
            unit.draw(self.screen,self.images)
           

        pygame.display.flip()
        

    def load_images(self):
        """Charge les images nécessaires au jeu."""
        base_path = os.path.join(os.path.dirname(__file__), 'images')
        images = {}
        try:
            images['background_menu'] = pygame.image.load(os.path.join(base_path, 'background_menu.jpg'))
            images['cromagnon'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'cromagnon.png')), (60, 60))
            images['homme_moderne'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'future_soldier.png')), (60, 60))
            images['homme_futur'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'homme_futur.png')), (60, 60))
            images['portal'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'portal.png')), (60, 60))
            images['anomaly'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'anomaly.png')), (60, 60))
        except FileNotFoundError as e:
            print(f"Erreur : {e}. Vérifiez que toutes les images sont présentes dans le dossier 'images'.")
            pygame.quit()
            exit()
        return images
    

    def main(self):
        self.images = self.load_images()
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
                
            
    


