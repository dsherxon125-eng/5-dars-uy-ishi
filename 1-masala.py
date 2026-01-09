import os
os.system("cls")

cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}

eng_qimmat = max(cars, key=cars.get)
eng_arzon = min(cars, key=cars.get)

ortacha_narx = sum(cars.values()) / len(cars)

print(f"Eng qimmat avtomobil: {eng_qimmat} - ${cars[eng_qimmat]}")
print(f"Eng arzon avtomobil: {eng_arzon} - ${cars[eng_arzon]}")
print(f"Avtomobillarning o'rtacha narxi: ${ortacha_narx}")
