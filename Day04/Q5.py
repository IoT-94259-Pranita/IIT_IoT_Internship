conversion=[lambda tonnes:tonnes*1000,lambda kg:kg*1000,lambda gm:gm*1000,lambda mg:mg/453592.37]
tonnes=float(input("Enter weight of tonnes:"))

kg=conversion[0](tonnes)
gm=conversion[1](kg)
mg=conversion[2](gm)
lbs=conversion[3](mg)

print(f"{kg}kg")
print(f"{gm}gm")
print(f"{mg}mg")
print(f"{lbs}lbs")

