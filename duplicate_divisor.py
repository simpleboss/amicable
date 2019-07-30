input_number = 220
result = 0
for i in range(1, input_number):
    if input_number % i == 0:
        result += i

print(result)

result2 = 1
for i in range(2, input_number):
    if i*i < input_number:
        if input_number % i == 0:
            result2 += i
            print(i, input_number //i)
            result2 += input_number // i
            print(result2)

print(result2)
