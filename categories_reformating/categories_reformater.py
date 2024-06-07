import os

def list_files(directory):
    """Lists files in a given directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_user_input(prompt, valid_options=None):
    """Gets validated user input."""
    while True:
        choice = input(prompt)
        if valid_options:
            if choice in valid_options:
                return choice
            else:
                print("Invalid choice. Please try again.")
        else:
            return choice

def reformat_file(input_path, output_path, num_elements):
    """Reformats the content of the file."""
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    # Separate the elements
    elements = [line.strip() for line in lines if line.strip()]
    
    # Ensure we have enough elements
    if len(elements) < num_elements:
        print(f"Not enough elements in the file. Found {len(elements)}, but {num_elements} were required.")
        return
    
    # Format the output
    formatted_content = ""
    chunk_size = num_elements + 1  # Including the heading
    for i in range(0, len(elements), chunk_size):
        chunk = elements[i:i + chunk_size]
        if len(chunk) > 0:
            formatted_content += f"## {chunk[0]}\n\n"
            formatted_content += "\n".join(chunk[1:chunk_size])
            formatted_content += "\n\n"
    
    # Write to the output file
    with open(output_path, 'w') as file:
        file.write(formatted_content)

def main():
    # Define directories
    base_dir = os.getcwd()
    input_dir = os.path.join(base_dir, 'to_reformat')
    output_dir = os.path.join(base_dir, 'reformatted_files')
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List files and get user choice
    files = list_files(input_dir)
    if not files:
        print("No files found in the 'to_reformat' directory.")
        return
    
    print("Files available for reformatting:")
    for idx, file in enumerate(files):
        print(f"{idx}: {file}")
    
    file_choice = get_user_input("Enter the number of the file you want to reformat: ", [str(i) for i in range(len(files))])
    chosen_file = files[int(file_choice)]
    
    # Get number of elements to reformat
    while True:
        try:
            num_elements = int(input("Enter the number of elements to reformat: "))
            if num_elements > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Define input and output paths
    input_path = os.path.join(input_dir, chosen_file)
    output_path = os.path.join(output_dir, f"{os.path.splitext(chosen_file)[0]}_reformatted.md")
    
    # Reformat the file
    reformat_file(input_path, output_path, num_elements)
    print(f"File reformatted and saved to: {output_path}")

if __name__ == "__main__":
    main()
