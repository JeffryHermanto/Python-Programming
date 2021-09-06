# Working With CSV Files

import csv

# with open("09 Python Standard Library/06_working_with_csv_files/data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1000, 2, 15])

with open("09 Python Standard Library/06_working_with_csv_files/data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
