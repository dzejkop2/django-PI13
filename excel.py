import csv
import random

arr = []

with open('ULICE.csv', mode ='r') as file:
    csvFile = csv.reader(file,delimiter=";")
    for lines in csvFile:
        arr.append(lines)

miesto = random.choice(arr)
print(miesto[0])
print(miesto[1])
print(miesto[2])