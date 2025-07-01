import os  # Import the 'os' module to interact with the operating system, e.g., for file path operations
import subprocess  # Import the subprocess module to run external commands

def run_python_file(working_directory, file_path):
    # Define a function that takes two parameters:
    # - working_directory: the base directory where the file should be located
    # - file_path: the relative or absolute path to the Python file to be run

    # Convert the working directory to an absolute path to ensure a full, unambiguous path
    abs_working_dir = os.path.abspath(working_directory)
    
    # Create the absolute path of the target file by joining the working directory with the file path
    # os.path.join ensures proper path construction (e.g., handling different OS separators like '/' or '\')
    # os.path.abspath ensures the resulting path is absolute
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Print the absolute working directory for debugging or informational purposes
    print("Absolute working directory:", abs_working_dir)
    
    # Check if the target file is within the working directory to prevent unauthorized access
    # os.path.commonpath finds the common prefix of the two paths
    # If the common path is not exactly the absolute working directory, the file is outside the permitted directory
    if os.path.commonpath([abs_working_dir, target_file_path]) != abs_working_dir:
        # Return an error message if the file is outside the working directory
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # If the file_path doesn't exist, return an error string:
    if not os.path.isfile(target_file_path):
        # Return an error message indicating the file was not found
        return f'Error: File "{file_path}" not found.'
    
    # If the file_path is not a Python file, return an error string:
    if not file_path.endswith('.py'):
        # Return an error message indicating the file is not a Python file
        return f'Error: "{file_path}" is not a Python file.'
    
    
    # Use subprocess.run function to execute the Python file.
    import subprocess  # Import the subprocess module to run external commands
    result = subprocess.run(
        ['python3', target_file_path],  # Command to run the Python file using Python
        capture_output=True,  # Capture both stdout and stderr
        text=True,  # Return output as text (string) instead of bytes
        timeout=30,  # Set a timeout of 30 seconds to prevent infinite execution
        cwd=abs_working_dir  # Set the working directory to the absolute working directory
    )

    #Format the output to include:
    #The stdout (prefixed with "STDOUT:")
    #The stderr (prefixed with "STDERR:")
    #If the process exits with a non-zero code, include "Process exited with code X"
    #If no output is produced, return "No output produced."
    #If any exceptions occur during execution, catch them and return an error string:
    try:
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
       
        # If the process exited with a non-zero code, append that information to the output        
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."       
    
    except Exception as e:
        # If an exception occurs, return an error message with the exception details
        return f"Error: executing Python file: {e}"