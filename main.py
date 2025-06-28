import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


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

    # Generate content using the Gemini API with the provided user prompt    
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )

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
    
