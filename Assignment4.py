def modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"Content has been successfully modified and written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the file.")
    
# Example usage
input_file = "example.txt"
output_file = "modified_example.txt"
modify_file(input_file, output_file)
def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")

    try:
        # Attempt to open the file
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file {filename}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
read_file_with_error_handling()
