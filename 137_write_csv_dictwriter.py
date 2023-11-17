from csv import DictWriter

with open("file4.csv", "w", newline="") as f:
    csv_writer = DictWriter(f, fieldnames=["firstname", "lastname", "age"])

    csv_writer.writeheader()

    # methods - writerow and writerows

    # writerow
    # csv_writer.writerow({
    #     "firstname":"tushar",
    #     "lastname":"makwana",
    #     "age":21 
    # })
    # csv_writer.writerow({
    #     "firstname":"nupur",
    #     "lastname":"vyas",
    #     "age":21 
    # })

    # writerows - [dict, dict ...] // inside function list, inside list dict
    csv_writer.writerows([
        {"firstname":"tushar", "lastname":"makwana", "age":21 },
        {"firstname":"nupur", "lastname":"vyas", "age":21 }
    ])