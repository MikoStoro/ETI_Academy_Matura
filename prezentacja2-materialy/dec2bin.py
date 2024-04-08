def print_bin(bin):
    dec_arr = []
    while(bin > 0):
        dec_arr.insert(0, str(bin % 2))
        bin //= 2
    print("".join(dec_arr))




number = 12435667832
print_bin(number)

blocks = 0
last = -1  #kazda cyfra bedzie rozna od -1
while number > 0:
    digit = number % 2
    if(last != digit):
        blocks += 1
    last = digit
    number //= 2

print("Counted " + str(blocks) + " blocks")