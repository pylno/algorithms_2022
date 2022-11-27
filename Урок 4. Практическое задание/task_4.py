"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit


test_array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


print('func_1 -', timeit(f'func_1({test_array})', globals=globals()))
print(func_1(test_array))
print('-'*100)
print('func_2 -', timeit(f'func_2({test_array})', globals=globals()))
print(func_2(test_array))
print('-'*100)
print('func_3 -', timeit(f'func_3({test_array})', globals=globals()))
print(func_3(test_array))
print('-'*100)


"""
Получившиеся результаты:

func_1 - 1.018475299999409
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
----------------------------------------------------------------------------------------------------
func_2 - 1.3494993000058457
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
----------------------------------------------------------------------------------------------------
func_3 - 1.140531800003373
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
----------------------------------------------------------------------------------------------------

Уменьшения времени отработки нет, поскольку у функции max аналогичная сложность - O(N), 
которая совпадает со сложностью циклов.
"""


