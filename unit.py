import pygame
import random
class Unit:
    def __init__(self, x, y, nom, health, attack, defense, team, move_counter, competence,esquive):
        """
        Initialise une unité.

        Paramètres
        ----------
        x : int
            Coordonnée x sur la grille.
        y : int
            Coordonnée y sur la grille.
        nom : str
            Nom de l'unité.
        health : int
            Points de vie de l'unité.
        attack : int
            Valeur d'attaque de l'unité.
        defense : int
            Valeur de défense de l'unité.
        team : str
            Équipe de l'unité ('player' ou 'enemy').
        move_counter : int
            Nombre de déplacements possibles.
        competence : object
            Compétence spéciale de l'unité.
        esquive : int
            Statistique d'esquive de l'unité
        """
        self.x = x
        self.y = y
        self.nom = nom
        self.health = health
        self.attack = attack
        self.defense = defense
        self.team = team
        self.move_counter = move_counter
        self.competence = competence
        self.is_selected = False
        self.esquive = esquive
    def move(self, dx, dy):
        """Déplace l'unité de dx et dy si possible."""
        if self.move_counter > 0:
            self.x += dx
            self.y += dy
           

    def attack(self, target):
        """Attaque une autre unité."""
        if random.randint(0,100)<self.esquive:
            
            damage = max(0, self.attack - target.defense)
            target.health -= damage

    def competence_attack(self,target):
        if random.randint(0,100)<self.esquive:    
            return self.competence.attack(target,self)


    def draw(self, screen, images):
        """Affiche l'unité sur l'écran avec une image ou un cercle si l'image est manquante."""
        if self.nom == 'Homme de Cromagnon_joueur_1' or self.nom == 'Homme de Cromagnon_joueur_2' :
            image = images.get("cromagnon")
        elif self.nom == 'Homme_moderne_joueur_1' or self.nom == 'Homme_moderne_joueur_2' :
            image = images.get("homme_moderne")
        elif self.nom == 'Homme_futur_joueur_1' or self.nom == 'Homme_futur_joueur_2' :
            image = images.get("homme_futur")
        else:
            image = images.get("anomaly")  # Image par défaut si le nom ne correspond pas

        if image:
            screen.blit(image, (self.x * 60, self.y * 60))
        else:
            color = (0, 0, 255) if self.team == 'player' else (255, 0, 0)
            if self.is_selected:
                pygame.draw.rect(screen, (0, 255, 0), (self.x * 100, self.y * 100, 70, 70))
            pygame.draw.circle(screen, color, (self.x * 60 + 30, self.y * 60 + 30), 20)