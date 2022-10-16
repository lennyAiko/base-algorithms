### CONVERTING BASE 10 TO BASE 2

# collect user input

value = int(input("Enter value you want to convert to binary: "))

# perform modulos operation

def converter(value, base=2, binary_values = [], reminder = 0, divided_value = 0, count = 0):

    for i in range(value-1):
        if count < 1:
            divided_value = value // base
            reminder = value % base
            count += 1
            binary_values.append(reminder)
        reminder = divided_value % base
        divided_value = divided_value // base
        binary_values.append(reminder)
    return binary_values

print(f"The binary conversion of {value} is: ", end="")

binary = converter(value=value)

binary = binary[::-1]

start = binary.index(1)

for i in binary[start:]:
    print(i, end="")
