import random
import pandas as pd

commands = {
    'Astralis': [16, 29, 3, 2, 19],
    'NaVi': [6, 11, 25, 12, 29],
    'FaZe': [13, 27, 4, 22, 8], 
    'Liquid': [6, 4, 13, 11, 15], 
    'Monte': [2, 11, 18, 4, 20], 
    'Vitality': [2, 14, 11, 22, 9], 
    'ENCE': [24, 27, 22, 28, 3], 
    'mousesports': [3, 27, 22, 3, 15], 
    'fnatic': [19, 12, 11, 3, 21]
}
df = pd.DataFrame(commands)
print(df)

while True:
    command_name = input("Введіть ім'я команди: ")
    if not command_name in commands:
        print("Такої команди немає! Спробуйте ще раз")
    else:
        break

print(df[command_name])
print(f'Середній бал команди {command_name}: ', df[command_name].mean())
print(f'Максимальний бал команди {command_name}: ', df[command_name].max())
print(f'Мінімальний бал команди {command_name}: ', df[command_name].min())
print(f'Сума балів команди {command_name}: ', df[command_name].sum())
print(f'Медіанний бал команди {command_name}: ', df[command_name].median())
