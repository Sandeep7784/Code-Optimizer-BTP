from langchain_groq import ChatGroq
from langchain_core.output_parsers.string import StrOutputParser

# def create_optimization_prompt(code_chunk, global_context, static_analysis_report):
#     """Generate a prompt to send to the LLM with enhanced instructions for code optimization, incorporating static analysis insights."""

#     template = """
#     You are an expert C code optimization assistant. Your task is to optimize the provided C code **only as it is**, without introducing any additional elements or dependencies. The code chunk is part of a larger codebase, so focus solely on enhancing the performance and memory usage of the provided portion, while ensuring functionality remains intact. Below are context details and instructions for this task.

#     **Global Context**
#     - Variables, Macros, and Includes:
#       {global_context}

#     **Static Analysis Report**
#     The static analysis provides valuable insights into the code’s structure and identifies specific areas for optimization within this code chunk:
#     - **Cppcheck Report**: General findings on issues, potential errors, and inefficiencies in this code.
#     - **Functions List**: Lists the functions present in this code with their parameters and types, to help identify functions suitable for inlining or refactoring.
#     - **Dependencies**: Details interdependencies among functions, showing call relationships to help streamline calls or reduce redundancies if relevant.
#     - **Dependency Report**: Summarizes code flow within this chunk, offering insights into performance bottlenecks or high-frequency function use.

#     **Optimization Instructions**
#     Use the static analysis findings as a guide, and apply these optimizations only to the provided code chunk. Focus on both performance and readability:
#     1. **Code Refactoring**: Simplify redundant or overly complex code within the chunk.
#     2. **Function Inlining**: Inline any small or frequently called functions as appropriate to minimize call overhead.
#     3. **Variable Optimization**: Streamline variable declarations, types, and usage to improve memory and speed.
#     4. **Loop Optimization**: Optimize loops to minimize iterations and improve branching efficiency.
#     5. **Dependency Management**: Where dependencies allow, refine function calls or structure for better performance within the given chunk.
#     6. **Memory Management**: Minimize memory use by optimizing allocations, reducing redundancy, and freeing memory within this code.
#     7. **Constant Folding**: Simplify constant expressions based on the cppcheck report, especially in frequently accessed sections.
#     8. **Dead Code Elimination**: Remove any unused functions, variables, or blocks as identified by the cppcheck report.
#     9. **Loop Unrolling**: If loops are frequently executed and have a predictable number of iterations, consider unrolling.
#     10. **Strength Reduction**: Simplify arithmetic expressions for efficiency.
#     11. **Register Allocation**: Allocate frequently accessed variables to registers to reduce memory access overhead.

#     **Formatting Requirements**
#     - Ensure that the optimized code behaves identically to the original in terms of functionality.
#     - Retain all variable names and structures for easy readability.
#     - Avoid adding any elements unrelated to this code chunk or introducing additional complexity.

#     Here is the code to optimize:
#     ```c
#     {code_chunk}
#     ```
    
#     **Output Requirements**
#     Return the result in the following format to ensure each part is directed to its corresponding file:

#     Optimized Code:
#     ```c
#     [Your optimized code here]
#     ```

#     Results:
#     Provide explanations in the following format:
#       - Function Name: [Write the name of the function you optimized]
#       - Explanation: Explain each optimization made for this function, referencing the static analysis findings (e.g., from cppcheck report, functions list, or dependency report). Include the optimization technique, why it was used, and how it improves performance or memory usage.
#       - Note: If an optimization technique from the list was not applied, please omit it from the explanations.
#     """
    
#     return template.format(code_chunk=code_chunk, global_context=global_context, static_analysis_report=static_analysis_report)

# def create_optimization_prompt(code_chunk, global_context, static_analysis_report):
#     """Generate a prompt to send to the LLM with enhanced instructions for code optimization, incorporating static analysis insights."""

#     template = """
#     You are an expert embedded C code optimization specialist. Analyze and optimize the provided code chunk while maintaining its core functionality and embedded system constraints. Your optimization must consider the provided static analysis data and global context.

#     **Context and Analysis Data**
#     1. Global Context:
#     {global_context}

#     2. Static Analysis Information:
#     - Cppcheck Report: {cppcheck_report}
#     - Functions List: {functions_list}
#     - Function Dependencies: {dependencies}
#     - Code Flow Analysis: {flow_analysis}

#     **Optimization Focus Areas**
#     Apply these embedded-specific optimization techniques where applicable:

#     1. Memory Optimization:
#     - Minimize stack usage
#     - Optimize variable sizes and alignment
#     - Reduce dynamic memory operations
#     - Consider flash vs RAM tradeoffs

#     2. Performance Optimization:
#     - Optimize critical paths identified in the dependency report
#     - Improve instruction efficiency
#     - Minimize function call overhead
#     - Optimize loop structures
#     - Consider interrupt latency impacts

#     3. Code Size Optimization:
#     - Remove redundant operations
#     - Consolidate similar code paths
#     - Optimize binary footprint
#     - Consider ROM space constraints

#     4. Resource Usage:
#     - Optimize register allocation
#     - Minimize peripheral access overhead
#     - Consider hardware-specific optimizations
#     - Reduce interrupt disable time

#     **Embedded Constraints**
#     - Maintain deterministic behavior
#     - Respect real-time requirements
#     - Consider memory alignment requirements
#     - Maintain interrupt safety
#     - Preserve volatile access patterns
#     - Consider hardware-specific limitations

#     **Code To Optimize**

#     ```c
#     {code_chunk}
#     ```

#     **Implementation Guidelines**
#     1. Use static analysis findings to identify:
#     - High-frequency code paths
#     - Memory usage patterns
#     - Function call hierarchies
#     - Potential bottlenecks

#     2. Apply optimizations that:
#     - Maintain original functionality
#     - Respect embedded constraints
#     - Improve performance metrics
#     - Reduce resource usage

#     3. Consider tradeoffs between:
#     - Code size vs execution speed
#     - RAM usage vs processing time
#     - Flash wear vs performance
#     - Interrupt latency vs throughput

#     **Output Requirements**
#     Return the result in the following format to ensure each part is directed to its corresponding file:

#     Optimized Code:
#     - Do not include any global context details, such as headers, macros, or includes, in the optimized code section. Only include the optimized function code.

#     ```c
#     [Your optimized code here]
#     ```

#     Results:
#     Provide explanations in the following format:
#     - Function Name: [Write the name of the function you optimized]
#     - Explanation: Explain each optimization made for this function, referencing the static analysis findings (e.g., from cppcheck report, functions list, or dependency report). Include the optimization technique, why it was used, and how it improves performance or memory usage.

#     """    
    
#     cppcheck_report = static_analysis_report.get('cppcheck_report', 'No report available')
#     functions_list = static_analysis_report.get('functions', 'No list available')
#     dependencies = static_analysis_report.get('dependencies', 'No dependencies found')
#     flow_analysis = static_analysis_report.get('dependency_report', 'No flow analysis available')

#     formatted_template = template.format(
#         global_context=global_context,
#         cppcheck_report=cppcheck_report,
#         functions_list=functions_list,
#         dependencies=dependencies,
#         flow_analysis=flow_analysis,
#         code_chunk=code_chunk
#     )

#     return formatted_template

def create_optimization_prompt(code_chunk, global_context, static_analysis_report):
    """Generate a prompt to send to the LLM with enhanced instructions for code optimization, incorporating static analysis insights."""

    # Conditionally include the global context if it's non-empty
    global_context_section = f"1. Global Context:\n{global_context}" if global_context else ""

    template = f"""
    You are an expert embedded C code optimization specialist. Analyze and optimize the provided code chunk while maintaining its core functionality and embedded system constraints. Your optimization must consider the provided static analysis data and global context.

    **Context and Analysis Data**
    {global_context_section}

    2. Static Analysis Information:
    - Cppcheck Report: {{cppcheck_report}}
    - Functions List: {{functions_list}}
    - Function Dependencies: {{dependencies}}
    - Code Flow Analysis: {{flow_analysis}}

    **Optimization Focus Areas**
    Apply these embedded-specific optimization techniques where applicable:

    1. Memory Optimization:
    - Minimize stack usage
    - Optimize variable sizes and alignment
    - Reduce dynamic memory operations
    - Consider flash vs RAM tradeoffs

    2. Performance Optimization:
    - Optimize critical paths identified in the dependency report
    - Improve instruction efficiency
    - Minimize function call overhead
    - Optimize loop structures
    - Consider interrupt latency impacts

    3. Code Size Optimization:
    - Remove redundant operations
    - Consolidate similar code paths
    - Optimize binary footprint
    - Consider ROM space constraints

    4. Resource Usage:
    - Optimize register allocation
    - Minimize peripheral access overhead
    - Consider hardware-specific optimizations
    - Reduce interrupt disable time

    **Embedded Constraints**
    - Maintain deterministic behavior
    - Respect real-time requirements
    - Consider memory alignment requirements
    - Maintain interrupt safety
    - Preserve volatile access patterns
    - Consider hardware-specific limitations

    **Code To Optimize**

    ```c
    {{code_chunk}}
    ```

    **Implementation Guidelines**
    1. Use static analysis findings to identify:
    - High-frequency code paths
    - Memory usage patterns
    - Function call hierarchies
    - Potential bottlenecks

    2. Apply optimizations that:
    - Maintain original functionality
    - Respect embedded constraints
    - Improve performance metrics
    - Reduce resource usage

    3. Consider tradeoffs between:
    - Code size vs execution speed
    - RAM usage vs processing time
    - Flash wear vs performance
    - Interrupt latency vs throughput

    **Output Requirements**
    Return the result in the following format to ensure each part is directed to its corresponding file. It is crucial to adhere strictly to this format without any deviations:

    Optimized Code:
    - Do not include any global context details, such as headers, macros, or includes, in the optimized code section. Only include the optimized function code.

    ```c
    [Your optimized code here]
    ```

    Results:
    - Provide the following information in this specific format:
      - Function Name: [Write the name of the function you optimized]
      - Explanation: Explain each optimization made for this function, referencing the static analysis findings (e.g., from cppcheck report, functions list, or dependency report). Include the optimization technique, why it was used, and how it improves performance or memory usage.
      
    **Example of Expected Output:**
    ```
    Optimized Code:
    ```c
    void optimized_function() {
        "// optimized code here"
    }
    ```

    Results:
    - Function Name: optimized_function
    - Explanation: The optimization reduced memory usage by eliminating redundant variables and improved execution speed by inlining critical function calls.

    """    

    cppcheck_report = static_analysis_report.get('cppcheck_report', 'No report available')
    functions_list = static_analysis_report.get('functions', 'No list available')
    dependencies = static_analysis_report.get('dependencies', 'No dependencies found')
    flow_analysis = static_analysis_report.get('dependency_report', 'No flow analysis available')

    formatted_template = template.format(
        cppcheck_report=cppcheck_report,
        functions_list=functions_list,
        dependencies=dependencies,
        flow_analysis=flow_analysis,
        code_chunk=code_chunk
    )

    return formatted_template


def optimize_code_with_llm(chunks, global_context, static_analysis_report):
    """Optimize each chunk of code using the LLM, store optimized code and explanations effectively."""
    
    # Initialize LLM model
    llm = ChatGroq(model="llama3-8b-8192")
    optimized_code = []
    explanations = []
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        
        # Create optimization prompt with global context and static analysis report
        prompt = create_optimization_prompt(chunk, global_context, static_analysis_report)
        print(f"Created optimization prompt for chunk {i+1}")

        # Define the message format for the LLM
        messages = [
            {"role": "system", "content": "Optimize the C code"}, 
            {"role": "user", "content": prompt}
        ]
        
        # Invoke the LLM with the prompt
        print(f"Invoking LLM for chunk {i+1}")
        try:
            result = llm.invoke(messages, timeout=3)  # Set a timeout of 3 seconds
            print(f"LLM invocation successful for chunk {i+1}")
        except Exception as e:
            print(f"Error invoking LLM for chunk {i+1}: {e}")
            result = None

        if result is None:
            print(f"No result for chunk {i+1}, skipping to next chunk")
            continue
        print(f"Received result from LLM for chunk {i+1}")

        # Parse the output content
        parser = StrOutputParser()
        output = parser.parse(result)
        content = output.content

        # print(content)
        # Split the output to separate optimized code and explanations
        split_output = content.split("Results:")
        optimized_code_chunk = split_output[0].strip()
        explanation_chunk = split_output[1].strip() if len(split_output) > 1 else "No explanation provided."

        # Add the optimized code to the list
        optimized_code.append(f"{optimized_code_chunk}")

        # print(explanation_chunk)
        # Structure the explanation with the chunk and function name
        if "Function Name:" in explanation_chunk:
            explanation_sections = explanation_chunk.split("Function Name:")
            for section in explanation_sections[1:]:
                function_name, function_explanation = section.strip().split("\n", 1)
                explanations.append(
                    f"Function: {function_name.strip()}\n {function_explanation.strip()}\n"
                )
        else:
            explanations.append(f"Chunk {i+1} Explanation:\n{explanation_chunk}")

        print(f"Processed chunk {i+1} complete")

    print("All chunks processed")
    return "\n\n".join(optimized_code), "\n\n".join(explanations)

