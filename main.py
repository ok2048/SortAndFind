# Сортировка методом вставки
def insertion_sort(arr):
    # Сортировку начинаем со второго элемента
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        # Просматриваем отсортированную часть слева от элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вправо, пока не найдем место
        # для вставки текущего элемента
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем элемент
        arr[j + 1] = item_to_insert


# Модифицированный двоичный поиск. Подфункция, которая будет использоваться
# в основной функции поиска
def modified_binary_search(arr, element, left, right):
    middle = (right + left) // 2  # находимо середину
    if arr[middle] < element and arr[middle + 1] >= element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element <= arr[middle]:  # если элемент меньше или равен элементу в середине
        # рекурсивно ищем в левой половине
        return modified_binary_search(arr, element, left, middle - 1)
    else:  # иначе в правой
        return modified_binary_search(arr, element, middle + 1, right)


# Определение позиции элемента списка arr, который меньше заданного числа num,
# а следующий за ним больше или равен этому числу
# Если первый элемент списка arr[0] тоже >= num, то возвращаем -1
def position_to_insert(arr, num):
    # Проверяем первый и последний элементы. Если первый >= num, возвращаем -1.
    # Если последний < num, возвращаем его индекс.
    # Если оба этих условия не выполняются, т.е. arr[0]<num and arr[len]>=num,
    # то искать нужно где-то между ними
    j = len(arr) - 1
    if arr[0] >= num:
        return -1
    elif arr[j] < num:
        return j
    else:
        return modified_binary_search(arr, num, 0, j)


# Вводим список для сортировки
print('Введите последовательность целых чисел через пробел.')
print('Enter - окончание ввода.')
while True:
    input_str = input('>>')
    list_of_str = input_str.split(' ')
    try:
        list_of_int = list(map(int, list_of_str))
        break
    except ValueError:
        print('Список содержит некорректные значения. Повторите ввод')

# Сортируем введенный список и выводим его на экран
insertion_sort(list_of_int)
print('Отсортированный список:')
print(list_of_int)

# Вводим теперь число, для которого будет осуществляться поиск позиции
print('Теперь введите любое целое число.')
while True:
    input_str = input('>>')
    try:
        int_to_find = int(input_str)
        break
    except ValueError:
        print('Введено некорректное значение. Повторите ввод')

# Находим позицию элемента списка, который меньше введенного числа,
# а следующий за ним больше или равен этому числу,
# и выводим его на экран
print(f'''Позиция элемента списка, который меньше числа {int_to_find},
а следующий за ним больше или равен этому числу: ''',
      position_to_insert(list_of_int, int_to_find))
