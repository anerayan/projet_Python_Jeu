import pygame
import os
import random

def load_images():
    """Charge les images nécessaires au jeu."""
    base_path = os.path.join(os.path.dirname(__file__), 'images')
    images = {}
    try:
        images['background_menu'] = pygame.image.load(os.path.join(base_path, 'background_menu.jpg'))
        images['cromagnon'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'cromagnon.png')), (60, 60))
        images['homme_futur'] = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'homme_futur.png')), (60, 60))
        images['portal'] = pygame.image.load(os.path.join(base_path, 'portal.png'))
        images['anomaly'] = pygame.image.load(os.path.join(base_path, 'anomaly.png'))
    except FileNotFoundError as e:
        print(f"Erreur : {e}. Vérifiez que toutes les images sont présentes dans le dossier 'images'.")
        pygame.quit()
        exit()
    return images

class Menu:
    def __init__(self, screen, images):
        """
        Initialise le menu principal.

        Paramètres
        ----------
        screen : pygame.Surface
            La surface de l'écran de jeu.
        images : dict
            Dictionnaire contenant les images chargées.
        """
        self.screen = screen
        self.images = images
        self.options = ["1 Player", "2 Players", "Rules", "Quit"]
        self.selected_option = 0

    def display_menu(self):
        """Affiche le menu principal."""
        self.screen.blit(self.images['background_menu'], (0, 0))
        font = pygame.font.Font(None, 50)

        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (200, 200, 200)
            text = font.render(option, True, color)
            self.screen.blit(text, (200, 150 + i * 50))

        pygame.display.flip()

    def run(self):
        """Boucle principale du menu."""
        running = True
        while running:
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
                        return self.options[self.selected_option]

def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 480))
    pygame.display.set_caption("ChronoTactics")

    images = load_images()
    menu = Menu(screen, images)

    selected_option = menu.run()
    print(f"Option choisie : {selected_option}")

    pygame.quit()

if __name__ == "__main__":
    main()