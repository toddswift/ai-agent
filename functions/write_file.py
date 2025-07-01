import os
from os.path import exists

def write_file(working_directory, file_path, content):

    # determine the absolute path of the working directory and the target file
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Check if the target file is within the working directory
    if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:  
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not exists(target_file):
        # create the file_path if it does not exist
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
        except Exception as e:
            return f"Error: {e}"
    
    # Overwrite the contents of the file with the content argument
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
        