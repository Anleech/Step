def change(lst):
    print(lst)
    first = lst[0]
    last = lst[-1]
    lst2 = lst[1:-1]
    lst2.append(first)
    lst2.insert(0, last)
    return lst2


n = [1, 2, 3]
print(change(n))
print()

n = [9, 12, 22, 54, 105]
print(change(n))
print()

n = ['с', 'л', 'о', 'н']
print(change(n))
