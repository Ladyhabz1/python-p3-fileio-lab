def write_file(file_name, file_content):
    """Creates a .txt file and writes content to it."""
    with open(str(file_name) + ".txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends content to an existing .txt file."""
    with open(str(file_name) + ".txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """Reads and returns the content of a .txt file."""
    with open(str(file_name) + ".txt", "r") as file:
        return file.read()
