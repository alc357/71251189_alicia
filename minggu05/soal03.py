farenheit = lambda cel : 9/5 * cel + 32
Remaur = lambda cel : 0.8 * cel 

C = int(input("suhumu dalam celicius : "))

print(f"suhumu F = {farenheit(C):.2f}")
print(f"suhumu R = {Remaur(C):.2f}")