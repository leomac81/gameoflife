from itertools import count
import random
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

squaresize = int(input("you are creating an N x N grid. Choose N:  "))


def InitalBoardfun(height, width):
    InputBoard = np.random.randint(0, 2, size=(height, width))
    return InputBoard


def NextBoardfun(Firstboard, width, height):
    nextBoard = np.random.rand(height, width)

    # set_zero_idxs = (Firstboard == 1) & ((N<2)|(N>3))

    for i in range(width):
        for j in range(height):

            countAlive = 0
            isAlive = False
            nextIsAlive = False
            if Firstboard[i][j] == 1:
                isAlive = True
                countAlive = -1

            r = -1
            while r < 2:
                y = j + r
                q = -1

                while q < 2:
                    x = i + q

                    if x == -1:
                        x = width - 1
                    if x == width:
                        x = 0
                    if y == -1:
                        y = height - 1
                    if y == height:
                        y = 0

                    if Firstboard[x][y] == 1:
                        countAlive = countAlive + 1

                    q = q + 1
                r = r + 1

            # print(countAlive)

            if isAlive == True:
                if countAlive == 3 or countAlive == 2:
                    nextIsAlive = True

            elif isAlive == False and countAlive == 3:
                nextIsAlive = True

            if nextIsAlive == True:
                nextBoard[i][j] = 1

            else:
                nextBoard[i][j] = 0

    return nextBoard


height = squaresize
width = squaresize
Firstboard = InitalBoardfun(height, width)

fig = plt.figure()
im = plt.imshow(Firstboard)


def init():
    im.set_data(np.zeros_like(Firstboard))
    return (im,)


i = 0
number_alive = []
generation = []


def update(frames):
    global Firstboard
    global i

    Firstboard = NextBoardfun(Firstboard, width, height)
    im.set_data(Firstboard)
    number_alive.append(np.count_nonzero(Firstboard))
    generation.append(i)
    print(generation[-1], number_alive[-1])
    if number_alive[-1] == number_alive[-2] == number_alive[-3] == number_alive[-4] == number_alive[-5]:
        fig = plt.figure()
        plt.plot(generation, number_alive)
        plt.show()
        sys.exit()
    i = i + 1


anim = animation.FuncAnimation(fig, update, init_func=init, interval=10, repeat=False)
plt.show()
plt.close()
