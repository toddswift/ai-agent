import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file

def main():

    # Import and load environment variables from a .env file into the application's environment
    load_dotenv()

    # Retrieve the Gemini API key from environment variables
    # os.environ.get() safely accesses the variable; returns None if the key doesn't exist
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize a client for the Gemini API, passing the API key for authentication
    # The client object will be used to interact with Gemini's AI services
    client = genai.Client(api_key=api_key)

    try:
        # Check if content is provided via command line
        if len(sys.argv) < 2: # ensure at least one argument is provided
            print("Error: Please provide content as a command-line argument.")
            sys.exit(1) # graciously exit if no content is provided

        # Get content from command line argument
        content = sys.argv[1] # the first argument after the script name

        # Check for --verbose flag
        verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"
        
        user_prompt = content # Use the provided content as the user prompt

        # Prepare the message to send to the Gemini API
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        # If verbose mode is enabled, print the user prompt
        if verbose:
            print(f"User prompt: {user_prompt}")

        available_functions = types.Tool(
            function_declarations=[
                schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
            ]      
        )          
              
            
        # Calls a function based on the function call part provided by the Gemini API.
        # If verbose mode is enabled, it prints the function name and arguments.
        def call_function(function_call_part, verbose=False):
            if verbose:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            else:
                print(f" - Calling function: {function_call_part.name}")

            # Get the arguments and add working_directory
            args = dict(function_call_part.args)  # Make a copy of the args
            args["working_directory"] = "./calculator"  # Add the working directory

            
            # Call the function with the provided arguments and return types.Content objects

            if function_call_part.name == "get_files_info":
                # return types.Content objects
                content_results = get_files_info(**args)
                # Convert the content results to types.Content objects
                return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_call_part.name,  # This should be the function name
                        response={"result": content_results},  # Result wrapped in a dict
                        )     
                    ],
                )
            elif function_call_part.name == "get_file_content":
                content_results = get_file_content(**args)
                return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_call_part.name,  # This should be the function name
                            response={"result": content_results},  # Result wrapped in a dict
                        )
                    ],
                )
            elif function_call_part.name == "run_python_file":
                content_results = run_python_file(**args)
                return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_call_part.name,  # This should be the function name  
                            response={"result": content_results},  # Result wrapped in a dict          
                        )   
                    ],
                )
            elif function_call_part.name == "write_file":
                content_results = write_file(**args)
                return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_call_part.name,  # This should be the function name
                            response={"result": content_results},  # Result wrapped in a dict
                        )
                    ],
                )   
            else:
                # raise an error
                return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                        )
                    ],
                )
                        
        # Generate content using the Gemini API with the provided user prompt    
        response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config = types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt), # system_prompt is stored in prompts.py
        )

        # If the LLM called a function, print the function name and arguments
        if response.function_calls:
            function_call_part = response.function_calls
            
            for function_call_part in response.function_calls:
                #print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                function_call_result = call_function(function_call_part, verbose)
                # Check if the result has the expected structure
                if not hasattr(function_call_result.parts[0], 'function_response') or not function_call_result.parts[0].function_response.response:
                    raise Exception("Function call result missing expected structure")

                if function_call_result:
                    # If the function call result is not None, print the result
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                
        else:
            # Print the response from the Gemini API
            print(response.text)

        # If verbose mode is enabled, print the usage metadata if available
        if verbose and hasattr(response, 'usage_metadata') and response.usage_metadata:
            # Print the usage metadata if available
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        # If verbose mode is enabled but no usage metadata is available, print a message
        elif verbose:
            print("No usage metadata available.")
    except Exception as e:
        print(f"Error occured: {str(e)}")
    
# This is the main entry point of the script
# It checks if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()