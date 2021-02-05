# Latihan Konversi Satuan Temperatur

print("\nPROGRAM KONVERSI TEMPERATUR")
'''
Konversi Celcius
'''
print("\nKONVERSI SATUAN CELCIUS")
SuhuC = float(input("Masukkan temperatur dalam celcius: "))
konv1 = SuhuC * (4/5)
konv2 = ((9/5)*SuhuC) + 32
konv3 = SuhuC + 273
print("Konversi C >> R = ", konv1)
print("Konversi C >> F = ", konv2)
print("Konversi C >> K = ", konv3)

'''
Konversi Reamur
'''
print("\nKONVERSI SATUAN REAMUR")
suhuR = float(input("Masukkan temperatur dalam reamur: "))
konv4 = suhuR * (5/4)
konv5 = ((9/4)*suhuR) + 32
konv6 = konv4 + 273
print("Konversi R >> C = ", konv4)
print("Konversi R >> F = ", konv5)
print("Konversi R >> K = ", konv6)

'''
Konversi Fahrenheit
'''
print("\nKONVERSI SATUAN FAHRENHEIT")
suhuF = float(input("Masukkan temperatur dalam fahrenheit: "))
konv7 = (suhuF - 32) * (5/9)
konv8 = (suhuF - 32) * (4/9)
konv9 = konv7 + 273
print("Konversi F >> C = ", konv7)
print("Konversi F >> R = ", konv8)
print("Konversi F >> K = ", konv9)

'''
Konversi Kelvin
'''
print("\nKONVERSI SATUAN KELVIN")
suhuK = float(input("Masukkan temperatur dalam kelvin: "))
konv10 = suhuK - 273
konv11 = (4/5) * (konv10)
konv12 = ((9/5)*konv10) + 32
print("Konversi K >> C = ", konv10)
print("Konversi K >> R = ", konv11)
print("Konversi K >> F = ", konv12)

## ENDING THE PROGRAM
print()
close = input("Press enter key to close...")
print()

import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, "Thanks, have a great day!", "Temperature Converter")
