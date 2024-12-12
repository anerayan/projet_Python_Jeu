# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:54:32 2024

@author: rayan
@author: anis
"""
import random
from abc import ABC, abstractmethod
class competence(ABC):
    def __init__(self, competence_power, competence_defense, portee, precision):
        self.competence_power = competence_power
        self.competence_defense = competence_defense
        self.portee = portee
        self.precision = precision 
    
    @abstractmethod
    def attack(self):
        pass

    
class fusil(competence):
    def __init__(self):
        super().__init__(18, 0, 8, 60)

        
    def attack(self,cibles,selected_unit):
        has_attacked = False
        """Exécute une attaque de compétence."""
        if random.randint(0, 100) <= self.precision:
            for cible in cibles:
                if abs(selected_unit.x - cible.x) <= self.portee and cible.y == selected_unit.y and has_attacked == False: 
                    damage = max(self.competence_power - cible.defense, 0)
                    cible.health -= damage
                    has_attacked == True
                    print(f"{selected_unit.nom} utilise une compétence sur {cible.nom}, infligeant {damage} dégâts.")
                if abs(selected_unit.y - cible.y) <= self.portee and cible.x == selected_unit.x and has_attacked == False: 
                    damage = max(self.competence_power - cible.defense, 0)
                    cible.health -= damage
                    has_attacked == True
                    print(f"{selected_unit.nom} utilise une compétence sur {cible.nom}, infligeant {damage} dégâts.")
        else:
            print(f"{selected_unit.nom} a manqué son attaque avec la compétence.")

class grenade(competence):
    
    def __init__(self):
        super().__init__(13, 0, 4, 75)

    def attack(self, cibles, selected_unit):
        """Applique des dégâts dans une zone autour de la cible."""
        zone_portee = 2  # Rayon de la zone d'effet
        print(f"💥 {selected_unit.nom} lance une grenade sur ses ennemis !")
        if random.randint(0, 100) <= self.precision:
            for cible in cibles:
                if abs(selected_unit.x - cible.x) <= self.portee and abs(selected_unit.y - cible.y) <= self.portee:
                    damage = max(self.competence_power - cible.defense, 0)
                    cible.health -= damage
                    print(f"{selected_unit.nom} utilise une compétence sur {cible.nom}, infligeant {damage} dégâts.")
        else:
            print(f"{selected_unit.nom} a manqué son attaque avec la compétence.")
        

class soin(competence):
    def __init__(self):
        super().__init__(0, 5, 0, 100)
        
    def attack(self,cibles,selected_unit):
        if selected_unit.health<=selected_unit.max_health-self.competence_defense:
            selected_unit.health+=self.competence_defense
            print(f"{selected_unit.nom} s'est soigné.")
    


