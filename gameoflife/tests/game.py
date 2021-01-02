import re

import matplotlib.pyplot as plt

import numpy as np


class Game:

    def __init__(self, number=50, condi='B3/S23'):
        pattern = re.compile(r'\w(\d)/\w(\d)(\d)')
        path_de = pattern.findall(condi)
        self.create = int(path_de[0][0])
        self.survive = int(path_de[0][1]), int(path_de[0][2])
        self.number = number
        self.board = self.create_game_board()

    def __str__(self):
        # credit to chess game from ex:157
        """Return current state of the board for display purposes."""
        printable = ""
        for row in self.board:
            for col in row:
                printable = printable + f" {col} "
            printable = printable + '\n'
        return printable

    def create_game_board(self):
        "Creat first board position"
        return np.random.choice([0, 1], size=self.number ** 2, p=[0.75, 0.25]).reshape(self.number, self.number)

    def is_valid_square(self, row, column):
        # credit to chess game from ex:157
        """Return True if square in board bounds, False otherwise."""
        row_exists = row in range(len(self.board))
        column_exists = column in range(len(self.board))
        return row_exists and column_exists

    def alive_or_dead(self, row, col):
        """check 8 squares next to current squere and return how many alive"""
        count = 0
        if self.is_valid_square(row - 1, col - 1) and self.board[row - 1, col - 1] == 1:
            count += 1
        if self.is_valid_square(row - 1, col) and self.board[row - 1, col - 1] == 1:
            count += 1
        if self.is_valid_square(row - 1, col + 1) and self.board[row - 1, col + 1] == 1:
            count += 1
        if self.is_valid_square(row, col - 1) and self.board[row, col - 1] == 1:
            count += 1
        if self.is_valid_square(row, col + 1) and self.board[row, col + 1] == 1:
            count += 1
        if self.is_valid_square(row + 1, col - 1) and self.board[row + 1, col - 1] == 1:
            count += 1
        if self.is_valid_square(row + 1, col) and self.board[row + 1, col] == 1:
            count += 1
        if self.is_valid_square(row + 1, col + 1) and self.board[row + 1, col + 1] == 1:
            count += 1
        return count

    def get_next_board(self):
        """creat next array"""
        new_board = np.empty(shape=(0))
        for row in range(self.number):
            for col in range(self.number):
                count = self.alive_or_dead(row, col)
                current = self.board[row, col]
                if current and count in self.survive:
                    new_board = np.append(new_board, 1)
                elif count == self.create:
                    new_board = np.append(new_board, 1)
                else:
                    new_board = np.append(new_board, 0)
        self.board = new_board.reshape(self.number, self.number)
        return self.board

    def game_of_life(self, times=100):
        """Get number of time to run the program"""
        for _ in range(times):
            x = self.get_next_board()
            plt.imshow(x)
            plt.draw()
            plt.pause(0.001)
        return 'game over'


if __name__ == "__main__":
    x = Game()
    x.game_of_life()
