file = open("informatyka-2023-maj-matura-rozszerzona-zalaczniki/Dane_2305/bin_przyklad.txt")
numbers = file.readlines()
largest = -1
for x in numbers:
    number = int(x) #inaczej bedziemy sortować alfabetycznie
    if number > largest:
        largest = number

print(largest)