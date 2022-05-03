import cv2
import numpy as np
import imageio

lista_obrazow = []

class Cialo:
    temp = 0.0
    temp_poprzednia = 0.0


def tworzenie_tablicy(n, temp):
    tab = [ [0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new = Cialo()
            new.temp = temp
            new.temp_poprzednia = temp

            tab[i][j] = new
    return tab


def zapisz_obraz(tab, img, nr_obrazu):
    for i in range(len(tab)):
        for j in range(len(tab)):
            contours = np.array([[(i-1) * 10, (j-1)*10], [(i-1) * 10, ((j-1)*10)+9], [((i-1) * 10) + 9, ((j-1)*10) + 9], [((i-1) * 10) + 9, (j-1)*10]])
            cv2.fillPoly(img, pts=[contours], color=(int((tab[i-1][j-1].temp)*2.55), int((tab[i-1][j-1].temp)*2.55), int((tab[i-1][j-1].temp)*2.55)))
    cv2.imwrite("dwuwymiarowa/"+str(nr_obrazu)+".png", img)
    lista_obrazow.append("dwuwymiarowa/"+str(nr_obrazu)+".png")


def krok(tab):
    zmiana = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            if(i > 0 and i < (len(tab)-1) and j > 0 and j < (len(tab)-1)):
                if(tab[i][j] != tab[int(rozmiar_tablicy/2)][int(rozmiar_tablicy/2)]):
                    wczesniej = tab[i][j].temp
                    tab[i][j].temp = round(((0.7*tab[i-1][j-1].temp_poprzednia) + tab[i-1][j].temp_poprzednia + (0.7*tab[i-1][j+1].temp_poprzednia) + tab[i][j-1].temp_poprzednia + tab[i][j].temp_poprzednia + tab[i][j+1].temp_poprzednia + (0.7*tab[i+1][j-1].temp_poprzednia) + tab[i+1][j].temp_poprzednia + (0.7*tab[i+1][j+1].temp_poprzednia))/7.8, 2)
                    if(wczesniej != tab[i][j].temp):
                        zmiana = zmiana + 1

    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j].temp_poprzednia = tab[i][j].temp
    return zmiana


if __name__ == '__main__':

    rozmiar_tablicy = 9

    tab = tworzenie_tablicy(rozmiar_tablicy, 0)
    tab[int(rozmiar_tablicy/2)][int(rozmiar_tablicy/2)].temp = 100
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].temp_poprzednia = 100

    img = np.zeros(((rozmiar_tablicy) * 10, (rozmiar_tablicy) * 10, 3), dtype='uint8')

    zmiana = 1
    nr_obrazu = 0

    while(zmiana > 0):
        zapisz_obraz(tab, img, nr_obrazu)
        zmiana = krok(tab)
        nr_obrazu = nr_obrazu + 1

                                                                                        # składanie gifa
    with imageio.get_writer('dwuwymiarowa/dwuwymiarowa.gif', mode='I') as writer:
        for filename in lista_obrazow:
            image = imageio.imread(filename)
            writer.append_data(image)








