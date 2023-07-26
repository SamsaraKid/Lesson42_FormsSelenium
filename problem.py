'''
Задание 4 Есть стопка оладий различного радиуса.
Единственная операция, проводимая с ними —
между любыми двумя суем лопатку и меняем порядок оладий над лопаткой на обратный.
Необходимо за минимальное количество операций таких отсортировать снизу вверх по убыванию радиуса.
'''

import random

arr0 = []
for i in range(10):
    arr0.append(random.randint(1, 9))

print(arr0)

def lopatka(i, arr):
    arr1 = arr[:i]
    arr2 = arr[i:]
    arr2.reverse()
    return arr1 + arr2

i = 0
while True:
    if arr0[i] > arr0[i + 1]:
        if i == 0:
            arr0.reverse()
        else:
            arr0 = lopatka(i - 1, arr0)
    print(arr0)
    if i == len(arr0) - 2:
        i = 0
    else:
        i += 1