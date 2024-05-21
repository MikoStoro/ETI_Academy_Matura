liczby = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/przyklad.txt").readlines()

zrownowazonych = 0
prawie_zrownowazonych = 0



for liczba in liczby:
    zer = 0
    jedynek = 0
    for d in liczba:
        print(d)
        if d == '1':
            jedynek += 1
        if d == '0':
            zer += 1
    if zer == jedynek:
        zrownowazonych += 1
    if abs(zer-jedynek) == 1:
        prawie_zrownowazonych += 1



print("zrownowazonych: " + str(zrownowazonych))
print("prawie zrownowazonych: " + str(prawie_zrownowazonych))