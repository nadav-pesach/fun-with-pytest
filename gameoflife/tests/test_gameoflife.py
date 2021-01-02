from game import Game

import numpy as np


def test_game(game):
    assert isinstance(game, Game)


def test_game_create(game):
    assert isinstance(game.create, int)


def test_game_survive(game):
    assert isinstance(game.survive, tuple)


def test_game_number(game):
    assert isinstance(game.number, int)


def test_game_board(game):
    assert isinstance(game.board, np.ndarray)


def test_game_str():
    assert '__str__' in Game.__dict__


def test_create_board(create_board):
    assert isinstance(create_board, np.ndarray)


def test_create_board_size(game, create_board):
    assert len(create_board) == game.number


def test_valid_square(valid_square):
    assert isinstance(valid_square, bool)


def test_alivedead(check_alive_or_dead):
    assert check_alive_or_dead in range(9)


def test_get_next_board(check_get_next_board):
    assert isinstance(check_get_next_board, np.ndarray)


def test_gameoflife(gameoflife):
    assert 'game over' in gameoflife
