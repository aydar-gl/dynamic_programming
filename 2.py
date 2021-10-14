import numpy as np

weights = [[[3, 5]], [[4, 2], [4, 9]], [[10, 10], [4, 7], [6, 5]], [[999, 7], [2, 2], [8, 1], [1, 999]], [[999, 5], [7, 1], [3, 999]], [[999, 3], [4, 999]]]
vershina = np.zeros((4,4), dtype=int)

for j in range(1, vershina.shape[1]):
    vershina[0, j] = vershina[0, j - 1] + weights[j - 1][0][0]
for i in range(1, vershina.shape[0]):
    vershina[i, 0] = vershina[i - 1, 0] + weights[i - 1][len(weights[i - 1]) - 1][len(weights[i - 1][len(weights[i - 1]) - 1]) - 1]

for i in range(1, vershina.shape[0] - 1):
    for j in range(1, vershina.shape[1] - 1):
        vershina[i,j] = min(vershina[i-1,j] + weights[i + j - 1][i - 1][1], vershina[i,j - 1] + weights[i + j - 1][i][0])

offset = 0
for i in range(1, vershina.shape[0] - 1):
    if len(weights[i + len(vershina) - 2]) < len(weights[i + len(vershina) - 3]):
        offset += 1
    vershina[i, vershina.shape[1] - 1] = min(vershina[i - 1, vershina.shape[1] - 1] + weights[i + vershina.shape[1] - 2][i - 1 - offset][1], vershina[i, vershina.shape[1] - 2] + weights[i + vershina.shape[1] - 2][i - offset][0])

offset = 0
for j in range(1, vershina.shape[1]):
    if len(weights[j + len(vershina) - 2]) < len(weights[j + len(vershina) - 3]):
        offset += 1
    vershina[vershina.shape[0] - 1, j] = min(vershina[vershina.shape[0] - 2, j] + weights[j + vershina.shape[0] - 2][vershina.shape[0] - 2 - offset][1], vershina[vershina.shape[0] - 1, j - 1] + weights[j + vershina.shape[0] - 2][vershina.shape[0] - 1 - offset][0])

otvet = np.zeros((vershina.shape[0],vershina.shape[1]), dtype=int)
m = n = 0
for i in range(0, vershina.shape[0]):
    for j in range(vershina.shape[1] - 1, -1, -1):
        otvet[n, m] = vershina[i, j]
        m += 1
    n += 1
    m = 0
print(otvet)

m = 0
n = otvet.shape[0] - 1
print('[', n, ',', m, ']', 'элемент = ', otvet[n, m])
for i in range(0, len(weights)):
    if m == otvet.shape[1] - 1:
        n -= 1
    elif n == 0:
        m += 1
    else:
        if otvet[n - 1, m] > otvet[n, m + 1]:
            m += 1
        else:
            n -= 1
    print('[', n, ',', m, ']', 'элемент =', otvet[n, m])
