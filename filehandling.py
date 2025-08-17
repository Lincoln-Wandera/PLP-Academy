# Open file for reading
with open("input.txt", "r") as infile:
    content = infile.read()

# Make content uppercase
modified_content = content.upper()

# Write modified content to new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read, modified, and written to output.txt ")

#error handling

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile Content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
