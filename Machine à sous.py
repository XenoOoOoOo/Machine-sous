# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:54:19 2020

@author: martial
"""

import random 
import time
import math
import os

# on créer trois listes correspondants aux trois rouleaux avec des éléments coefficientés
premRouleau = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0]
deuxRouleau = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0]
troisRouleau = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0]
# un seul zero par liste


 
print("Bienvenue sur la machine à sous de Martial Dorian Et Jad !")
time.sleep(2)
print("Le but du jeu est de miser des jetons et d'esperer avoir les trois symboles de chaque rouleau identiques.")
time.sleep(3)
print("Voici les règles du jeu, si vous tombez sur une ligne composée de trois symboles identiques, alors vous multipliez votre mise par un coefficient qui est définie en fonction du symbole présent sur la ligne. Voici les coefficients :")
print("Ligne de 1, 2 ou 3 --> Mise multipliée par 2\nLigne de 4, 5 ou 6 --> Mise multipliée par 4\nLigne de 7, 8 ou 9 --> Mise multipliée par 7")
print("Ligne de 3 symboles différents --> La moitié de la mise est rendue\nLigne de 0 --> Le joueur gagne 500 jetons\nSinon les jetons misés vont à la banque... ")
time.sleep(5)

ecartBanque = 0
credit = int(input("Tout d'abord, combien de jetons avez-vous pour jouer ? : "))
time.sleep(1)
print()


print("              -----------------------------------------------------------")


# on créer la boucle prinipale infinie qui se répète à chaque partie jusqu'à ce que le joueur arrête ou n'ai plus de de jetons
while True :
    
    # On créer une boucle pour savoir si le nombre de jetons misés ne dépasse pas le crédit du joueur
    while True :
        jetonsMises = int(input("Combien de jetons voulez-vous miser pour cette partie ? : "))
        if jetonsMises > credit :
            print("Vous n'avez pas assez de jetons !")
            continue
        elif jetonsMises <= 0 :
            print("Vous ne pouvez pas miser moins de 1 jetons")
            continue
        else:
            break
        
    # on soustrait les jetons misés au crédit du joueur
    credit -= jetonsMises
    
    print("La machine se lance...")
    print()
    time.sleep(3)
    
    # ici on effectue le tirage dans chaque liste correspondant au rouleau et on supprime l'élément tiré de la liste
    tiragePremRouleau = random.choice(premRouleau)
    premRouleau.remove(tiragePremRouleau)
    tirageDeuxRouleau = random.choice(deuxRouleau)
    deuxRouleau.remove(tirageDeuxRouleau)
    tirageTroisRouleau = random.choice(troisRouleau)
    troisRouleau.remove(tirageTroisRouleau)
    
    print("Symbole premier rouleau ... :", tiragePremRouleau)
    time.sleep(1)
    print("Symbole deuxième rouleau... :", tirageDeuxRouleau)
    time.sleep(1)
    print("Symbole troisième rouleau... :", tirageTroisRouleau)
    print()
    time.sleep(2)
    
    # ici on définie les supérieurs et inférieurs à afficher dans la matrice
    sup1 = tiragePremRouleau+1
    if tiragePremRouleau == 9:
        sup1 == 0
    sup2 = tirageDeuxRouleau+1
    if tirageDeuxRouleau == 9:
        sup2 == 0
    sup3 = tirageTroisRouleau+1
    if tirageTroisRouleau == 9:
        sup3 == 0
    inf1 = tiragePremRouleau-1
    if tiragePremRouleau == 0:
        inf1 == 9
    inf2 = tirageDeuxRouleau-1
    if tirageDeuxRouleau == 0:
        inf2 == 9
    inf3 = tirageTroisRouleau-1
    if tirageTroisRouleau == 0:
        inf3 == 9
    
    # on créer trois listes pour pouvoir afficher la matrice comprenant trois éléments pour chaque rouleau simulant l'affichage de la machine
    matrice1 = [sup1, sup2, sup3]
    matrice2 = [tiragePremRouleau, tirageDeuxRouleau, tirageTroisRouleau]
    matrice3 = [inf1, inf2, inf3]
    print("          ", matrice1)
    print("          ", matrice2, "     <-- Résultats du tirage")
    print("          ", matrice3)
    
    print()
    print()
    time.sleep(3)
    
    # on compare ensuite les valeurs tirées de chaque rouleau 
    # et en cas de victoire on choisis le gain en fonction du coefficient des éléments 
    if tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 0 :
        print("BRAVO ! VOUS AVEZ TOUCHE LE GROS LOT !!!!! Les trois symboles sont égal à 0 ! Vous avez gagné 100 fois votre mise ! Vous remportez donc :", jetonsMises * 100, "jetons !")
        credit += jetonsMises * 100
        ecartBanque -= jetonsMises * 99
        time.sleep(2)
    
    elif tirageDeuxRouleau != tiragePremRouleau and tiragePremRouleau != tirageTroisRouleau and tirageDeuxRouleau != tirageTroisRouleau :
        b = math.ceil(jetonsMises/2)
        print("Les trois symboles sont différents, vous récuperez donc la moitié de votre mise ! Vous remportez donc ", b, " jetons.")
        credit += b
        ecartBanque += (jetonsMises - b)
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 1 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 2.")
        print("Vous gagnez donc ", jetonsMises*2, " jetons.")
        credit += jetonsMises *2
        ecartBanque -= jetonsMises
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 2 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 2.")
        print("Vous gagnez donc ", jetonsMises*2, " jetons.")
        credit += jetonsMises *2
        ecartBanque -= jetonsMises
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 3 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 2.")
        print("Vous gagnez donc ", jetonsMises*2, " jetons.")
        credit += jetonsMises *2
        ecartBanque -= jetonsMises
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 4 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 4.")
        print("Vous gagnez donc ", jetonsMises*4, " jetons.")
        credit += jetonsMises *4
        ecartBanque -= jetonsMises*3
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 5 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 4.")
        print("Vous gagnez donc ", jetonsMises*4, " jetons.")
        credit += jetonsMises *4
        ecartBanque -= jetonsMises*3
        time.sleep(2)
    
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 6 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 4.")
        print("Vous gagnez donc ", jetonsMises*4, " jetons.")
        credit += jetonsMises *4
        ecartBanque -= jetonsMises*3
        time.sleep(2)
               
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 7 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 7.")
        print("Vous gagnez donc ", jetonsMises*7, " jetons.")
        credit += jetonsMises *7
        ecartBanque -= jetonsMises*6
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 8 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 7.")
        print("Vous gagnez donc ", jetonsMises*7, " jetons.")
        credit += jetonsMises *7
        ecartBanque -= jetonsMises*6
        time.sleep(2)
        
    elif tirageDeuxRouleau == tiragePremRouleau == tirageTroisRouleau == 9 :
        print("Bravo les trois symboles sont égal à ", tiragePremRouleau, ". Vous multipliez donc votre mise par 7.")
        print("Vous gagnez donc ", jetonsMises*7, " jetons.")
        credit += jetonsMises *7
        ecartBanque -= jetonsMises*6
        time.sleep(2)
        
    else:
        print("Oh noooon ! Quel dommage vous avez perdu c'est si triste mais vous ferez mieux la prochaîne fois ... Retentez votre chance !")
        print()
        time.sleep(2)
        ecartBanque += jetonsMises
        
    # si le joueur n'a plus de jetons la machine (boucle infinie) s'arrête
    if credit == 0 :
        print("Vous n'avez plus de jetons, vous ne pouvez plus continuer à jouer, ce fut un plaisir de faire affaire avec vous !")
        break
        
    print("Vous avez ", credit, " jetons restants.")
    print("( Ecart de la banque :", ecartBanque, ")")
    time.sleep(3)
    
  
    
    # on demande au joueur si il veut continuer à jouer 
    a = int(input("Voulez-vous continuer à jouer (tapez autre chose que 0) ou voulez-vous éteindre la machine (tapez 0) ? : "))
    if a == 0 :
        break
        os.system('cls')

    
