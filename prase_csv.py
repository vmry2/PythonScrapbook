import csv

with open("fake_csv.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # next(csv_reader)

    # for line in csv_reader:
    # print(line[2])
    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)

