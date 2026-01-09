import os
os.system("cls")

speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

sorted_speed = sorted(speed.items(), key=lambda x: x[1], reverse=True)

for car, spd in sorted_speed:
    print(f"{car} - {spd} km/soat")
