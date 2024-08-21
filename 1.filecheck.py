# Write a python program to open a file and check what are the access permissions acquired by that file using os module  31/07/24


import os


def check_file_permissions(file_path):
    """
    Check the file permissions for the given file path.

    Args:
        file_path (str): The path of the file to check.

    Returns:
        None
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    try:
        # Get the file mode
        mode = os.stat(file_path).st_mode

        # Get the permissions as a dictionary
        permissions = {
            'read': bool(mode & 0o400), # for read permission set 0o400, bool is used to convert integer to boolean as normal output is 0 or 1
            'write': bool(mode & 0o200), # for write permission set 0o200, bool is used to convert integer to boolean as normal output is 0 or 1
            'execute': bool(mode & 0o100) # for execute permission set 0o100, bool is used to convert integer to boolean as normal output is 0 or 1
        }

        # Print the permissions
        print(f"File permissions for '{file_path}':")
        print(f"Read: {permissions['read']}")
        print(f"Write: {permissions['write']}")
        print(f"Execute: {permissions['execute']}")

    except OSError as e:
        # Print the error message
        print(f"Error: {e}")


if __name__ == "__main__": # It checks if the file is being run directly or imported

    # Get the file path from the user
    file_path = input("Enter the file path: ")
    # Check the file permissions
    check_file_permissions(file_path)

