import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function


def main():
    # Load environment variables 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

    # CLI argument parsing
    parser = argparse.ArgumentParser(description="AI Agent CLI")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI model")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output (prompt, tokens, metadata)")
    args = parser.parse_args()

    prompt = args.user_prompt
    verbose = args.verbose

    # Gemini client
    client = genai.Client(api_key=api_key)
    # Initial message history
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    MAX_ITERATIONS = 20

    for iteration in range(MAX_ITERATIONS):
        response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=messages,
                        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0),
                   )

    # -------------------------------------------------
    # STEP 2.1 + 2.2: Add ALL candidates to history
    # -------------------------------------------------
        if not response.candidates:
            raise RuntimeError("Model returned no candidates")

        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    # -------------------------------------------------
    # STEP 4: Final answer (no function calls)
    # -------------------------------------------------
        if not response.function_calls:
            if response.text:
                if verbose:
                    print("--- VERBOSE MODE ENABLED ---")
                    print("Model: gemini-2.5-flash")
                    print("User prompt:")
                    print(prompt)

                    if response.usage_metadata:
                        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                        print("Response tokens:", response.usage_metadata.candidates_token_count)

                print("Response:")
                print(response.text)
                break

            raise RuntimeError("Model returned no function calls and no text")

    # -------------------------------------------------
    # STEP 3: Execute function calls
    # -------------------------------------------------
        function_responses = []

        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=verbose)

            if not function_call_result.parts:
                raise RuntimeError("Function call returned no parts")

            part = function_call_result.parts[0]

            if part.function_response is None:
                raise RuntimeError("Missing function_response")

            if part.function_response.response is None:
                raise RuntimeError("Function response payload is None")

            function_responses.append(part)

            if verbose:
                print(f"-> {part.function_response.response}")

    # -------------------------------------------------
    # STEP 3 (continued): Feed tool results back
    # -------------------------------------------------
        messages.append(
            types.Content(
                role="user",
                parts=function_responses,
            )   
        )

    else:
    # -------------------------------------------------
    # STEP 5: Max iterations reached
    # -------------------------------------------------
        print("Error: Agent exceeded maximum iterations without producing a final response.")
        exit(1)




if __name__ == "__main__":
    main()
