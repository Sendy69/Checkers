import pygame
from board import Board
from constants import BLACK, WHITE, BLUE, SQUARE_SIZE

## C'est dans ce fichier qu'il y'a tout la logique du jeu 
## On commence par créer une classe qu'on appelera Game qui contiendra toute les propriétés et fonctions de logique du jeu de dame

class Game:
    def __init__(self, win):
        self._init()
        self.win = win 

## Création de la fonction de mise à jour du tableau de jeu après chaque mouvement de pièces              
    def update_game(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

## Fonction qui permet de déterminer le gagnant à la fin de la partie de jeu
    def winner(self):
        return self.board.winner()

## Fonction de réinitialisation de la partie
    def reset_game(self):
        self._init()

## Cette fonction permet de récupérer la position (row, col) d'une pièce et de passer ses coordonnées à la fonction _move() 
## afin d'assurer son déplacement
    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)
         
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False

## Cette fonction permet le déplacement d'une pièce choisie par le joueur une fois que c'est son tour de jouer
    def _move(self, row, col):
        piece = self.board.get_piece(row, col) ## récupération des coordonnées de la pièce sur le tableau
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves: ## A ce niveau on vérifie si le pion est bien sélectionné et si ses coordonnées respectent les coordonnées valides
             self.board.move(self.selected_piece, row, col)
             jumped = self.valid_moves[(row, col)]
             if jumped:
                 self.board.remove(jumped)
             self.change_turn()
        else: 
            return False
        return True

## Cette
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15 )


    def  change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else: 
            self.turn = BLACK
