
"""
MenuHandler: Gérer le menu principal du jeu ChronoTactics
author anis
Ajout de Couleurses : Le titre est affiché en jaune et la sélection en gris pour une meilleure visibilité.
Options de Menu : Trois options sont maintenant disponibles : "Jouer", "Options" (pour des fonctionnalités futures), et "Quitter".
Navigation avec Flèches : Le joueur peut utiliser les flèches haut et bas pour naviguer dans le menu, et appuyer sur "Entrée" pour sélectionner une option.
"""

import pygame
import os
from menu_secondaire import MenuSecondaire

# Constantes
WIDTH = 1200  # Largeur de l'écran
HEIGHT = 800  # Hauteur de l'écran
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

MAIN_OPTIONS = ["Joueur 1", "Joueur 2", "Règles", "Quitter"]

class Menu:
    """
    Classe pour gérer le menu principal du jeu ChronoTactics.
    """
    def __init__(self, screen, background_image):
        self.screen = screen
        self.menu_active = True
        self.background_image = background_image
        self.selected_option = 0  # Option sélectionnée dans le menu

    def display_menu(self):
        """Affiche le menu principal."""
        self.screen.fill(BLACK)
        font_title = pygame.font.Font(None, 100)
        font_option = pygame.font.Font(None, 50)
        title_text = font_title.render("ChronoTactics", True, YELLOW)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 6))

        # Options du menu
        options = ["Jouer", "Options", "Quitter"]
        for i, option in enumerate(options):
            if i == self.selected_option:
                option_text = font_option.render(option, True, WHITE)
                background_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 50 + i * 70, 300, 50)
                pygame.draw.rect(self.screen, GRAY, background_rect)
            else:
                option_text = font_option.render(option, True, WHITE)

            self.screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 - 50 + i * 70))

        pygame.display.flip()

    def handle_menu(self):
        """Gestion de la navigation dans le menu."""
        while self.menu_active:
            self.display_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % 3
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % 3
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:  # Jouer
                            self.menu_active = False
                        elif self.selected_option == 1:  # Options (future expansion)
                            print("Options - Cette fonctionnalité sera implémentée plus tard.")
                        elif self.selected_option == 2:  # Quitter
                            pygame.quit()
                            exit()
    def show_rules(self):
    self.screen.fill(BLACK)
    font = pygame.font.Font(None, 50)
    rules_text = [
        "Règles du jeu ChronoTactics :",
        "1. Déplacez vos unités pour éliminer vos ennemis.",
        "2. Utilisez les portails temporels stratégiquement.",
        "3. Vainquez tous les ennemis pour gagner.",
    ]
    y_offset = HEIGHT // 4
    for line in rules_text:
        text = font.render(line, True, WHITE)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_offset))
        y_offset += 60
    pygame.display.flip()
    pygame.time.wait(5000)

    def select_option(self):
        """Exécute l'option sélectionnée."""
        if self.selected_option in [0, 1]:  # Joueur 1 ou Joueur 2
            menu_secondaire = MenuSecondaire(self.screen, self.background_image)
            menu_secondaire.handle_menu()
        elif self.selected_option == 2:  # Règles
            self.show_rules()
        elif self.selected_option == 3:  # Quitter
            pygame.quit()
            exit()


# Exemple d'utilisation du menu
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChronoTactics Menu")

     # Charger l'image de fond avec un chemin relatif
    current_dir = os.path.dirname(__file__)
    background_path = os.path.join(current_dir, "images", "background_menu.jpg")
    background_image = pygame.image.load(background_path)
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


    menu = Menu(screen)
    menu.handle_menu()
    print("Jeu démarré...")
    pygame.quit()
