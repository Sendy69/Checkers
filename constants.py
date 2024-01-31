import pygame as pg
import os

## Ce fichier contient tous les objets stables du jeu c-à-d qui ne changeront pas dans le jeu de dame soient les couleurs,
## les dimensions du tableaux, le chemin d'accès de l'image de la couronne 


WIDTH, HEIGHT = 800, 800  # Dimension du jeu
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH // COLS # permet d'indiquer que la taille des carrés varient en fct de la largeur du tableau et des lignes

#RGB
LIGHT_BROWN = (255,204,153)
BROWN = (153, 76, 0)
BLUE = (0,0,255)
GREY = (128,128,128)
WHITE = (255, 255, 255)
BLACK = (0,0,0)


#path of pawn
PATH = "chess_img"

#pawn sizing
CROWN = pg.transform.scale(pg.image.load(os.path.join(PATH, 'crown2.png')), (44, 25))
# red_pawn = pg.transform.scale(pg.image.load(os.path.join(PATH, 'red_pawn.png')), (SQUARE, SQUARE))