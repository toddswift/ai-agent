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
    if directory and not directory.startswith(working_directory):
        return {
            "error": f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        }
    
    #If the directory argument is not a directory, again, return an error string:
    if directory and not os.path.isdir(directory):
        return {
            "error": f'Error: "{directory}" is not a valid directory'
        }
    
    # We're returning strings here rather than raising errors because 
    # we want get_files_info to always return a string that the LLM can read. 
    # This way, when it encounters an error, it can try again with a different approach.


    #Build and return a string representing the contents of the directory. It should use this format:
    #- README.md: file_size=1032 bytes, is_dir=False
    #- src: file_size=128 bytes, is_dir=True
    #- package.json: file_size=1234 bytes, is_dir=False
    files_info = [] # List to hold file information strings

