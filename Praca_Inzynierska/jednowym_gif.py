import cv2
import numpy as np
import imageio
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

import analiza_RMSE

lista_obrazow = []
lista_RMSE = []
rozmiar_tablicy = 11                                # tutaj ustawiamy rozmiar tablicy

oczekiwany_wynik = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
rzeczywisty_wynik = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class Cialo:
    temp = 0.0
    temp_poprzednia = 0.0


def tworzenie_tablicy(n, temp):
    tab = []
    for i in range(n):
        new = Cialo()
        new.temp = temp
        new.temp_poprzednia = temp
        tab.append(new)
    return tab


def krok(tab):
    zmiana = 0
    for i in range(len(tab)):
        if(i > 0 and i < (len(tab) - 1)):
            wczesniej = tab[i].temp
            tab[i].temp = round((tab[i-1].temp_poprzednia + tab[i].temp_poprzednia + tab[i+1].temp_poprzednia)/3, 5)
            if(wczesniej != tab[i].temp):
                zmiana = zmiana + 1
    for i in range(len(tab)):
        tab[i].temp_poprzednia = tab[i].temp
    return zmiana


def RMSE(actual, pred):
    rmse = sqrt(mean_squared_error(actual, pred))
    f = open("jednowymiarowa/RMSE.txt", "a")
    f.write(str(rmse) + "\n")
    f.close()
    lista_RMSE.append(rmse)
    return rmse


def zapisz_obraz(tab, img, nr_obrazu):
    for i in range(len(tab)):
        contours = np.array([[i * 10, 0], [i * 10, 9], [(i * 10) + 9, 9], [(i * 10) + 9, 0]])
        cv2.fillPoly(img, pts=[contours], color=(int((tab[i].temp)*25.5), int((tab[i].temp)*25.5), int((tab[i].temp)*25.5)))
    cv2.imwrite("jednowymiarowa/"+str(nr_obrazu)+".png", img)
    lista_obrazow.append("jednowymiarowa/"+str(nr_obrazu)+".png")


def wyswietl(tab):
    p = ''
    for i in range(len(tab)):
        p = p + ' ' + str(round(tab[i].temp,2))
    return(p)


def zapisz_txt(tab):
    f = open("jednowymiarowa/dane.txt", "a")
    f.write(wyswietl(tab)+"\n")
    f.close()


def wykres_RMSE(lista_RMSE):
    for i in range(len(lista_RMSE)):
        lista_RMSE[i] = lista_RMSE[i]*100
    plt.plot(lista_RMSE)
    plt.grid(True)
    plt.xlabel("krok")
    plt.ylabel("Procent rozbieżności")
    plt.title("Wykres RMSE")
    plt.savefig("jednowymiarowa/wykres_RMSE.jpg", dpi=72)
    plt.show()


if __name__ == '__main__':
                                                        # czyszczenie pliku "dane.txt"
    f = open("jednowymiarowa/dane.txt", "w")
    f.close()
    f = open("jednowymiarowa/RMSE.txt", "w")
    f.close()

    tab = tworzenie_tablicy(rozmiar_tablicy, 0)
    tab[0].temp = 10                                    # tutaj ustawiamy punkty grzania
    tab[0].temp_poprzednia = 10

    img = np.zeros((10, (rozmiar_tablicy) * 10, 3), dtype='uint8')

    zmiana = 1
    nr_obrazu = 0
                                                    # pętla powtarza kroki dopóki zachodzą jakieś zmiany
    while(zmiana > 0):
        zapisz_obraz(tab, img, nr_obrazu)
        zapisz_txt(tab)

        for i in range(len(tab)):
            rzeczywisty_wynik[i]=tab[i].temp

        print(RMSE(rzeczywisty_wynik, oczekiwany_wynik))
        zmiana = krok(tab)
        nr_obrazu = nr_obrazu + 1
                                                                                        # składanie gifa
    with imageio.get_writer('jednowymiarowa/jednowymiarowa.gif', mode='I') as writer:
        for filename in lista_obrazow:
            image = imageio.imread(filename)
            writer.append_data(image)

    wykres_RMSE(lista_RMSE)