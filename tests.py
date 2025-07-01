# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():

    result = run_python_file("calculator", "main.py")
    print("Result for running 'main.py' file:")
    print(result)
    print("")
    
    result = run_python_file("calculator", "tests.py")
    print("Result for running 'tests.py' file:")
    print(result)
    print("")
    
    result = run_python_file("calculator", "../main.py") # (this should return an error)
    print("Result for running '../main.py' file:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py") # (this should return an error)
    print("Result for running 'nonexistent.py' file:")
    print(result)
    print("")

 
if __name__ == "__main__":
    test()