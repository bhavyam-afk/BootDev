import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    final_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security: prevent directory traversal
    if os.path.commonpath([working_directory, final_path]) != working_directory:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return

    # Validate file
    if not os.path.isfile(final_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return

    # Read file safely
    with open(final_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read(MAX_CHARS)

        # Check if truncated
        if f.read(1):
            content += f'\n\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    print(content)
