import random


def quick_sort(array):

    if len(array) <=1:
        return array

    pivot = array[int(len(array)/2)]
    left = [element for element in array if element < pivot]
    center = [element for element in array if element == pivot]
    right = [element for element in array if element > pivot]

    return quick_sort(left) + center + quick_sort(right)

def quick_sort_demonstration():
    list_size = int(input("Введіть розмір списку: "))
    list = [random.randint(1,1000) for i in range(list_size)]

    print("Список до сортування: ")
    print(list)

    print("Список після сортування: ")
    print(quick_sort(list))

    return

quick_sort_demonstration()