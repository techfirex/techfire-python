# writer, DictWriter
from csv import writer

with open("file3.csv", "w", newline="") as f:
    csv_writer = writer(f)

    # methods - writerow and writerows
    # writerow
    # csv_writer.writerow(["name","country"])
    # csv_writer.writerow(["Tushar","India"])
    # csv_writer.writerow(["Nupur","India"])

    # writerows
    csv_writer.writerows([["name","country"], ["Tushar","India"], ["Nupur","India"]])