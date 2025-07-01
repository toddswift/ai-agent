import os

def get_file_content(working_directory, file_path): 
    
    """
    Retrieves the content of a file located within the specified working directory.
    
    :param working_directory: The base directory where the file is located.
    :param file_path: The relative path to the file from the working directory.
    :return: The content of the file as a string, or an error message if the file cannot be accessed.
    """
    # check if the file_path is within the working directory
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Check if the target file is within the working directory
    if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check if the target file exists and is a file
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # Attempt to read the file content    
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

            # If the file contains more than 10000 characters, truncate it to the first 10000 characters
            if len(content) > 10000:
                content = content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'
                
        return content
    except Exception as e:
        return f"Error: {e}"
