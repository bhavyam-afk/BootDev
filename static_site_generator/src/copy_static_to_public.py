import os
import shutil

def copy_recursive(src, dest):
    # If destination exists, delete it first
    if os.path.exists(dest):
        print(f"Deleting existing directory: {dest}")
        shutil.rmtree(dest)

    # Create destination directory
    os.mkdir(dest)

    # Walk through source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} → {dest_path}")
            shutil.copy(src_path, dest_path)

        else:
            # Directory → recurse
            print(f"Entering directory: {src_path}")
            copy_recursive(src_path, dest_path)
