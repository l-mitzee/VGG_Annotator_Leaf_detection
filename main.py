import csv
import json

# Define the CSV file path
csv_file = 'Leaf_diseases_detection.csv'

# Define the output CSV file path
output_csv_file = 'output_file.csv'

# Define the column names for the output CSV file
output_columns = ['file_name', 'file_size', 'region_count', 'region_id', 'shape_name', 'x', 'y', 'width', 'height','Type', 'Description', 'Image_Quality']

def main():
    # Open the input and output CSV files
    with open(csv_file, 'r') as input_file, open(output_csv_file, 'w', newline='') as output_file:
        # Create CSV reader and writer objects
        csv_reader = csv.DictReader(input_file)
        csv_writer = csv.writer(output_file)

        # Write the header row to the output CSV file
        csv_writer.writerow(output_columns)

        # Process each row in the input CSV file
        for row in csv_reader:
            # Parse the region_attributes JSON string into a dictionary
            try:
                region_attributes = json.loads(row['region_attributes'])
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", row['region_attributes'])
                print("Error message:", str(e))
                continue

            # Extract shape attributes from region_shape_attributes
            shape_attributes = json.loads(row['region_shape_attributes'])

            # Create a new row with the required values
            new_row = [
                row['filename'],
                row['file_size'],
                row['region_count'],
                row['region_id'],
                shape_attributes.get('name', ''),
                shape_attributes.get('x', ''),
                shape_attributes.get('y', ''),
                shape_attributes.get('width', ''),
                shape_attributes.get('height', ''),
                region_attributes.get('Type', ''),
                region_attributes.get('Description', ''),
                region_attributes.get('Image_Quality', '')
            ]

            # Write the new row to the output CSV file
            csv_writer.writerow(new_row)

    # Print a message when the processing is complete
    print('CSV processing complete.')

if __name__ == "__main__":
    main()
