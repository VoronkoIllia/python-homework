def get_fibonacci_set(end_value):

    fibonacci_list = []
    current_index = 0

    while True:
        current_element = current_index if current_index<3 else fibonacci_list[current_index-2] + fibonacci_list[current_index-1]
        if current_element > end_value:
            break
        else:
            fibonacci_list.append(current_element)
        current_index += 1

    return set(fibonacci_list)

def fibonacci_count():
    set_of_numbers = set(range(1,51))
    set_of_fibonacci = get_fibonacci_set(50)
    print(len(set_of_numbers & set_of_fibonacci))

    return

fibonacci_count()
