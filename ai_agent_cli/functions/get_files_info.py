import os
import types

def get_files_info(working_directory, directory=""):

    working_directory = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    # Security: prevent escaping working directory
    if os.path.commonpath([working_directory, target_dir]) != working_directory:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return

    # Check directory validity
    if not os.path.isdir(target_dir):
        print(f'Error: "{directory}" is not a directory')
        return

    for name in os.listdir(target_dir):
        full_path = os.path.join(target_dir, name)
        is_dir = os.path.isdir(full_path)
        size = os.path.getsize(full_path)
        print(f"- {name}: file_size={size}, is_dir={is_dir}")
