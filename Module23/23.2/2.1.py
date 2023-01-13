import os

# Function to handle file errors
def handle_file_error(err):
    if isinstance(err, FileExistsError):
        print("Error: File already exists.")
    elif isinstance(err, IsADirectoryError):
        print("Error: A directory was expected, but a file was given.")
    else:
        print("Error: Invalid file input.")

# Function to handle age errors
def handle_age_error(err):
    if isinstance(err, ValueError):
        print("Error: Invalid age value.")
    else:
        print("Error: Invalid data type.")

# Function to process the ages file and write to a new file
def process_ages(input_file, output_file):
    try:
        # Open the input file
        with open(input_file, "r") as file:
            # Open the output file
            with open(output_file, "w") as out_file:
                # Iterate through the lines of the input file
                for i, line in enumerate(file):
                    try:
                        # Get the age from the line
                        age = int(line)
                        # Write the name and age to the output file
                        out_file.write("Person {} - {}\n".format(chr(ord('A') + i), age))
                    except ValueError as err:
                        # Handle age errors
                        handle_age_error(err)
    except (FileExistsError, IsADirectoryError) as err:
        # Handle file errors
        handle_file_error(err)

# Example usage
process_ages("ages.txt", "result.txt")
