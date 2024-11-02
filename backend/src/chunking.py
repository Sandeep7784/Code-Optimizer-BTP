import re

# Function to split code into individual functions
def split_code_into_functions(code):
    functions = []
    current_function = []
    inside_function = False

    for line in code.splitlines():
        if "{" in line and not inside_function:
            inside_function = True
            current_function.append(line)
        elif "}" in line and inside_function:
            current_function.append(line)
            functions.append("\n".join(current_function))
            current_function = []
            inside_function = False
        elif inside_function:
            current_function.append(line)
    
    return functions

# Apply sliding window only if function size exceeds token limit
def apply_sliding_window_if_needed(functions, max_chunk_size, overlap_size):
    chunks = []
    
    for function in functions:
        if len(function) > max_chunk_size:
            # Apply sliding window chunking if the function is too large
            chunks.extend(sliding_window_chunking(function, max_chunk_size, overlap_size))
        else:
            # Otherwise, keep the function intact as one chunk
            chunks.append(function)
    
    return chunks

# Sliding window chunking with overlap for large functions
def sliding_window_chunking(function, max_chunk_size, overlap_size):
    lines = function.splitlines()
    chunks = []
    
    for i in range(0, len(lines), max_chunk_size - overlap_size):
        chunk = "\n".join(lines[i:i + max_chunk_size])
        chunks.append(chunk)
    
    return chunks
