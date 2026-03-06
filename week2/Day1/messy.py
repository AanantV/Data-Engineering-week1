import csv

def messy():

    filename = "Week 2/Day 1/messy.csv"

    data = []
    seen_names = set()

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        #header = next(reader)
        for row in reader:

            {k.strip(): v.strip() for k,v in row.items()}

            if not all(row.values()):
                continue

            seen_id = row['Product'].lower().title()

            if seen_id not in seen_names:
                row['Product'] = row['Product'].lower().title()
                row['Price'] = float(row['Price'])
                row['Rating'] = float(row['Rating'])

                data.append(row)
                seen_names.add(seen_id)

        print(f"Total rows available: {len(data)}")
        for item in data:
            print(item)

messy()