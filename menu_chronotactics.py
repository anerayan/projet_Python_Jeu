
"""
MenuHandler: Gérer le menu principal du jeu ChronoTactics
author anis
Ajout de Couleurses : Le titre est affiché en jaune et la sélection en gris pour une meilleure visibilité.
Options de Menu : Trois options sont maintenant disponibles : "Jouer", "Options" (pour des fonctionnalités futures), et "Quitter".
Navigation avec Flèches : Le joueur peut utiliser les flèches haut et bas pour naviguer dans le menu, et appuyer sur "Entrée" pour sélectionner une option.
"""

import pygame

# Constantes
WIDTH = 800  # Largeur de l'écran
HEIGHT = 600  # Hauteur de l'écran
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

class Menu:
    """
    Classe pour gérer le menu principal du jeu ChronoTactics.
    """
    def __init__(self, screen):
        self.screen = screen
        self.menu_active = True
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

# Exemple d'utilisation du menu
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChronoTactics Menu")

    menu = Menu(screen)
    menu.handle_menu()
    print("Jeu démarré...")
    pygame.quit()
