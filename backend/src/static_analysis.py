import re
import subprocess
from collections import defaultdict

# Function to run Cppcheck static analysis
def run_cppcheck(code_file):
    cmd = ["cppcheck", "--enable=all", code_file]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("cppcheck run success!")
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def extract_functions_and_calls(code_file):
    """Extract function definitions and calls to build a dependency report."""
    function_pattern = r'\b(?:void|int|char|float|double|static)\s+(\w+)\s*\(.*?\)\s*\{'
    call_pattern = r'\b(\w+)\s*\('
    
    functions = {}
    dependencies = defaultdict(set)

    with open(code_file, 'r') as f:
        code_lines = f.readlines()
        
        # Extract function names and their definitions
        for i, line in enumerate(code_lines):
            function_match = re.search(function_pattern, line)
            if function_match:
                func_name = function_match.group(1)
                functions[func_name] = {'line': i, 'calls': []}
        
        # Extract function calls within the code
        for i, line in enumerate(code_lines):
            for func_name in functions.keys():
                if func_name in line:
                    # Check if it's a function call (not a definition)
                    if re.search(call_pattern, line):
                        for called_func in functions.keys():
                            if called_func in line and called_func != func_name:
                                dependencies[func_name].add(called_func)

    return functions, dependencies

def format_dependency_report(dependencies):
    """Format the dependency report as a string."""
    report_lines = ["Function Call Dependency Report:"]
    for func, calls in dependencies.items():
        if calls:
            report_lines.append(f"{func} calls: {', '.join(calls)}")
        else:
            report_lines.append(f"{func} has no calls")
    return "\n".join(report_lines)

def run_static_analysis(code_file):
    cppcheck_report = run_cppcheck(code_file)
    print("Static analysis completed successfully")

    # Extract functions and their calls for deeper analysis
    functions, dependencies = extract_functions_and_calls(code_file)

    # Format the dependency report
    dependency_report = format_dependency_report(dependencies)

    # Combine the analysis outputs
    analysis_output = {
        "cppcheck_report": cppcheck_report,
        "functions": functions,
        "dependencies": dependencies,
        "dependency_report": dependency_report,
    }

    return analysis_output

