import cv2
import numpy as np
import imageio
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

lista_obrazow = []
rozmiar_tablicy = 21                              # tutaj ustawiamy rozmiar tablicy


class Cialo:
    stan = 0
    stan_pop = 0


def tworzenie_tablicy(n):
    tab = [ [0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new = Cialo()
            new.stan = 0
            new.stan_pop = 0
            tab[i][j] = new
    return tab


def krok(tab):
    zmiana = 0
    for i in range(len(tab)-1):
        for j in range(len(tab)-1):
            wczesniej = tab[i][j].stan

            if(j%2 == 0):       #parzyste wiersze
                x = tab[i - 1][j - 1].stan_pop + tab[i][j - 1].stan_pop + tab[i][j + 1].stan_pop + tab[i - 1][j].stan_pop + tab[i][j].stan_pop + tab[i + 1][j].stan_pop + tab[i - 1][j + 1].stan_pop
            else:               #nieparzyste wiersze
                x = tab[i][j - 1].stan_pop + tab[i - 1][j].stan_pop + tab[i][j].stan_pop + tab[i + 1][j].stan_pop + tab[i][j + 1].stan_pop + tab[i + 1][j + 1].stan_pop + tab[i + 1][j - 1].stan_pop

            #if (x > 0):                # jednolity kryształ
            if (x == 1):                # płatek śniegu
                tab[i][j].stan = 1

            if(wczesniej != tab[i][j].stan):
                zmiana = zmiana + 1

    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j].stan_pop = tab[i][j].stan
    return zmiana


def zapisz_obraz(tab, img, nr_obrazu):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if(j%2 == 0 and tab[i][j].stan == 1):                   # parzyste wiersze
                hex = np.array([[(i*10)+5, (j*10)],[(i*10), (j*10)+5], [(i*10), (j*10)+10],[(i*10)+5, (j*10)+15], [(i*10)+10, (j*10)+10],[(i*10)+10, (j*10)+5]],np.int32)
                #cv2.polylines(img, [hex], True, (100, 100, 100))
                cv2.fillPoly(img, pts=[hex], color=(100, 100, 100))
            if (j % 2 != 0 and tab[i][j].stan == 1):                # nieparzyste wiersze
                hex = np.array([[(i*10) + 10, (j*10)], [(i*10) + 5, (j*10) + 5], [(i*10) + 5, (j*10) + 10], [(i*10) + 10, (j*10) + 15], [(i*10) + 15, (j*10) + 10],[(i*10) + 15, (j*10) + 5]], np.int32)
                #cv2.polylines(img, [hex], True, (100, 100, 100))
                cv2.fillPoly(img, pts=[hex], color=(100, 100, 100))
    cv2.imwrite("krysztal/"+str(nr_obrazu)+".png", img)
    lista_obrazow.append("krysztal/"+str(nr_obrazu)+".png")

if __name__ == '__main__':

    img = np.zeros((((rozmiar_tablicy) * 10), ((rozmiar_tablicy) * 10), 3),dtype='uint8')

    tab = tworzenie_tablicy(rozmiar_tablicy)
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].stan = 1
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].stan_pop = 1

    zmiana = 1
    nr_obrazu = 0

    while(zmiana > 0):
        zapisz_obraz(tab, img, nr_obrazu)
        zmiana = krok(tab)
        nr_obrazu = nr_obrazu + 1

                                                                                        # składanie gifa
    with imageio.get_writer('krysztal/krysztal.gif', mode='I') as writer:
        for filename in lista_obrazow:
            image = imageio.imread(filename)
            writer.append_data(image)








