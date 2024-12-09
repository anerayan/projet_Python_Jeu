# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:54:32 2024

@author: rayan
"""

class competence:
    
    def __init__(self,competence_power,competence_defense,portee):
        
        self.competence_power = competence_power
        self.competence_defense = competence_defense
        self.portee = portee 
        
        
    def attaque(self, cible,joueur):
        
        if self.portee>abs(cible.x-joueur.x) and cible.y == joueur.y: 
            cible.health -= self.competence_power-cible.defense
           # print(f"{self.nom} est utilisé sur {cible} avec une puissance de {self.puissance} !")
        elif self.portee>abs(cible.y-joueur.y) and cible.x == joueur.x :
            cible.health -= self.competence_power-cible.defense
            #print(f"{self.nom} est utilisé sur {cible} avec une puissance de {self.puissance} !")
            
         
    
    def methode_soin(self,joueur):
        if joueur.health<15:
            joueur.health+=self.competence_defense
        
class fusil(competence):
    def __init__(self):
        
        super().__init__(18,0,8)

class grenade(competence):
    def __init__(self):
        
        super().__init__(13,0,4)

class soin(competence):
    def __init__(self):
        
        super().__init__(0,5,0)