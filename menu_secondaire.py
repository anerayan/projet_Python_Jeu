import pygame

# Constantes
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

SECONDARY_OPTIONS = ["Jouer", "Options", "Revenir"]

class MenuSecondaire:
    def __init__(self, screen, background_image):
        self.screen = screen
        self.background_image = background_image
        self.selected_option = 0
        self.menu_active = True

    def display_menu(self):
        """Affiche le sous-menu."""
        self.screen.blit(self.background_image, (0, 0))  # Affiche l'image de fond
        font_title = pygame.font.Font(None, 100)
        font_option = pygame.font.Font(None, 50)

        title_text = font_title.render("Menu Joueur", True, YELLOW)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 6))

        for i, option in enumerate(SECONDARY_OPTIONS):
            color = WHITE if i == self.selected_option else GRAY
            option_text = font_option.render(option, True, color)
            self.screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 2 - 50 + i * 70))

        pygame.display.flip()

    def handle_menu(self):
        """Gère la navigation dans le sous-menu."""
        while self.menu_active:
            self.display_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(SECONDARY_OPTIONS)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(SECONDARY_OPTIONS)
                    elif event.key == pygame.K_RETURN:
                        self.select_option()

    def select_option(self):
        """Exécute l'option sélectionnée."""
        if self.selected_option == 0:  # Jouer
            print("Le jeu commence...")
            self.menu_active = False
        elif self.selected_option == 1:  # Options
            self.show_options()
        elif self.selected_option == 2:  # Revenir
            self.menu_active = False  # Retour au menu principal

    def show_options(self):
        """Affiche les réglages de luminosité et de son."""
        running = True
        brightness = 50
        volume = 50

        while running:
            self.screen.blit(self.background_image, (0, 0))  # Affiche l'image de fond
            font = pygame.font.Font(None, 50)

            # Affiche les options
            brightness_text = font.render(f"Luminosité: {brightness}%", True, WHITE)
            volume_text = font.render(f"Son: {volume}%", True, WHITE)
            self.screen.blit(brightness_text, (WIDTH // 2 - brightness_text.get_width() // 2, HEIGHT // 3))
            self.screen.blit(volume_text, (WIDTH // 2 - volume_text.get_width() // 2, HEIGHT // 3 + 100))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and brightness < 100:
                        brightness += 10
                    elif event.key == pygame.K_DOWN and brightness > 0:
                        brightness -= 10
                    elif event.key == pygame.K_LEFT and volume > 0:
                        volume -= 10
                    elif event.key == pygame.K_RIGHT and volume < 100:
                        volume += 10
                    elif event.key == pygame.K_RETURN:  # Retour au menu secondaire
                        running = False
