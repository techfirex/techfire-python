from csv import reader

with open("file.csv","r") as f:
    csv_reader = reader(f) # reader function from csv module
    # csv_reader is iterator object so we can loop ones on it, for many time run loop convert it into list
    next(csv_reader) # next func does not show heading
    for raw in csv_reader: 
        print(raw)