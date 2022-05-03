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


def wyswietl(tab):
    for i in range(len(tab)):
        p = ''
        for j in range(len(tab)):
            p = p + '\t' + str(round(tab[i][j].temp,1))
        print(p)

def krok(tab):
    zmiana = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            if(i > 0 and i < (len(tab) - 1) and j > 0 and j < (len(tab) - 1)):
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
    tab[int(rozmiar_tablicy/2)][int(rozmiar_tablicy/2)].temp = 10
    tab[int(rozmiar_tablicy / 2)][int(rozmiar_tablicy / 2)].temp_poprzednia = 10

    zmiana = 1
    while(zmiana > 0):
        wyswietl(tab)
        zmiana = krok(tab)
        print('')