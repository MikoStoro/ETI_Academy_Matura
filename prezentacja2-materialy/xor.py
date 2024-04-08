def div2(num):
    return num//10
def xor(b1,b2):
    return (b1+b2)%2


file = open("informatyka-2023-maj-matura-rozszerzona-zalaczniki/Dane_2305/bin_przyklad.txt")
numbers = file.readlines()

for number in numbers:
    number = int(number)
    divided = div2(number)
    result = ""
    while(divided > 0 or number > 0):
        b1 = divided % 10
        b2 = number % 10
        number //= 10
        divided //= 10
        bit = xor(b1,b2)
        result = str(bit) + result
    print(result)
