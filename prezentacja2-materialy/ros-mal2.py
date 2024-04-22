def czy_ros_mal(series):
    mal = False
    if not (series[0] < series[1]):
        return False

    for i in range(1, len(series) - 1):
        if mal:
            if not (series[i] > series[i + 1]):
                return False
        else:
            if not (series[i] < series[i + 1]):
                mal = True
    return True


file = open("informatyka-2023-maj-matura-rozszerzona-zalaczniki/Dane_2305/pi_przyklad.txt")

numbers = file.readlines()
numbers = [int(x) for x in numbers]

#minimalna dlugosc ciagu to 3
curr_index = 0
curr_len = 3

max_index = -1
max_len = -1

while (curr_index + curr_len < len(numbers)):
    slc = numbers[curr_index:curr_index + curr_len]
    if czy_ros_mal(slc):
        if curr_len > max_len:
            max_index = curr_index
            max_len = curr_len
        curr_len += 1
    else:
        curr_index += 1
        curr_len = 3
print(numbers[max_index:max_index + max_len])


