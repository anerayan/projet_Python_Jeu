# -*- coding: utf-8 -*-
"""
GraphicsHandler: Gérer les éléments graphiques du jeu ChronoTactics

Ce module contient des fonctions pour gérer le graphisme du jeu, incluant l'affichage des backgrounds,
des personnages, et des zones interactives.
Affichage d'une Image de Fond : J'ai ajouté la méthode display_background() pour afficher une image de fond (background_menu.jpg). Cela donne une dimension visuelle plus attrayante au jeu.

Superposition pour Lisibilité : J'ai intégré une superposition sombre (display_overlay()) pour améliorer la lisibilité des textes affichés au-dessus du fond, notamment en rendant le contraste plus agréable.

Affichage du Titre : La méthode display_title() permet d'afficher le titre du jeu au centre supérieur de l'écran. Cela est utile pour l'introduction et pour une présentation professionnelle.

Options de Menu : La méthode display_menu_options() affiche les différentes options du menu (comme "Jouer", "Options", "Quitter") et surligne l'option sélectionnée. L'option en surbrillance est entourée d'un rectangle bleu pour indiquer clairement la sélection en cours.

Mise à Jour de l'Écran : update_display() est utilisée pour actualiser l'écran après chaque changement, garantissant une interface fluide et réactive.
"""

import pygame
import os

# Constantes pour les dimensions et les couleurs
WIDTH = 800  # Largeur de l'écran
HEIGHT = 600  # Hauteur de l'écran
DARK_GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)


class GraphicsHandler:
    """
    Classe pour gérer les éléments graphiques du jeu ChronoTactics.
    """

    def __init__(self, screen):
        self.screen = screen
        # Chemin vers le dossier des images
        images_path = os.path.join(os.getcwd(), 'images')

        # Chargement des images avec gestion des erreurs
        try:
            self.background_image = pygame.image.load(os.path.join(images_path, 'background_menu.jpg'))
            self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
            self.cromagnon_image = pygame.image.load(os.path.join(images_path, 'cromagnon.png'))
            self.cromagnon_image = pygame.transform.scale(self.cromagnon_image, (60, 60))
            self.homme_futur_image = pygame.image.load(os.path.join(images_path, 'homme_futur.png'))
            self.homme_futur_image = pygame.transform.scale(self.homme_futur_image, (60, 60))
            self.portal_image = pygame.image.load(os.path.join(images_path, 'portal.png'))
            self.portal_image = pygame.transform.scale(self.portal_image, (60, 60))
            self.anomaly_image = pygame.image.load(os.path.join(images_path, 'anomaly.png'))
            self.anomaly_image = pygame.transform.scale(self.anomaly_image, (60, 60))
        except FileNotFoundError as e:
            print(f"Erreur : Fichier non trouvé - {e.filename}. Assurez-vous que le fichier est présent dans le dossier 'images'.")
            exit()

    def display_background(self):
        """Affiche l'image de fond."""
        self.screen.blit(self.background_image, (0, 0))

    def display_overlay(self):
        """Affiche une superposition sombre pour améliorer la lisibilité du texte."""
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(DARK_GRAY)
        self.screen.blit(overlay, (0, 0))

    def display_title(self, title_text):
        """Affiche le titre du jeu."""
        font_title = pygame.font.Font(None, 100)
        title_surface = font_title.render(title_text, True, YELLOW)
        self.screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 6))

    def display_menu_options(self, options, selected_option):
        """Affiche les options du menu."""
        font_option = pygame.font.Font(None, 50)
        for i, option in enumerate(options):
            if i == selected_option:
                option_text = font_option.render(option, True, BLACK)
                background_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 50 + i * 70, 300, 50)
                pygame.draw.rect(self.screen, BLUE, background_rect)
            else:
                option_text = font_option.render(option, True, WHITE)

            self.screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 - 50 + i * 70))

    def display_character(self, character_type, position):
        """Affiche un personnage à une position donnée.

        Args:
            character_type (str): Le type de personnage à afficher ('cromagnon' ou 'homme_futur').
            position (tuple): Coordonnées (x, y) de l'endroit où afficher le personnage.
        """
        if character_type == 'cromagnon':
            self.screen.blit(self.cromagnon_image, position)
        elif character_type == 'homme_futur':
            self.screen.blit(self.homme_futur_image, position)

    def display_special_zone(self, zone_type, position):
        """Affiche une zone spéciale (portail ou anomalie) à une position donnée.

        Args:
            zone_type (str): Le type de zone à afficher ('portal' ou 'anomaly').
            position (tuple): Coordonnées (x, y) de l'endroit où afficher la zone.
        """
        if zone_type == 'portal':
            self.screen.blit(self.portal_image, position)
        elif zone_type == 'anomaly':
            self.screen.blit(self.anomaly_image, position)

    def update_display(self):
        """Met à jour l'affichage de l'écran."""
        pygame.display.flip()


# Exemple d'utilisation du GraphicsHandler
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChronoTactics Graphics")

    graphics = GraphicsHandler(screen)
    graphics.display_background()
    graphics.display_overlay()
    graphics.display_title("ChronoTactics")
    graphics.display_menu_options(["Jouer", "Options", "Quitter"], 0)
    # Exemple d'affichage de personnages et zones spéciales
    graphics.display_character('cromagnon', (100, 300))
    graphics.display_character('homme_futur', (200, 300))
    graphics.display_special_zone('portal', (300, 400))
    graphics.display_special_zone('anomaly', (400, 400))
    graphics.update_display()

    # Attendre quelques secondes pour visualiser le résultat
    pygame.time.wait(5000)
    pygame.quit()
