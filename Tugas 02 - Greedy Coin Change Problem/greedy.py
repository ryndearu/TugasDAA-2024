def coin_change_greedy(X, arr):
    # Urutkan koin dari yang terbesar
    arr.sort(reverse=True)
    
    result = {}
    
    for coin in arr:
        if X >= coin:
            count = X // coin
            X = X % coin
            result[coin] = count
    
    return result

# Meminta input array nilai koin dari user
print("Masukkan nilai koin (pisahkan dengan spasi, contoh: 100 200 500 1000)")
while True:
    try:
        arr = list(map(int, input().split()))
        if len(arr) == 0:
            print("Masukkan setidaknya satu nilai koin.")
        elif any(coin <= 0 for coin in arr):
            print("Semua nilai koin harus positif. Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat positif, pisahkan dengan spasi.")

# Meminta input jumlah uang dari user
while True:
    try:
        X = int(input("Masukkan jumlah uang: "))
        if X < 0:
            print("Jumlah uang harus positif. Silakan coba lagi.")
        else:
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat positif.")

# Panggil fungsi
solution = coin_change_greedy(X, arr)

# Cetak hasil
print("\nSolusi coin change:")
for coin, count in solution.items():
    print(f"{count} koin bernilai {coin}")

# Cetak total koin
total_coins = sum(solution.values())
print(f"\nTotal koin yang digunakan: {total_coins}")

# Cek apakah semua uang telah ditukar
remaining = X - sum(coin * count for coin, count in solution.items())
if remaining > 0:
    print(f"\nPeringatan: {remaining} tidak dapat ditukar karena tidak ada koin yang sesuai.")