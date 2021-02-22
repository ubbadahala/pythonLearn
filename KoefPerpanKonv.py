# Kalkulator Koefisien Perpindahan Panas Konveksi (h)
import math
print("\nSelamat Datang di Penghitung\nKoefisien Perpindahan Panas Konveksi")
print("*)Kalkulator ini menggunakan prinsip tahanan termal dinding silinder")

def main():
    Ti = float(input("\nMasukkan nilai Ti: "))
    Tinf = float(input("Masukkan nilai T∞: "))
    q = float(input("Masukkan nilai q: "))
    r0 = float(input("Masukkan nilai r0: "))
    r1 = float(input("Masukkan nilai r1: "))
    k = float(input("Masukkan nilai k: "))
    L = float(input("Masukkan nilai L: "))
    A = float(input("Masukkan nilai A: "))
    h0 = 1/((((Ti-Tinf)/q)-((math.log(r0/r1))/(2*math.pi*k*L)))*A) 
    print("\nNilai h0 yang didapatkan adalah:")
    print(h0, "W/m2K")

while True:
    main()
    if input("\nRepeat the program? (Y/N): ").strip().upper() != 'Y':
        break