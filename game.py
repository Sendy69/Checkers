import pygame
from board import Board
from constants import BLACK, WHITE


class Game:
    def __init__(self, win):
        self._init()
        self.win = win 
        
    def update_game(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}
    
    def reset_game(self):
        self._init()

    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)
        else: 
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected_piece = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        
        return False



    # def _move(self, row, col):    