# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:40:52 2024

@author: rayan
"""
import pygame

# Constantes
WIDTH, HEIGHT = 720, 720
BLACK, WHITE, GRAY, YELLOW = (0, 0, 0), (255, 255, 255), (100, 100, 100), (255, 255, 0)

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.selected_option = 0
        self.options = ["1 Player ", "2 Players ","Rules" ,"Quit"]

    def display_menu(self):
        """Affiche le menu principal."""
        self.screen.fill(BLACK)
        font_title = pygame.font.Font(None, 100)
        font_option = pygame.font.Font(None, 50)
        title_text = font_title.render("ChronoTactics", True, YELLOW)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 6))

        for i, option in enumerate(self.options):
            color = WHITE if i == self.selected_option else GRAY
            option_text = font_option.render(option, True, color)
            self.screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 + i * 70))

        pygame.display.flip()

    def handle_menu(self):
        """Gère la navigation dans le menu."""
        while True:
            self.display_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:  # Jouer
                            return "play"
                        elif self.selected_option == 1:  # Jouer à 2
                            print("Multijoueur - À implémenter.")
                        elif self.selected_option == 2: #afficher règle
                            print("Affichage règle du jeu")
                        elif self.selected_option == 3:  # Quitter
                            pygame.quit()
                            exit()

class ClassSelectionMenu:
    def __init__(self, screen):
        self.screen = screen
        self.selected_classes = [[], []]  # Une liste pour chaque joueur
        self.current_player = 0
        self.current_selection = 0  # Permet de savoir si c'est le premier ou le second choix
        self.classes = ["Cromagnon", "Homme Moderne", "Homme Futur"]
        self.selected_option = 0

    def display_menu(self):
        """Affiche le menu de sélection des classes."""
        self.screen.fill(BLACK)
        font_title = pygame.font.Font(None, 40)
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
                            print(self.selected_classes)
                            return self.selected_classes

    
class Menufinvictoire:

    def __init__(self, screen):
        self.screen = screen
        self.selected_option = 0
        self.options = ["1 Player ", "2 Players ","Rules" ,"Quit"]

    def display_menu(self):
        """Affiche le menu principal."""
        self.screen.fill(BLACK)
        font_title = pygame.font.Font(None, 100)
       
        title_text = font_title.render("YOU WIN !!!", True, YELLOW)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 6))

        
        pygame.display.flip()

class Menufindefaite:

    def __init__(self, screen):
        self.screen = screen
        self.selected_option = 0
        self.options = ["1 Player ", "2 Players ","Rules" ,"Quit"]

    def display_menu(self):
        """Affiche le menu principal."""
        self.screen.fill(BLACK)
        font_title = pygame.font.Font(None, 100)
       
        title_text = font_title.render("YOU'VE LOST !!!", True, YELLOW)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 6))

        
        pygame.display.flip()

from chronotactics import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChronoTactics")

    # Menu principal
    main_menu = Menu(screen)
    action = main_menu.handle_menu()

    if action == "play":
        # Menu de sélection des classes
        class_menu = ClassSelectionMenu(screen)
        selected_classes = class_menu.handle_menu()
        print(f"Classes choisies : {selected_classes}")

          # Passez les classes au jeu
       
       
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ChronoTactics")

       
        clock = pygame.time.Clock()
        
        game = Game(screen,selected_classes)
        
        
        

main()
