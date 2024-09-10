def insertAfter():
    input_list = list(map(int, input("Введіть список: ").split()))
    print(input_list)

    value = int(input("Введіть значення, яке потрібно вставити: "))
    element_before_insert = int(input("Введіть елемент, після якого треба вставити значення: "))

    result = []

    for element in input_list:
        result.append(element)
        if element == element_before_insert:
            result.append(value)
    
    print(result)
    return result 
    
insertAfter()