import re

# Function to read a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

import os

# Function to write a file
def write_file(file_path, content):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(content))
        
        print(f"Successfully wrote content to {file_path}")
        return True
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return False

def extract_all_code_blocks(content):
    # Find all matches for code blocks within ```c and ```
    code_blocks = re.findall(r"```c\n(.*?)\n```", content, re.DOTALL)
    # Join all code blocks together, separating them with newlines
    return "\n\n".join(code_blocks).strip()

# Function to extract global variables, macros, etc. from code
def extract_globals(code):
    global_vars = []
    lines = code.splitlines()

    for line in lines:
        if re.match(r'^\s*(#define|extern|const)', line):
            global_vars.append(line)

    print(f"Extracted global variables, macros, etc")
    return "\n".join(global_vars)
