import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

try:
    # Check if content is provided via command line
    if len(sys.argv) < 2: # ensure at least one argument is provided
        print("Error: Please provide content as a command-line argument.")
        sys.exit(1)

    # Get content from command line argument
    content = sys.argv[1]

    # Check for --verbose flag
    verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"
    
    user_prompt = f"Generate a summary for the following content: {content}"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if verbose:
        print(f"User prompt: {user_prompt}")

    
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )

    print(response.text)

    if verbose and hasattr(response, 'usage_metadata') and response.usage_metadata:
        # Print the usage metadata if available
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    elif verbose:
        print("No usage metadata available.")
except Exception as e:
    print(f"Error occured: {str(e)}")
    
