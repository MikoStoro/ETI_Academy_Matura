liczby =   [ x.strip() for x in open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/przyklad.txt").readlines() ]

def zer_jedynek(liczba : str):
    zer = 0
    jedynek = 0
    for d in liczba:
        if d == '1':
            jedynek += 1
        if d == '0':
            zer += 1
    return [zer,jedynek]
def silnia(liczba : int):
    wynik = 1
    for i in range(1,liczba+1):
        wynik *= i
    return wynik
def _oblicz_mianownik(z_j : [ int ]):
    return(silnia(z_j[0]) * silnia(z_j[1]))

def oblicz_mianownik(liczba):
    return _oblicz_mianownik(zer_jedynek(liczba))

najmniejszy_mianownik = silnia(8) * silnia(8)
zbior_rozwiazan = []
for liczba in liczby:
    if(len(liczba) != 8):
        continue
    _liczba = liczba[1:]
    print(liczba)
    mianownik = oblicz_mianownik(_liczba)
    if mianownik == najmniejszy_mianownik:
        zbior_rozwiazan.append(liczba)
    if mianownik < najmniejszy_mianownik:
        zbior_rozwiazan = []
        zbior_rozwiazan.append(liczba)
        najmniejszy_mianownik = mianownik

print(zbior_rozwiazan)