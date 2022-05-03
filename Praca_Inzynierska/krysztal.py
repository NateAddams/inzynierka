
class Cialo:
    x = 0
    y = 0
    krysztal = 0
    krysztal_poprzedni = 0

def tworzenie_tablicy(n):
    tab = [ [0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new = Cialo()
            new.x = i
            new.y = j
            new.krysztal = 0
            new.krysztal_poprzedni = 0
            tab[i][j] = new
    return tab


def wyswietl(tab):
    for i in range(len(tab)):
        p = ''
        for j in range(len(tab)-1):
            p = p + ' ' + str(int(tab[i][j+1].krysztal))
        print(p)

def krok(tab):
    zmiana = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            if(i > 0 and i < (len(tab) - 1) and j>1 and j < (len(tab) - 1)):

                wczesniej = tab[i][j].krysztal

                if(i%2 == 0):       #parzyste wiersze
                    x = tab[i-1][j].krysztal_poprzedni + tab[i-1][j+1].krysztal_poprzedni + tab[i][j-1].krysztal_poprzedni + tab[i][j].krysztal_poprzedni + tab[i][j+1].krysztal_poprzedni + tab[i+1][j].krysztal_poprzedni + tab[i+1][j+1].krysztal_poprzedni
                else:               #nieparzyste wiersze
                    x = tab[i-1][j-1].krysztal_poprzedni + tab[i-1][j].krysztal_poprzedni + tab[i][j-1].krysztal_poprzedni + tab[i][j].krysztal_poprzedni + tab[i][j+1].krysztal_poprzedni + tab[i+1][j-1].krysztal_poprzedni + tab[i+1][j].krysztal_poprzedni

                if (x > 0):
                    tab[i][j].krysztal = 1

                if(wczesniej != tab[i][j].krysztal):
                    zmiana = zmiana + 1

    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j].krysztal_poprzedni = tab[i][j].krysztal
    return zmiana



if __name__ == '__main__':
    rozmiar_tablicy = 21
    tab = tworzenie_tablicy(rozmiar_tablicy)
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].krysztal = 1
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].krysztal_poprzedni = 1

    zmiana = 1
    while (zmiana > 0):
        wyswietl(tab)
        zmiana = krok(tab)
        print('')

