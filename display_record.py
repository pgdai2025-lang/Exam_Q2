import csv

def display_housing_record(filename):
    try:
        with open(filename, mode='r') as file:
            # Use DictReader to map information to column headers
            reader = csv.DictReader(file)
            
            # Fetch the first record
            record = next(reader)
            
            print("--- California Housing Record ---")
            for key, value in record.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_housing_record('housing.csv')
