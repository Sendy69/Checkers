import pygame as pg
import os
# Rôle de OS et pygame ??

width, height = 760, 760 # Dimension du jeu
rows, cols = 8,8
square = width // rows # permet d'indiquer que la taille des carrés varient en fct de la largeur du tableau et des lignes

light_brown = (255,204,153)
brown = (153, 76, 0)

#path of pawn
PATH = "chess_img"

#pawn sizing
black_pawn = pg.transform.scale(pg.image.load(os.path.join(PATH, 'black_pawn.png')), (square, square))
red_pawn = pg.transform.scale(pg.image.load(os.path.join(PATH, 'red_pawn.png')), (square, square))