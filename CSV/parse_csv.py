import csv

# with open("fake_csv.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # next(csv_reader)

#     # for line in csv_reader:
#     # print(line[2])
#     with open("new_names.csv", "w") as new_file:
#         csv_writer = csv.writer(new_file, delimiter="\t")

#         for line in csv_reader:
#             csv_writer.writerow(line)


html_output = ""
names = []

with open("customers.csv", "r") as data_file:
    csv_data = csv.DictReader(data_file)

    for line in csv_data:
        names.append(f"{line['FirstName']} {line['LastName']}")

    # skip first line (header) of CSV
    # next(csv_data)

    # for line in csv_data:
    #     names.append(f"{line[0]} {line[1]}")

html_output += (
    f"<p>There are currently {len(names)} public contributors.  Thank you!</p>"
)

html_output += "\n<ul>"

for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += f"\n</ul>"

print(html_output)

# for name in names:
#     print(name)
