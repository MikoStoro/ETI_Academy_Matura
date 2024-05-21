file = open("informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki/sufiks_4.txt")
lines = file.readlines()
for s in lines:
    slowo = s.split(" ")[1]
    najmniejszy_sufiks = slowo
    for i in range(len(slowo)-1):
        sufiks = slowo[i:]
        if sufiks < najmniejszy_sufiks:
            najmniejszy_sufiks = sufiks
    print(najmniejszy_sufiks)