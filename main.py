n = int(input('Masukkan bilangan bulat antara 3 dan 9: '))

while n < 3 or n > 9:
    print('Bilangan tidak valid!')

    n = int(input('Masukkan bilangan bulat antara 3 dan 9: '))

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(' ', end='')

    for j in range(1, 2 * i):
        print(n, end='')

    print()
