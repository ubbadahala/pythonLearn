# Kalkulator Distribusi Temperatur Dinding Silinder
import math
print("\nSelamat Datang di Penghitung\nDistribusi Temperatur Dinding Silinder!")

def main():
    Ts1 = float(input("\nMasukkan nilai Ts1: "))
    Ts2 = float(input("Masukkan nilai Ts2: "))
    r1 = float(input("Masukkan nilai r1: "))
    r2 = float(input("Masukkan nilai r2: "))
    r = float(input("Masukkan nilai r: "))
    Tr = ((Ts1 - Ts2)/math.log(r1/r2)) * math.log(r/r2) + Ts2
    print("\nNilai Tr yang didapatkan adalah:")
    print(Tr, "°C")

while True:
    main()
    if input("\nRepeat the program? (Y/N): ").strip().upper() != 'Y':
        break
