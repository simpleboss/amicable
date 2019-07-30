input_number = int(input())
# input_number = 500
saved_list = []


def return_divisor_sum(nb):
    result_sum = 1
    i = 2
    while i * i < nb:
        if nb % i == 0:
            result_sum += i + nb // i
        i += 1
    return result_sum


for j in range(2, input_number + 1):
    sum_of_j = return_divisor_sum(j)
    sum_of_k = return_divisor_sum(sum_of_j)
    if j == sum_of_k and j != sum_of_j:
        result = sorted([j, sum_of_j])
        if result not in saved_list:
            saved_list.append(result)
            print(result[0], result[1])
