from csv import reader

with open("data.csv") as file:
    csv_file = reader(file)
    print(csv_file)
    for row in csv_file:
        print(row)
