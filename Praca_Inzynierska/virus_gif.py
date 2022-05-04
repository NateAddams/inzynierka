import cv2
import numpy as np
import imageio

lista_obrazow = []

class Cialo:
    stan = 0
    stan_poprzednia = 0
    odpornosc = 0
    choroba = 0


def tworzenie_tablicy(n):
    tab = [ [0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new = Cialo()
            new.stan = 0
            new.stan_poprzednia = 0
            new.odpornosc = 0
            new.choroba = 0

            tab[i][j] = new
    return tab


def zapisz_obraz(tab, img, nr_obrazu):
    for i in range(len(tab)):
        for j in range(len(tab)):
            contours = np.array([[i * 10, j * 10], [i * 10, (j * 10) + 9], [(i * 10) + 9, (j * 10) + 9], [(i * 10) + 9, j * 10]])
            if tab[i][j].stan == 0:
                cv2.fillPoly(img, pts=[contours], color=(0, 150, 0))
            else:
                cv2.fillPoly(img, pts=[contours], color=(0, 0, 150))
    cv2.imwrite("wirus/"+str(nr_obrazu)+".png", img)
    lista_obrazow.append("wirus/"+str(nr_obrazu)+".png")


def krok(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i != 0:
                x1 = i - 1
            else:
                x1 = len(tab) - 1

            if j != 0:
                y1 = j - 1
            else:
                y1 = len(tab) - 1

            if i != (len(tab) - 1):
                x2 = i + 1
            else:
                x2 = 0

            if j != (len(tab) - 1):
                y2 = j + 1
            else:
                y2 = 0

            if 0 < round(((0.7*tab[x1][y1].stan_poprzednia) + tab[x1][j].stan_poprzednia + (0.7*tab[x1][y2].stan_poprzednia) + tab[i][y1].stan_poprzednia + tab[i][j].stan_poprzednia + tab[i][y2].stan_poprzednia + (0.7*tab[x2][y1].stan_poprzednia) + tab[x2][j].stan_poprzednia + (0.7*tab[x2][y2].stan_poprzednia))/7.8, 2):
                tab[i][j].stan = 1






    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j].stan_poprzednia = tab[i][j].stan


if __name__ == '__main__':

    rozmiar_tablicy = 9

    tab = tworzenie_tablicy(rozmiar_tablicy)
    tab[int(rozmiar_tablicy/2)][int(rozmiar_tablicy/2)].stan = 1
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].stan_poprzednia = 1

    img = np.zeros(((rozmiar_tablicy) * 10, (rozmiar_tablicy) * 10, 3), dtype='uint8')

    nr_obrazu = 0

    while nr_obrazu < 100:
        zapisz_obraz(tab, img, nr_obrazu)
        krok(tab)
        nr_obrazu = nr_obrazu + 1

                                                                                        # składanie gifa
    with imageio.get_writer('wirus/wirus.gif', mode='I') as writer:
        for filename in lista_obrazow:
            image = imageio.imread(filename)
            writer.append_data(image)








