plik1 = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/slowa1.txt")
plik2 = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/slowa2.txt")
plik3 = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/slowa3.txt")

aktualny_plik = plik1

aktualny_plik = aktualny_plik.readlines()
slowo = aktualny_plik[1].strip()
k1 = int(aktualny_plik[2].split(" ")[0]) - 1
k2 = int(aktualny_plik[2].split(" ")[1]) - 1

sufiks1 = slowo[k1:]
sufiks2 = slowo[k2:]
print("s1: " + sufiks1 + " s2: " + sufiks2)
print(sufiks1<sufiks2)


