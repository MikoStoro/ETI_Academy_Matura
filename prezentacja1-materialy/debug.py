def example_function():
    print("Line 1 in function")
    print("Line 2 in function")

print("Message1")
print("Message2")
variable1 = 123
print(variable1)
text = "Variable is "
variable1 = 456
print(text + str(variable1))


#step into
example_function()
#step over
example_function()

#podczas tej petli mozna zatrzymac program
for i in range(1000000000):
    print(i)

