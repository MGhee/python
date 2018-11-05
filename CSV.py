from csv import reader
with open("fighters.csv")  as file:
    csv_reader= reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

from csv import writer
with open ("cats.csv", "w") as file:
    csv_writer= writer(file)
    csv_writer.writerow(["name","age"])
    csv_writer.writerow(["betty","39"])