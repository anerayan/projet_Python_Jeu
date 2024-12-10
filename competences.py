# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:54:32 2024

@author: rayan
@author: anis
"""
import random

class competence:
    def __init__(self, competence_power, competence_defense, portee, precision):
        self.competence_power = competence_power
        self.competence_defense = competence_defense
        self.portee = portee
        self.precision = precision

    def attaque(self, cible, joueur, units=None):
        """Exécute une attaque de compétence."""
        if random.randint(0, 100) <= self.precision:
            damage = max(self.competence_power - cible.defense, 0)
            cible.health -= damage
            print(f"{joueur.nom} utilise une compétence sur {cible.nom}, infligeant {damage} dégâts.")
        else:
            print(f"{joueur.nom} a manqué son attaque avec la compétence.")

class fusil(competence):
    def __init__(self):
        super().__init__(18, 0, 8, 60)

class grenade(competence):
    def __init__(self):
        super().__init__(13, 0, 4, 75)

    def attaque(self, cible, joueur, units):
        """Applique des dégâts dans une zone autour de la cible."""
        zone_portee = 2  # Rayon de la zone d'effet
        print(f"💥 {joueur.nom} lance une grenade sur {cible.nom} !")

        for unit in units:
            if abs(unit.x - cible.x) <= zone_portee and abs(unit.y - cible.y) <= zone_portee:
                damage = max(self.competence_power - unit.defense, 0)
                unit.health -= damage
                print(f"💥 La grenade inflige {damage} à {unit.nom}. Santé restante : {unit.health}")

class soin(competence):
    def __init__(self):
        super().__init__(0, 5, 0, 100)
