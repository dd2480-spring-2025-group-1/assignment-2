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
        err = Exception(f"Failed cloning into repository {url}.")
        err.add_note(ret.stderr.decode())
        raise err

    # Git commands outputs information message on stderr
    # see https://stackoverflow.com/questions/57016157/how-to-stop-git-from-writing-non-errors-to-stderr
    return ret.stderr.decode()


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
        err = Exception(f"Failed to checkout the commit {ref} in the repository.")
        err.add_note(ret.stderr.decode())
        raise err

    # Git commands outputs information message on stderr
    # see https://stackoverflow.com/questions/57016157/how-to-stop-git-from-writing-non-errors-to-stderr
    return ret.stderr.decode()


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

    command = "python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-dev.txt"
    ret = subprocess.run(command, capture_output=True, shell=True, cwd=target_folder)

    if ret.returncode != 0:
        err = Exception(f"Failed to install dependencies for {target_folder}.")
        err.add_note(ret.stderr.decode())
        raise err

    return ret.stdout.decode()


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

    flake_command = "flake8 --select E9,F63,F82,F7 ."
    result = subprocess.run(
        flake_command, capture_output=True, shell=True, cwd=target_folder
    )

    success = result.returncode == 0

    if result.stdout:
        logs = "Linting Log: \n" + result.stdout.decode()
    else:
        logs = "Linting Log: No syntax errors found."

    return (success, logs)


def run_tests(target_folder: str) -> tuple[bool, str]:
    """
    Run the tests on the project.
    This function will invoke the test runner to execute the test suite.
    :param target_folder: The root folder of the project.
    :return: True if all the tests pass, False if some tests fail. Also return the CLI logs from the test process.
    :raises: Exception if the target folder does not exist.
    """
    if not check_if_folder_exists(target_folder):
        raise ValueError(f"The provided path {target_folder} is not a valid directory.")

    test_command = ". .venv/bin/activate && python -m unittest"
    result = subprocess.run(
        test_command, capture_output=True, shell=True, cwd=target_folder
    )

    success = result.returncode == 0

    if result.stderr:
        logs = "Test Log: \n" + result.stderr.decode()
    else:
        logs = "Test Log: No test results found."

    return (success, logs)
