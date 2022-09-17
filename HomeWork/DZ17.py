li = [-2, 3, 8, -11, -4, 6]

print('Вычислить количество отрицательных чисел в списке', li)

def negative_elements(li1):
    if not li1:
        return 0
    else:
        count = negative_elements(li1[1:])
        if li1[0] < 0:
            count += 1
        return count


print('n = ', negative_elements(li))
