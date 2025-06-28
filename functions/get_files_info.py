import os

def get_files_info(working_directory, directory=None):
    # if the directory is outside the working directory, raise an error
    '''
    WARNING: This code is designed to run in a restricted environment.
    It is restricted to only access files within a specific working directory.
    # This is to ensure that the LLM can only interact with files
    # within a designated area of the filesystem, preventing it from accessing
    # sensitive files or directories outside of this area.
    # The working directory is set to the current directory of the script.

    # Without this restriction
    # the LLM might go running amok anywhere on the machine
    # reading sensitive files or overwriting important data. 
    # This is a very important step that we'll 
    # bake into every function the LLM can call
    :WARNING
    '''
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    # We're returning strings here rather than raising errors because 
    # we want get_files_info to always return a string that the LLM can read. 
    # This way, when it encounters an error, it can try again with a different approach.

    #Build and return a string representing the contents of the directory. It should use this format:
    #- README.md: file_size=1032 bytes, is_dir=False
    #- src: file_size=128 bytes, is_dir=True
    #- package.json: file_size=1234 bytes, is_dir=False
    try:
        files_info = [] # List to hold file information strings
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
