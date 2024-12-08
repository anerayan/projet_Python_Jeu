import pygame

class Unit:
    def __init__(self, x, y, nom, health, attack, defense, team, move_counter, competence):
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

    def move(self, dx, dy):
        """Déplace l'unité de dx et dy si possible."""
        if self.move_counter > 0:
            self.x += dx
            self.y += dy
           

    def attack(self, target):
        """Attaque une autre unité."""
        damage = max(0, self.attack - target.defense)
        target.health -= damage

    def competence_attack(self,target):
        return self.competence.attack(target,self)


    def draw(self, screen, images):
        """Affiche l'unité sur l'écran avec une image ou un cercle si l'image est manquante."""
        if self.nom.startswith("Homme de Cromagnon"):
            image = images.get("cromagnon")
        elif self.nom.startswith("Homme Futur"):
            image = images.get("homme_futur")
        else:
            image = images.get("anomaly")  # Image par défaut si le nom ne correspond pas

        if image:
            screen.blit(image, (self.x * 60, self.y * 60))
        else:
            color = (0, 0, 255) if self.team == 'player' else (255, 0, 0)
            if self.is_selected:
                pygame.draw.rect(screen, (0, 255, 0), (self.x * 60, self.y * 60, 60, 60))
            pygame.draw.circle(screen, color, (self.x * 60 + 30, self.y * 60 + 30), 20)