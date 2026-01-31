import os
from dotenv import load_dotenv
from google import genai
import argparse

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Ai Agent CLI")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI model")
    args = parser.parse_args()
    prompt = args.user_prompt
    
    generate_content = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    response = generate_content.text

    if generate_content.usage_metadata == None:
        raise RuntimeError("Usage metadata is missing in the response.")
    
    print("User prompt: ", prompt)
    print("Prompt tokens: ", generate_content.usage_metadata.prompt_token_count)
    print("Response tokens: ", generate_content.usage_metadata.candidates_token_count)

    print("Response:")
    print(response)


if __name__ == "__main__":
    main()
