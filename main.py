
from enum import Enum


class PieceType(Enum):
    EMPTY = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class PieceColor(Enum):
    WHITE = 1
    BLACK = 2

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Piece:
    def __init__(self):
        self.type = PieceType.EMPTY
        self.color = PieceColor.WHITE
    
    def typeFromChar(self, char):
        char = char.upper()
        if char == 'P':
            self.type = PieceType.PAWN
        elif char == 'N':
            self.type = PieceType.KNIGHT
        elif char == 'B':
            self.type = PieceType.BISHOP
        elif char == 'R':
            self.type = PieceType.ROOK
        elif char == 'Q':
            self.type = PieceType.QUEEN
        elif char == 'K':
            self.type = PieceType.KING
        elif char == '.':
            self.type = PieceType.EMPTY
        else:
            self.type = PieceType.EMPTY

    def colourFromChar(self, char):
        if char.islower():
            self.color = PieceColor.WHITE
        else:
            self.color = PieceColor.BLACK

    def __str__(self):
        piece = '.'
        if self.type == PieceType.PAWN:
            piece = 'P'
        elif self.type == PieceType.KNIGHT:
            piece = 'N'
        elif self.type == PieceType.BISHOP:
            piece = 'B'
        elif self.type == PieceType.ROOK:
            piece = 'R'
        elif self.type == PieceType.QUEEN:
            piece = 'Q'
        elif self.type == PieceType.KING:
            piece = 'K'
        if self.color == PieceColor.WHITE:
            piece = piece.lower()
        return piece

class ChessBoard:
    def __init__(self):
        self.chesboard = []
        for i in range(8):
            line = []
            for j in range(8):
                line.append(Piece())
            self.chesboard.append(line)

    def open(self, filename):
        self.chesboard = []
        with open(filename) as f:
            file = f.readlines()
            for fileLine in file:
                line = []
                for char in fileLine:
                    if char == '\n':
                        continue
                    piece = Piece()
                    piece.colourFromChar(char)
                    piece.typeFromChar(char)
                    line.append(piece)
                self.chesboard.append(line)
        return self.chesboard

    def print(self):
        for line in self.chesboard:
            for piece in line:
                print(piece, end='')
            print()
        return self.chesboard

    def getPiece(self, x, y):
        return self.chesboard[x][y]

print("Testing ChessBoard")
board = ChessBoard()
board.open("board.txt")
board.print()
