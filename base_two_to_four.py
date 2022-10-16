### CONVERTING BASE 2 TO BASE 10

# collect user input

value = input("Enter the binary value: ")

# convert from 2 to 10
def two_to_ten(value, pow_value = 0, eval=[]):
    # returns a list 

    for i in value:
        num = 2**pow_value
        num = int(i) * num
        eval.append(num)
        pow_value += 1

    num = 0
    
    for x in eval:
        num += x
    return num

# converter from base 10 to another base
def converter(value, base, binary_values = [], reminder = 0, divided_value = 0, count = 0):

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

base_10 = two_to_ten(value=value)

result = converter(value=base_10, base=4)

base_4 = result[::-1]

start = 0

for i in base_4:
    if i > 0:
        start = base_4.index(i)
        break

print("The result is: ")
for i in base_4[start:]:
    print(i, end="")


# show result