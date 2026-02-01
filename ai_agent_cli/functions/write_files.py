import os

def write_files(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    final_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([working_directory, final_path]) != working_directory:
        print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        return

    if os.path.isdir(final_path):
        print(f'Error: Cannot write to "{file_path}" as it is a directory')
        return

    parent_dir = os.path.dirname(final_path)
    os.makedirs(parent_dir, exist_ok=True)

    with open(final_path, "w", encoding="utf-8") as f:
        f.write(content)
        print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
        return
