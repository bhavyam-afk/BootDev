import os 
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_directory = os.path.abspath(working_directory)
    final_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security: prevent directory traversal
    if os.path.commonpath([working_directory, final_path]) != working_directory:
        print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        return
    
    if os.path.isfile(final_path) == False:
        print(f'Error: "{file_path}" does not exist or is not a regular file')
        return
    
    if final_path.endswith(".py") == False:
        print(f'Error: "{file_path}" is not a Python file')
        return
    
    command = ["python", final_path]
    if args:
        command.extend(args)
    
    completed_process = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
    if completed_process.returncode != 0:
        print(f"Process exited with code {completed_process.returncode}")
    
    if (not completed_process.stdout) and (not completed_process.stderr):
        print("No output produced")
        return

    if completed_process.stdout:
        print(f"STDOUT: {completed_process.stdout}")
        return

    if completed_process.stderr:
        print(f"STDERR: {completed_process.stderr}")
        return
