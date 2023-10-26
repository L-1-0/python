# This code uses the faker module to generate synthetic data and uses the csv module to create a csv file

import csv
from faker import Faker

# Create a Faker object
fake = Faker()

# Specify the number of rows you want in your CSV file
num_rows = 100

# Define the CSV file name
csv_file = "fake_data.csv"

# Define the CSV field names (column headers)
field_names = ["Name", "Email", "Phone Number", "Address", "Date of Birth"]

# Generate and write the data to the CSV file
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

    # Write the header row
    writer.writeheader()

    # Generate and write fake data for each row
    for _ in range(num_rows):
        data = {
            "Name": fake.name(),
            "Email": fake.email(),
            "Phone Number": fake.phone_number(),
            "Address": fake.address(),
            "Date of Birth": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
        }
        writer.writerow(data)

print(f"{num_rows} rows of fake data have been written to {csv_file}")

