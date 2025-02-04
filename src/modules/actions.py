import subprocess
from src.modules.utils import check_if_folder_exists


def clone_repo(url: str, destination: str) -> str:
    """
    Clone the repository from the given URL to the destination folder.
    Note that this function will create the destination folder if it does not exist.
    :param url: The URL of the repository to clone.
    :param destination: The destination folder to clone the repository to.
    :return: The CLI logs from the cloning process.
    :raises: Exception if the cloning fails.
    """
    # TODO: Implement this function
    pass


def checkout_ref(target_folder: str, ref: str) -> str:
    """
    Checkout the given commit SHA in the repository.
    :param target_folder: The folder of the repository.
    :param ref: The commit reference to checkout.
    :return: The CLI logs from the checkout process.
    :raises: Exception if the checkout fails.
    """
    # TODO: Implement this function
    pass


def setup_dependencies(target_folder: str) -> str:
    """
    Setup and install dependencies for the project.
    This function will invoke python3 to create a virtual environment,
    then install the dependencies listed in `requirements.txt`.
    :param destination: The root folder of the project.
    :return: The CLI logs from the setup process.
    :raises: Exception if the target folder does not exist or if the installation fails.
    """
    # TODO: Implement this function
    pass


def run_linter_check(target_folder: str) -> tuple[bool, str]:
    """
    Run the linter on the project.
    This function will invoke the linter tool to check for syntax errors.
    :param target_folder: The root folder of the project.
    :return: True if the linter passes, False if the linter fails. Also return the CLI logs from the linter process.
    :raises: Exception if the target folder does not exist.
    """

    if not check_if_folder_exists(target_folder):
        raise ValueError(f"The provided path {target_folder} is not a valid directory.")

    flake_command = "flake8 --select E999 ."
    result = subprocess.run(
        flake_command, capture_output=True, shell=True, cwd=target_folder
    )
    if result.stdout:
        logs = result.stdout.decode()
        success = False
    else:
        logs = "Linting Log: No syntax errors found."
        success = True

    return (success, logs)


def run_tests(target_folder: str) -> tuple[bool, str]:
    """
    Run the tests on the project.
    This function will invoke the test runner to execute the test suite.
    :param target_folder: The root folder of the project.
    :return: True if all the tests pass, False if some tests fail. Also return the CLI logs from the test process.
    :raises: Exception if the target folder does not exist.
    """
    # TODO: Implement this function and clean up mock return value.
    return (True, "Mock logs: All tests passed.")
