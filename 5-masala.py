import os
os.system("cls")

car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

eng_kop = max(car_count, key=car_count.get)
eng_kam = min(car_count, key=car_count.get)

print("Eng ko‘p sotilgan mashina:", eng_kop, "-", car_count[eng_kop], "ta")
print("Eng kam sotilgan mashina:", eng_kam, "-", car_count[eng_kam], "ta")

