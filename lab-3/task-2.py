word = str(input("Введіть слово: "))

while(len(word) < 2):
    print("Слово повинно містити мінімум дві літери")
    word = str(input("Введіть слово: "))

current_symbol = word[0]
current_symbol_count = 1
max_symbol_count = current_symbol_count

for i in range(1,len(word)):
    if word[i] != current_symbol:
        if current_symbol_count > max_symbol_count:
            max_symbol_count = current_symbol_count
        current_symbol = word[i]
        current_symbol_count = 1
    else:
        current_symbol_count += 1

if current_symbol_count > max_symbol_count:
            max_symbol_count = current_symbol_count

print("Максимальна кількість символів, записаних підряд у слові: ", max_symbol_count)