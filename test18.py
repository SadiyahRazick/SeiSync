dlist = [1, 2, 3, 4, 5, 6, 7]
n = 3
summ = dlist[-1]
print(summ)
for i in range(1, n):
    summ = summ + dlist[-1-i]
print(summ)
