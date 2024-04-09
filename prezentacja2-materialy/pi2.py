file = open("informatyka-2023-maj-matura-rozszerzona-zalaczniki/Dane_2305/pi_przyklad.txt")

def get_fragment(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

results = []
for i in range(100):
    results.append(0)



numbers = file.readlines() #kazda linia zawiera jedną cyfrę
last = int(numbers[0]) #upewnijmy sie, że python odczytal liczbe, nie napis
for n in numbers[1:]:
    current = int(n)
    fragment = last*10 + current
    results[fragment] += 1
    last = current

#znajdzmy skrajne elementy
smallest_index = 0
smallest = results[0]
largest_index = 0
largest = results[0]

for i in range(100):
    #stosujac <, a nie <= upewnimy sie, ze tylko uwzglednimy tylko pierwszy wynik
    if results[i] < smallest:
        smallest = results[i]
        smallest_index = i
    if results[i] > largest:
        largest = results[i]
        largest_index = i


print(get_fragment(smallest_index))
print(smallest)
print(get_fragment(largest_index))
print(largest)

