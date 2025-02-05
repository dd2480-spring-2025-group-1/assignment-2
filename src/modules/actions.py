import subprocess
from src.modules.utils import check_if_folder_exists, create_folder


def clone_repo(url: str, destination: str) -> str:
    """
    Clone the repository from the given URL to the destination folder.
    Note that this function will create the destination folder if it does not exist.
    :param url: The URL of the repository to clone.
    :param destination: The destination folder to clone the repository to.
    :return: The CLI logs from the cloning process.
    :raises: Exception if the cloning fails.
    """
    if not check_if_folder_exists(destination):
        create_folder(destination)

    command = f"git clone {url}"
    ret = subprocess.run(command, capture_output=True, shell=True, cwd=destination)

    if ret.returncode != 0:
        raise Exception(f"Failed cloning into repository {url}.")

    return ret.stdout.decode()


def checkout_ref(target_folder: str, ref: str) -> str:
    """
    Checkout the given commit SHA in the repository.
    :param target_folder: The folder of the repository.
    :param ref: The commit reference to checkout.
    :return: The CLI logs from the checkout process.
    :raises: Exception if the checkout fails, e.g., the commit SHA or the repo folder does not exist.
    """
    if not check_if_folder_exists(target_folder):
        raise Exception(f"The target folder ${target_folder} does not exist.")

    command = f"git checkout {ref}"
    ret = subprocess.run(command, capture_output=True, shell=True, cwd=target_folder)

    if ret.returncode != 0:
        raise Exception(f"Failed to checkout the commit {ref} in the repository.")

    return ret.stdout.decode()


def setup_dependencies(target_folder: str) -> str:
    """
    Setup and install dependencies for the project.
    This function will invoke python3 to create a virtual environment,
    then install the dependencies listed in `requirements-dev.txt`.
    :param destination: The root folder of the project.
    :return: The CLI logs from the setup process.
    :raises: Exception if the target folder does not exist or if the installation fails.
    """
    if not check_if_folder_exists(target_folder):
        raise Exception(f"The target folder ${target_folder} does not exist.")

    command = "python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.txt"
    ret = subprocess.run(command, capture_output=True, shell=True, cwd=target_folder)

    if ret.returncode != 0:
        raise Exception(f"Failed to install dependencies for ${target_folder}.")

    return ret.stdout.decode()


def run_linter_check(target_folder: str) -> tuple[bool, str]:
    """
    Run the linter on the project.
    This function will invoke the linter tool to check for syntax errors.
    :param target_folder: The root folder of the project.
    :return: True if the linter passes, False if the linter fails. Also return the CLI logs from the linter process.
    :raises: Exception if the target folder does not exist.
    """
    # TODO: Implement this function and clean up mock return value.
    # Note that we should call Flake8, but only check for E999 errors (syntax errors).
    # See https://flake8.pycqa.org/en/latest/user/violations.html#selecting-violations-with-flake8 and
    # https://flake8.pycqa.org/en/latest/user/error-codes.html for more information.
    return (True, "Mock logs: No syntax errors found.")


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
