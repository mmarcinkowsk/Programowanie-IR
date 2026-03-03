#!/usr/bin/python3

masa = float(input("Podaj masę w kilogramach:"))
wzrost = float(input("Podaj wzrost w metrach:"))

bmi = masa/(wzrost**2)

print(f"BMI wynosi {bmi}")

if bmi < 18.5:
    print("Niedowaga")
elif bmi<25:
    print("Waga prawidłowa")
elif bmi < 30:
    print("Nadwaga")
else:
    print("Otyłość")
