import os
from chunking import split_code_into_functions, apply_sliding_window_if_needed
from optimization import optimize_code_with_llm
from static_analysis import run_static_analysis
from utils import read_file, write_file, extract_globals, extract_all_code_blocks
from dotenv import load_dotenv
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
load_dotenv()

# Environment setup
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
os.environ["HF_TOKEN"] = os.getenv("HUGGING_FACE_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN")

INPUT_FILE = '../data/input_code.c'
OUTPUT_OPTIMIZED_CODE = '../data/optimized_code.c'
OUTPUT_EXPLANATIONS = '../data/explanations.txt'
# temp = '../data/temp.c'
CHUNK_SIZE = 8192  # Token limit for the LLM
OVERLAP_SIZE = 400  # Overlap for sliding window chunking

def main(INPUT_FILE):
    # Step 1: Read input C code
    code = read_file(INPUT_FILE)
    print(f"Input code read from {INPUT_FILE}")

    # Step 2: Extract global variables, macros, etc.
    global_context = extract_globals(code)
    print("Global context extracted successfully")
    # print(global_context)

    # Step 3: Run static analysis
    static_analysis_report = run_static_analysis(INPUT_FILE)
    print("Static analysis reported generated successfully")

    # Step 4: Chunk the code by functions
    functions = split_code_into_functions(code)
    print(f"Code split into {len(functions)} functions")

    # Step 5: Apply sliding window chunking only if needed
    chunks = apply_sliding_window_if_needed(functions, CHUNK_SIZE, OVERLAP_SIZE)
    print(f"Code split into {len(chunks)} chunks")

    # Step 6: Optimize code chunks and generate explanations using LLM
    optimized_chunks, explanations = optimize_code_with_llm(chunks, global_context, static_analysis_report)
    print("Code optimization completed successfully")
    # print(optimized_chunks)
    print("content type", type(optimized_chunks))
    # print("content type", type(explanations))

    # Step 7: Write the optimized code and explanations to output files
    # print(global_context)
    # write_file(OUTPUT_OPTIMIZED_CODE, global_context)
    # print(global_context)
    formatted_code_chunks = global_context + "\n\n" + extract_all_code_blocks(optimized_chunks)
    write_file(OUTPUT_OPTIMIZED_CODE, formatted_code_chunks)
    write_file(OUTPUT_EXPLANATIONS, explanations)
    return [formatted_code_chunks, explanations]
    
    print(f"Optimized code and explanations saved to {OUTPUT_OPTIMIZED_CODE} and {OUTPUT_EXPLANATIONS}")

if __name__ == "__main__":
    main(INPUT_FILE)
