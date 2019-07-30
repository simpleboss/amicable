input_number = int(input())
result = []

for i in range(1, input_number + 1):
    divisor1_sum = 0
    for divisor in range(1, i):
        if i % divisor == 0:
            divisor1_sum += divisor

    divisor2_sum = 0
    for divisor in range(1, divisor1_sum):
        if divisor1_sum % divisor == 0:
            divisor2_sum += divisor

    if i == divisor2_sum and i != divisor1_sum:
        if not sorted([i, divisor1_sum]) in result:
            result.append(sorted([i, divisor1_sum]))
            print(result[-1][0], result[-1][1])
