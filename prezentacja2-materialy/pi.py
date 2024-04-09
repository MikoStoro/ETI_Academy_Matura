file = open("informatyka-2023-maj-matura-rozszerzona-zalaczniki/Dane_2305/pi_przyklad.txt")

numbers = file.readlines() #kazda linia zawiera jedną cyfrę
last = int(numbers[0]) #upewnijmy sie, że python odczytal liczbe, nie napis
result = 0
for n in numbers[1:]:
    current = int(n)
    if last*10 + current > 90:
        result +=1
    last = current

print(result)
