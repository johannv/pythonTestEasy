# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2012

@author: Vincent Bruneau, Johann Verbroucht
'''
import unicodedata
from Student import Student
from Teacher import Teacher

class Code(object):
    '''
    Pour réaliser ces exercices il n'y a pas besoin de modifier les autres 
    classes, il suffit d'écrire les fonctions nécessaires.
    '''
    
    '''Exercice 1:
    Développez la fonction permettant de retourner le nombre d'élément d'une
    liste.
    '''
    def get_list_size(self, mylist):
        return 0
    
    '''
    Exercice 2:
    Développez la fonction permettant de retourner la factoriel d'un nombre.
    Exemple: 6! = 6*5*4*3*2*1 = 720
    '''
    
    def factoriel(self, number):
        return 0

    '''
    Exercice 3:
    Développez la fonction permettant de retourner le plus grand nombre
    d'une liste.
    Si la liste est vide, la fonction renvoie 0.
    '''
    def get_max_in_list(self, mylist):
        return 0

    '''
    Exercice 4:
    Développez la fonction qui renvoie la liste triée par ordre croissant.
    '''
    def sort_list(self, mylist):
        return 0

    '''
    Exercice 5:
    Développez la fonction qui renvoie une liste sans nombres impairs.
    '''
    def delete_uneven(self, mylist):
        return 0

    '''
    Exercice 6:
    Développez la fonction permettant de retourner le nombre d'occurrences
    d'une chaîne de caractères dans une autre.
    Exemples:
    get_occurrence('foo', 'foobar foo') retourne 2
    get_occurrence('foo', 'foofoo foobar') retourne 3
    '''
    def get_occurrence(self, string1, string2):
        return 0

    '''
    Exercice 7:
    Développez la fonction permettant de créer un nouvel élève en remplissant
    ses informations.
    Il faut aussi créer un professeur et l'associer à un élève.
    '''
    def create_student(self, studentid, studentlastname, studentfirstname, teacherid, teacherlastname, teacherfirstname):
        return 0

    '''
    Exercice 8:
    Développez la fonction qui renvoie la moyenne de l'élève.
    '''
    def get_average(self, student):
        return 0
    
    '''
    Exercice 9:
    Développez la fonction qui renvoie la meilleure note de l'élève.
    '''
    def get_best_mark(self, student):
        return 0

    '''
    Exercice 10:
    Développez la fonction qui renvoie la liste des notes par ordre croissant.
    '''
    def sort_mark_list(self, student):
        return student

    '''
     Exercice 11:
     Un nombre de Kaprekar est un nombre qui lorsqu'il est élevé au carré,
     peut être séparé en une partie gauche et une partie droite (non nulle)
     telles que la somme donne le nombre initial.
     
     Exemples: 
     703 est un nombre de Kaprekar car 703² = 494 209 et que 494 + 209 = 703. 
     4879 est un nombre de Kaprekar car 4879² = 23 804 641 et 238 + 04641 = 4879.
     
     Développez la fonction qui permet de tester si un nombre est un nombre de
     Kaprekar ou non.
     Attention: 1 est considéré comme un nombre de Kaprekar,
     2 et 3 ne le sont pas.
    '''
    def is_a_kaprekar_number(self, number):
        return False

    '''
    Exercice 12:
    Développez la fonction qui indique si un mot est un palindrome ou non. Un
    palindrome est un mot ou une phrase dont l'ordre des lettres reste le
    même qu'on le lise de gauche à droite ou de droite à gauche.
     
    Attention: Ne pas tenir compte de la ponctuation, ni des accents.
    
    Exemples: 
    Eh ! ça va la vache. 
    Kayak ...
    '''
    def is_a_palindrome(self, string):
        return False
    '''
    Cette fonction permet de supprimer les caractères accentués, les espaces
    et la ponctuation d'une chaîne de caractère. Exemple:
    "Il a arrêté une voiture." ==> "Ilaarreteunevoiture"
    '''
    def normalize_string(self, string):
        return ''.join(c for c in unicodedata.normalize('NFKD', unicode(string)) if c.isalnum()).lower()
