import os
import sys
# Function to check if a file is a text file
def is_text_file(file_path, blocksize=512):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(blocksize)
            if b'\0' in chunk:  # Contains null byte, likely binary
                return False
            # Check if most characters are printable ASCII or UTF-8 compatible
            text_chars = bytes(range(32, 127)) + b'\n\r\t\f\b'
            return all(byte in text_chars for byte in chunk)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return False

# Function to save the folder structure into the output file
def save_folder_structure(folder_path, output_file, indent_level=0):
    total_size = 0
    indent = " " * (indent_level * 4)  # Indentation for nested folders
    
    # Print the name of the current folder
    folder_name = os.path.basename(folder_path)
    output_file.write(f"{indent}- {folder_name}/\n")
    
    for entry in os.scandir(folder_path):
        if entry.is_file():
            # Only process text files
            if is_text_file(entry.path):
                # Write file name and size
                file_size = os.path.getsize(entry.path)
                total_size += file_size
                output_file.write(f"{indent}    - {entry.name} ({file_size} bytes)\n")
        
        elif entry.is_dir():
            # Recursive call to print the contents of the subfolder
            subfolder_size = save_folder_structure(entry.path, output_file, indent_level + 1)
            total_size += subfolder_size
    
    return total_size

# Function to save all content from text files
def save_folder_contents(folder_path, output_file):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if is_text_file(file_path) and file_path != output_file.name:
                # Write the file name as a title
                output_file.write(f"\n--- {file_name} ---\n")
                output_file.write("=" * 50 + "\n")
                
                # Read and write the content of the file
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                        output_file.write(file_content + "\n")
                        output_file.write("=" * 50 + "\n")
                except Exception as e:
                    output_file.write(f"Error reading file: {e}\n")

# Main function to handle the workflow
def main():
    if len(sys.argv) < 2:
        print("Please provide the folder path as a command-line argument.")
        sys.exit(1)

    folder_path = sys.argv[1].strip()
    # folder_path = input("Please enter the folder path to work with: ").strip()
    
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("The specified folder path does not exist.")
        return
    
    # Create the output text file and calculate its size

    output_file = f"{folder_path}\\{folder_path.split("\\")[-1]}-collected-data.txt"
    total_size = 0
    # Calculate the size of the output file with folder structure
    with open(output_file, 'w') as out_file:
        out_file.write("Folder Structure:\n")
        out_file.write("-" * 50 + "\n")
        total_size = save_folder_structure(folder_path, out_file)
        out_file.write("-" * 50 + "\n")
        out_file.write(f"Total Size: {total_size} bytes\n")
    
    # Calculate the output file size
    output_size = os.path.getsize(output_file)
    print(f"Output text file size ~= {total_size/1024} KB")
    
    # Ask the user if they want to continue
    continue_choice = input("Do you want to continue and save the file contents? (yes/no): ").strip().lower()
    
    if continue_choice == "yes" or "y":
        with open(output_file, 'a') as out_file:
            out_file.write("\n" + "=" * 50 + "\n")
            out_file.write("File Contents:\n")
            out_file.write("-" * 50 + "\n")
            save_folder_contents(folder_path, out_file)
        
        # Recalculate the output file size
        output_size = os.path.getsize(output_file)
        print(f"Final output text file size: {output_size/1024} KB")
        print(f"Cheak the collected data text file : {output_file}")
    else:
        print("Operation canceled. No content was added.")

# Run the main function
if __name__ == "__main__":
    main()
