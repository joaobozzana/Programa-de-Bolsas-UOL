import csv

animais = ["Gato", "Cachorro", "Beija-Flor", "Leao", "Tucano", "Onça", "Girafa", "Lagarto", "Capivara", "Jacare",
           "Cavalo", "Vaca", "Galinha", "Pato", "Peixe", "Tatu", "Cobra", "Tartaruga", "Tubarao"]

animais.sort()
[print(animal) for animal in animais]

with open("animais.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    for animal in animais:
        writer.writerow([animal])
