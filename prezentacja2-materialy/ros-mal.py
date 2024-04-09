
def czy_ros_mal(series):
    mal = False
    if not(series[0] < series[1]):
        return False

    for i in range(1, 5):
        if mal:
            if not(series[i] > series[i+1]):
                return False
        else:
            if not(series[i] < series[i+1]):
                mal = True
    return True

file = open("informatyka-2023-maj-matura-rozszerzona-zalaczniki/Dane_2305/pi_przyklad.txt")

numbers = file.readlines()
numbers = [int(x) for x in numbers]

num_of_series = 0
for i in range(len(numbers)-6):
    slc = numbers[i:i + 6]
    res = czy_ros_mal(slc)
    if res:
        num_of_series += 1
        print(slc)
        print(res)

print(num_of_series)


