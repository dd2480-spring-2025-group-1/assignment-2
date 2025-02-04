import os
import shutil


def check_if_folder_exists(folder_path: str) -> bool:
    """
    Check if the folder exists at the given path.
    """
    return os.path.exists(folder_path) and os.path.isdir(folder_path)


def check_if_file_exists(file_path: str) -> bool:
    """
    Check if the file exists at the given path.
    """
    return os.path.exists(file_path) and os.path.isfile(file_path)


def create_folder(folder_path: str) -> None:
    """
    Create a folder at the given path.

    This function will also create all necessary parent folders if they do not exist.
    """
    os.makedirs(folder_path, exist_ok=True)


def write_to_file(file_path: str, content: str) -> None:
    """
    Write the content to the file at the given path.

    Note that this function will overwrite the file if it already exists.

    If the path does not exist, a new file along the path will be created.
    """
    if not check_if_folder_exists(os.path.dirname(file_path)):
        create_folder(os.path.dirname(file_path))
    with open(file_path, "w") as file:
        file.write(content)


def remove_folder(folder_path: str) -> None:
    """
    Remove the folder (and its content) at the given path.

    If the folder does not exist, this function will do nothing.
    """
    if check_if_folder_exists(folder_path):
        shutil.rmtree(folder_path)


def remove_file(file_path: str) -> None:
    """
    Remove the file at the given path.

    If the file does not exist, or if it is a folder, this function will do nothing.
    """
    if check_if_file_exists(file_path):
        os.remove(file_path)
