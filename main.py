
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

    def setPiece(self, x, y, piece):
        self.chesboard[x][y] = piece
        return self.chesboard

    def getDiagonalMoves(self, x, y):
        moves = []
        for i in range(1, 8):
            if x + i < 8 and y + i < 8:
                moves.append((x + i, y + i))
            if x + i < 8 and y - i >= 0:
                moves.append((x + i, y - i))
            if x - i >= 0 and y + i < 8:
                moves.append((x - i, y + i))
            if x - i >= 0 and y - i >= 0:
                moves.append((x - i, y - i))
        return moves

    def getHorizontalMoves(self, x, y):
        moves = []
        for i in range(1, 8):
            if x + i < 8:
                moves.append((x + i, y))
            if x - i >= 0:
                moves.append((x - i, y))
        return moves

    def getVerticalMoves(self, x, y):
        moves = []
        for i in range(1, 8):
            if y + i < 8:
                moves.append((x, y + i))
            if y - i >= 0:
                moves.append((x, y - i))
        return moves

    def getMoves(self, x, y):
        figure = self.getPiece(x, y)
        if figure.type == PieceType.EMPTY:
            return []
        elif figure.type == PieceType.PAWN:
            if figure.color == PieceColor.WHITE:
                if y == 1:
                    return [(x, y + 1), (x, y + 2)]
                else:
                    return [(x, y + 1)]
            else:
                if y == 6:
                    return [(x, y - 1), (x, y - 2)]
                else:
                    return [(x, y - 1)]
        elif figure.type == PieceType.KNIGHT:
            return [(x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2), (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)]
        elif figure.type == PieceType.BISHOP:
            return self.getDiagonalMoves(x, y)
        elif figure.type == PieceType.ROOK:
            return self.getHorizontalMoves(x, y).extend(self.getVerticalMoves(x, y))
        elif figure.type == PieceType.QUEEN:
            return self.getDiagonalMoves(x, y).extend(self.getHorizontalMoves(x, y).extend(self.getVerticalMoves(x, y)))
        elif figure.type == PieceType.KING:
            return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
        else:
            return []
    
    def getValidMoves(self, x, y):
        moves = self.getMoves(x, y)
        validMoves = []
        for move in moves:
            if self.getPiece(move[0], move[1]).type == PieceType.EMPTY:
                validMoves.append(move)
            elif self.getPiece(move[0], move[1]).color != self.getPiece(x, y).color:
                validMoves.append(move)
        return validMoves

print("Testing ChessBoard")
board = ChessBoard()
board.open("board.txt")
board.print()
