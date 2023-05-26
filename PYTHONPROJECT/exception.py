import csv 

filename = "astronauts.csv" 

try: 
    with open(filename) as file: 
        reader = csv.reader(file) 
        for row in reader: print(row) 
except FileNotFoundError:
    print(f"File {filename} not found.") 
except Exception as e: print(f"Error reading file: {e}")
else: print("File read successfully.") 
finally: print("End of program.")
