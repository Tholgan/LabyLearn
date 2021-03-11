### Code origiennellement par @Thibault Neveu - https://github.com/thibo73800
### Modifié par moi - mars 2021

import numpy as np
from random import randint
import random
import math

from sympy.strategies.core import switch


class EnvGrid(object):

    Q_table_sortie = [
        [0, 0, 0, 0],  ## pour l'état 0 (n'existe pas)
        [0, 0, 0, 0],  ## pour l'état 1
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

    Q_table_tresor1 = [
        [0, 0, 0, 0],  ## pour l'état 0 (n'existe pas)
        [0, 0, 0, 0],  ## pour l'état 1
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

    searchExit = False

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
        curTab = self.movement[self.y][self.x]
        print(curTab)
        print("Choice " + str(action))

        if (curTab[action] == 0):
          return -1

        return 0

    def check_treasure(self):
        if (self.searchExit == False):
            coor = [(index, row.index(1)) for index, row in enumerate(self.grid) if 1 in row]
            for co in coor:
                print(co[0], " cehrché et x current = ", self.x)
                print(co[1], " cehrché et y current = ", self.y)
                if co[0] == self.x and co[1] == self.y:
                    self.searchExit = True
                    return self.Q_table_sortie
                else:
                    return self.Q_table_tresor1
        return self.Q_table_sortie

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

        self.y = max(0, min(self.y + self.actions[action][0],5))
        self.x = max(0, min(self.x + self.actions[action][1],5))


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
    a = env.check_treasure()
    print(a)

    env = EnvGrid()
    env.reset()
    st = env.get_state()

    for _ in range(20):
        # Reset
        env.reset()
        st = env.get_state()
        
        while not env.is_finished(): ## on est pas encore sur la case finale

            Q = env.check_treasure()

            env.show()
            #at = int(input("$>"))
            action = take_action(st, Q, 0.8)

            stp1, r = env.step(action)
            print("s", stp1)
            print("r", r)

            # Mise à jour de la Q-table
            atp1 = take_action(stp1, Q, 0.0)
            if (env.searchExit == False):
                env.Q_table_sortie[st][action] = env.Q_table_sortie[st][action] + 0.1*(r + 0.9*env.Q_table_sortie[stp1][atp1] - env.Q_table_sortie[st][action])
                print(env.Q_table_sortie)
            else:
                env.Q_table_tresor1[st][action] = env.Q_table_tresor1[st][action] + 0.1 * (r + 0.9 * env.Q_table_tresor1[stp1][atp1] - env.Q_table_tresor1[st][action])
                print(env.Q_table_tresor1)

            st = stp1


    ## affichage de la Q-table finale
    print('     up     down    left   right')
    for s in range(1, 36):
        formatted_Q = [ '%.2f' % elem for elem in env.Q_table_sortie[s] ]
        print(s, formatted_Q)

    env.searchExit = False

    ## affichage de la policy finale apprise et du nombre d'étapes
    env.reset()
    s = env.get_state()
    print("starting state", s)
    nb_steps = 0
    while not env.is_finished():
        Q = env.check_treasure()
        if (env.searchExit == False):
            a = take_action(s,env.Q_table_sortie,0.0)
        else:
            a = take_action(s, env.Q_table_tresor1, 0.0)
        next_state, reward = env.step(a)
        print("state", next_state)
        s = next_state
        nb_steps += 1
    print("fin du parcours en", nb_steps, "etapes")