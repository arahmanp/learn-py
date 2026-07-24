import sys

# 1. Objek baru dibuat
x = ["Python", "2026"]
print(sys.getrefcount(x))  # Output: 2 (x + argumen fungsi)

# 2. Kita tambah dua variabel baru yang menunjuk ke objek yang sama
y = x
z = x
print(sys.getrefcount(x))  # Output: 4 (x, y, z + argumen fungsi)

# 3. Kita hapus satu referensi menggunakan 'del'
del y
print(sys.getrefcount(x))  # Output: 3 (x, z + argumen fungsi)