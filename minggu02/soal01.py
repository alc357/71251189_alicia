#tinggi badan harus dalam meter
tinggi_badan = float (input("Berapa tinggi badanmu dalam meter? "))

#BMI harus dalam kg/m^2
BMI = float (input("Berapa BMI mu? "))

#menghitung berat badan
berat_badan = round(BMI * (tinggi_badan**2), 2)

print (f"Berat badanmu = {berat_badan} kg")

