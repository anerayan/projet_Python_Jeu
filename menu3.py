# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:45:15 2024

@author: rayan
"""

import pygame
import os
from chronotactics import Game 
# Constantes
WIDTH = 1200  # Largeur de l'écran
HEIGHT = 800  # Hauteur de l'écran
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)


class ClassSelectionMenu:
    def __init__(self, screen,background,choix):
        self.screen = screen
        self.selected_classes = [[], []]  # Une liste pour chaque joueur
        self.current_player = 0
        self.background = background
        self.choix = choix
        self.current_selection = 0  # Permet de savoir si c'est le premier ou le second choix
        self.classes = ["Cromagnon", "Homme Moderne", "Homme Futur"]
        self.selected_option = 0

    def display_menu(self):
        """Affiche le menu de sélection des classes."""
        self.screen.blit(self.background, (0, 0))
        font_title = pygame.font.Font(None, 60)
        font_option = pygame.font.Font(None, 40)
        title_text = font_title.render(
            f"Joueur {self.current_player + 1} : Choisissez la classe de l'unité {self.current_selection + 1}",
            True,
            YELLOW,
        )
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 6))

        for i, cls in enumerate(self.classes):
            color = WHITE if i == self.selected_option else GRAY
            option_text = font_option.render(cls, True, color)
            self.screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 + i * 70))

        pygame.display.flip()

    def handle_menu(self):
        """Gère la sélection des classes pour deux unités par joueur."""
        while True:
            self.display_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.classes)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.classes)
                    elif event.key == pygame.K_RETURN:
                        # Ajouter la classe sélectionnée pour le joueur en cours
                        self.selected_classes[self.current_player].append(self.classes[self.selected_option])
                        self.current_selection += 1

                        # Passer au joueur suivant si les deux choix sont faits
                        if self.current_selection == 2:
                            self.current_player += 1
                            self.current_selection = 0

                        # Si les deux joueurs ont fini leurs sélections, retourner les choix
                        if self.current_player == 2:


                            return self.selected_classes, self.choix

    
 # Suppose que le jeu est défini dans 'game.py'

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ChronoTactics")
        current_dir = os.path.dirname(__file__)
        background_path = os.path.join(current_dir, "images", "background_menu.jpg")
        background_image = pygame.image.load(background_path)
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
   
    
        # Menu de sélection des classes
        class_menu = ClassSelectionMenu(screen,background_image,self.choix)
        selected_classes,choix = class_menu.handle_menu()
        print(f"Classes choisies : {selected_classes}")

        # Lancer le jeu avec les classes sélectionnées
        Game(screen, selected_classes,choix)  # Passe les classes au jeu
        

        pygame.quit()

       
