import os
import curses

def list_files(directory):
    """Lists files in a given directory."""
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return []

def reformat_file(input_path, output_path, num_elements):
    """Reformats the content of the file."""
    try:
        with open(input_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {input_path}")
        return
    
    elements = [line.strip() for line in lines if line.strip()]  # Filter out empty lines
    
    if not elements:
        print(f"No elements found in the file.")
        return
    
    formatted_content = format_elements(elements, num_elements)
    
    try:
        with open(output_path, 'w') as file:
            file.write(formatted_content)
    except IOError:
        print(f"Error writing to file: {output_path}")

def format_elements(elements, num_elements):
    """Formats elements into the desired structure."""
    formatted_content = ""
    chunk_size = num_elements + 1  # Including the heading
    for i in range(0, len(elements), chunk_size):
        chunk = elements[i:i + chunk_size]
        if len(chunk) > 0:
            formatted_content += f"## {chunk[0]}\n\n"
            formatted_content += "\n".join(chunk[1:])
            formatted_content += "\n\n"
    return formatted_content

def get_positive_integer(stdscr, prompt):
    """Gets a positive integer from user input using curses."""
    curses.echo()
    stdscr.addstr(prompt)
    stdscr.refresh()
    while True:
        try:
            value = int(stdscr.getstr().decode('utf-8'))
            if value > 0:
                curses.noecho()
                return value
            else:
                stdscr.addstr("Please enter a positive integer: ")
                stdscr.refresh()
        except ValueError:
            stdscr.addstr("Invalid input. Please enter a positive integer: ")
            stdscr.refresh()

def file_selector(stdscr, files):
    """Allows the user to select a file using arrow keys."""
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Files available for reformatting:")
        for idx, file in enumerate(files):
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(idx + 1, 0, file)
            if idx == current_row:
                stdscr.attroff(curses.A_REVERSE)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return files[current_row]

def main(stdscr):
    base_dir = os.getcwd()
    input_dir = os.path.join(base_dir, 'to_reformat')
    output_dir = os.path.join(base_dir, 'reformatted_files')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    files = list_files(input_dir)
    if not files:
        print("No files found in the 'to_reformat' directory.")
        return
    
    chosen_file = file_selector(stdscr, files)
    
    stdscr.clear()
    num_elements = get_positive_integer(stdscr, "Enter the number of elements to reformat: ")
    
    input_path = os.path.join(input_dir, chosen_file)
    output_path = os.path.join(output_dir, f"{os.path.splitext(chosen_file)[0]}_reformatted.md")
    
    reformat_file(input_path, output_path, num_elements)
    
    stdscr.addstr(f"\nFile reformatted and saved to: {output_path}\n")
    stdscr.addstr("Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
