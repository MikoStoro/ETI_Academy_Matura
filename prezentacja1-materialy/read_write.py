write_file = open('example1.txt', 'w')
write_file.write("aaaaa\nbbbbb\ncccccc\nddddd")
write_file.close()


read_file = open('example1.txt', 'r')
print(read_file.read())
read_file.close()

write_file = open('example1.txt', 'a')
write_file.write("\neeeeee\nfffffff")
write_file.close()

read_file = open('example1.txt', 'r')
print(read_file.read())
read_file.close()

write_file = open('example1.txt', 'w')
write_file.write("xxxxx\nyyyyy\nzzzzz")
write_file.close()

read_file = open('example1.txt', 'r')
print(read_file.read())
read_file.close()
