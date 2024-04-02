import os
import string
import random

os.system('cls')

i = 0

data_mapel = []

while True:
    data_01 = ('mata pelajaran', 'guru', 'hari', 'jam', 'ruangan')
    data = {}
    
    for key in data_01:
        data[key] = input(f"{key.capitalize()}\t: ")
    
    next = input("Lanjut (Y/N)? ").lower()
    code = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
    i += 1  
    
    data_mapel.append({
        'code': code,
        'data': data,
    })
    
    if next == 'y':
        print("-" * 50)
        continue
    if next == 'n':
        print(f'{"ID":<7} {"Mata Pelajaran":<20} {"Guru":<15} {"Hari":<5} {"Jam":<5} {"Ruangan":<10}')
        print("-" * 50)
        for key, value in enumerate(data_mapel):
         print(f"{value['code']:<7} {value['data']['mata pelajaran']:<20} {value['data']['guru']:<15} {value['data']['hari']:<5} {value['data']['jam']:<5} {value['data']['ruangan']:<10}")
        break
    else:
        print("Error !")
        break