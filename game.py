
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# class game:
    

#     def __init__(self, number):
#         self.initgamme(number)


#     def create_game_board(number):
#       return np.random.choice([0, 1], size = 5 ** 2, p=[0.75, 0.25]).reshape(5, 5)



x = np.random.choice([0, 1], size = 50 ** 2, p=[0.75, 0.25]).reshape(50, 50)

for i in range(50):
    x = np.random.choice([0, 1], size = 50 ** 2, p=[0.75, 0.25]).reshape(50, 50)
    plt.imshow(x)
    plt.draw()
    plt.pause(0.0001)



