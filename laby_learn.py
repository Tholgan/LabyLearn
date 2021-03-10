### Code origiennellement par @Thibault Neveu - https://github.com/thibo73800
### Modifié par moi - mars 2021

import numpy as np
from random import randint
import random

from sympy.strategies.core import switch


class EnvGrid(object):

    def __init__(self):
        super(EnvGrid, self).__init__()

        self.grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0]
        ]

        # starting position
        self.st_pos = [0,0]
        self.reset()

        self.actions = [
            [-1, 0], # Up
            [0, 1], # Right
            [1, 0], #Down
            [0, -1] # Left
        ]

        self.movement = [
            [[0,1,1,0], [0,1,0,1], [0,1,0,1], [0,1,1,1], [0,1,0,1], [0,0,1,1]], #[haut, droite, bas, gauche]
            [[1,1,1,0], [0,1,1,1], [0,1,1,1], [1,0,1,1], [0,1,1,0], [1,1,1,1]],
            [[1,1,1,0], [1,0,1,1], [1,0,1,0], [1,1,0,0], [1,1,1,1], [1,1,1,1]],
            [[1,0,1,0], [1,1,1,0], [1,1,0,1], [0,1,1,1], [1,1,0,1], [1,1,1,1]],
            [[1,0,1,0], [1,1,1,0], [0,1,1,1], [1,1,1,1], [0,1,1,1], [1,1,1,1]],
            [[0,1,1,0], [1,0,0,1], [1,1,0,0], [1,0,1,1], [1,1,0,0], [1,1,1,1]]
        ]

    def get_state(self):
        return self.y*6 + self.x + 1

    def checkCrossing(self, action):
        curTab = self.movement[self.x][self.y]
        print(curTab)
        print("Choice " + str(action))

        # if (action == self.actions[0]):
        #     if (curTab[0] == 0):
        #         return 0
        # if (action == self.actions[1]):
        #     if (curTab[2] == 0):
        #         return 0
        # if (action == self.actions[2]):
        #     if (curTab[3] == 0):
        #         return 0
        # if (action == self.actions[3]):
        #     if (curTab[1] == 0):
        #         return 0

        if (curTab[action] == 0):
          return -1

        return 0

    def reset(self):
        """
            Reset du jeu
        """
        self.x = self.st_pos[0]
        self.y = self.st_pos[1]

    def step(self, action):
        """
            Action: 0, 1, 2, 3;
            mise a jour de la position + retourne l'état d'arrivée et la récompense
        """
        r = self.checkCrossing(action)

        if (r == -1) :
            return self.get_state(), r

        self.y = max(0, min(self.y + self.actions[action][0],2))
        self.x = max(0, min(self.x + self.actions[action][1],2))

        return self.get_state(), self.grid[self.y][self.x]

    def show(self):
        """
            Show the grid
        """
        print("---------------------")
        y = 0
        for line in self.grid:
            x = 0
            for pt in line:
                print("%s\t" % (pt if y != self.y or x != self.x else "X"), end="")
                x += 1
            y += 1
            print("")

    def is_finished(self):
        return self.grid[self.y][self.x] == 2 ## on est arrives au but

def take_action(st, Q, eps):
    # Choisir une action (retourne l'action choisie)
    if random.uniform(0, 1) < eps: # exploration
        action = randint(0, 3)
    else: # exploitation
        action = np.argmax(Q[st])
    return action

if __name__ == '__main__':
    env = EnvGrid()
    env.reset()
    st = env.get_state()

    Q = [
        [0, 0, 0, 0], ## pour l'état 0 (n'existe pas)
        [0, 0, 0, 0], ## pour l'état 1
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    for _ in range(20):
        # Reset
        env.reset()
        st = env.get_state()
        
        while not env.is_finished(): ## on est pas encore sur la case finale
            env.show()
            #at = int(input("$>"))
            action = take_action(st, Q, 0.8)

            stp1, r = env.step(action)
            print("s", stp1)
            print("r", r)

            # Mise à jour de la Q-table
            atp1 = take_action(stp1, Q, 0.0)
            Q[st][action] = Q[st][action] + 0.1*(r + 0.9*Q[stp1][atp1] - Q[st][action])
            print(Q)
            st = stp1

    ## affichage de la Q-table finale
    print('     up     down    left   right')
    for s in range(1, 36):
        formatted_Q = [ '%.2f' % elem for elem in Q[s] ]
        print(s, formatted_Q)
    
    ## affichage de la policy finale apprise et du nombre d'étapes
    env.reset()
    s = env.get_state()
    print("starting state", s)
    nb_steps = 0
    while not env.is_finished():
        a = take_action(s,Q,0.0)
        next_state, reward = env.step(a)
        print("state", next_state)
        s = next_state
        nb_steps += 1
    print("fin du parcours en", nb_steps, "etapes")