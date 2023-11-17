from csv import DictReader
# this give ordered dict - better than reader func

with open("file2.csv","r") as f:
    csv_reader = DictReader(f, delimiter="|")
    print(csv_reader)

    for raw in csv_reader:
        # print(raw)
        print(raw['name'])