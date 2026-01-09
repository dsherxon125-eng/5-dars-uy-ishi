import os
os.system("cls")

professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}

ism = input("Ism kiriting: ")

if ism in professions:
    print(f"{ism} kasbi: {professions[ism]}")
else:
    print("Bu shaxs haqida ma'lumot topilmadi.")
