plik1 = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/slowa1.txt")
plik2 = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/slowa2.txt")
plik3 = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/slowa3.txt")
aktualny_plik = plik1
aktualny_plik = aktualny_plik.readlines()

def czy_mniejszy(n,s,k1,k2):
    sufiks1 = s[k1:]
    sufiks2 = s[k2:]
    return sufiks1 < sufiks2

slowo = aktualny_plik[1].strip()

tablica = []
slowo = "mascarpone"
for i in range(len(slowo)):
    tablica.append(0)

for i in range(len(slowo)):
    sufiks = slowo[i:]
    pozycja = 0
    for j in range(len(slowo)):
        if czy_mniejszy(len(slowo), slowo, j, i):
            pozycja += 1
    #print(sufiks + ": " +str(pozycja))
    tablica[pozycja] = (i+1) # liczymy od 1

print(tablica)


