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

def krok_zly(tab):
    zmiana = 0
    for i in range(len(tab)):
        if(i > 0 and i < (len(tab) - 1)):
            if (tab[i].temp != 10):
                wczesniej = tab[i].temp
                tab[i].temp = round((tab[i-1].temp + tab[i].temp + tab[i+1].temp)/3, 2)
                if(wczesniej != tab[i].temp):
                    zmiana = zmiana + 1
    return zmiana

def krok(tab):
    zmiana = 0
    for i in range(len(tab)):
        if(i > 0 and i < (len(tab) - 1)):
            if(tab[i].temp != 10):
                wczesniej = tab[i].temp
                tab[i].temp = round((tab[i-1].temp_poprzednia + tab[i].temp_poprzednia + tab[i+1].temp_poprzednia)/3, 2)
                if(wczesniej != tab[i].temp):
                    zmiana = zmiana + 1
    for i in range(len(tab)):
        tab[i].temp_poprzednia = tab[i].temp
    return zmiana



def wyswietl(tab):
    p = ''
    for i in range(len(tab)):
        p = p + ' ' + str(round(tab[i].temp,2))
    print(p)


if __name__ == '__main__':
    rozmiar_tablicy = 11
    tab = tworzenie_tablicy(rozmiar_tablicy, 0)
    tab[0].temp = 10
    tab[0].temp_poprzednia = 10

    zmiana = 1
    i = 0
    while(zmiana > 0):
        #print("Krok:", i)
        wyswietl(tab)
        zmiana = krok_zly(tab)
        i = i + 1
