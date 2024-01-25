import csv # Imports the csv library
total = 0

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 

  for row in reader:
    total += float(row["Cost"]) * float(row["Quantity"])

print("🌟Shop $$ Tracker🌟")
print()
print(f"Your shop took ${round(total,2)} pounds today.")