from game import Game


import pytest


@pytest.fixture
def game(scope="sesson"):
    return Game()


@pytest.fixture
def gameoflife(scope="sesson"):
    x = Game(5)
    return x.game_of_life(5)


@pytest.fixture
def create_board(scope="sesson"):
    x = Game()
    return x.create_game_board()


@pytest.fixture
def valid_square(scope="sesson"):
    x = Game()
    return x.is_valid_square(-5, 5)


@pytest.fixture
def check_alive_or_dead(scope="sesson"):
    x = Game()
    return x.alive_or_dead(1, 5)


@pytest.fixture
def check_get_next_board(scope="sesson"):
    x = Game()
    return x.get_next_board()
