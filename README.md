# DD2480 Spring 2025 Assignment 2 - Group 1

## What is this?

This repository serves as the code base of a CI/CD server.

For more information, please refer to the course [DD2480](https://www.kth.se/student/kurser/kurs/DD2480?startterm=20251&l=en).

## How to setup

The prerequisites:
- Python <=3.11
- Git
- Docker

Firstly, you need to obtain a github token ([user access token](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app), [installation access token](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app), or [fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) should all work) to setup the credentials:
```bash
cp .env.sample .env
nano .env # update your github token
```

As a developer, you should first run the following to install relevant dependencies:
```bash
# activate venv to avoid package conflicts
python3.11 -m venv .venv
source .venv/bin/activate
# install required packages, and setup pre-commit hooks
pip install -r requirements-dev.txt
pre-commit install
```

Optionally, you can find the VS code extensions for Black formatter and Flake8 linter [here](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) and [there](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8).

You should now be able to run the application! Despite the ability to serve the application locally, it is highly recommended to use [Docker](https://www.docker.com/) for active development or service deployment:
```bash
# start development (with hot reload)
make docker_dev
# production environment (automatic rebuild upon file changes)
make docker
# production environment (requires manual rebuilding)
make docker_man
```
```bash
# alternatively, start development locally
make uvicorn_dev
# you can only run unit tests locally
make test
```

Either way, after serving the application, you should now see the API docs available at http://localhost:8001/redoc (recommended) or http://localhost:8001/docs.

For deployment on the KTH server it is recommended to use tmux in order to use multiple terminals in one session and detaching them. You will have to both start the server and forward the port from the CI server.

For forwarding the CI server port you will need the to set up ngrok as explained [here](https://ngrok.com/docs/guides/device-gateway/linux/) and add the token from our group. After that you can execute the following command:
```bash
make ngrok
```

Note: In case you are unsure about the available commands you can run `make help` for a help message with all the available commands


## Project specifications

⚠️ Note that HTTPS is currently not supported.

## How it works

### Static Syntax Check

The static syntax check is done by executing the `run_linter_check` function which is called in the CI servers processing pipeline in the main function. The `run_linter_check` function executes a check with flake8 on the respective target folder with flags to only look for E9,F63,F82,F7 errors, which we deemed as indicating of potential syntax errors.

Unit testing is performed by running the linting check on a series of fixture folders in the tests folder. Some folders contain code that should pass the check without triggering any errors and others contain code that are supposed to trigger the various errors we are checking for. The output of flake8 is then checked to make sure it contains certain keywords that indicate right behaviour.

### Testing

Testing was implemented with the _unittest_ python library. Each function has its respective unittests in the _tests_ folder in order to test the functionality in a minimal way. The CI main function pipeline executes the `run_tests` function which in turn runs the shell command that initializes the tests inside a target folder and stores the output given after execution.

Unit testing is performed by running the `run_tests` function inside of fixture folders in the tests folder. These fixtures contain very simple tests that should fail or tests that pass.

### Notification
Notifications uses two functions to operate: 'add_commit_status' and 'get_commit_status'. They both utilize REST API and requests to communicate with Github. They update and read commit statuses respectively. When a commit is pushed a webhook activates the API endpoints in main that later goes through testing. The status gets updated accordingly. It is important to have a Github personal access token in environmental variables that authenticates the user.

Unit testing is performed on a mockup that validates that a Github token exists and catches a bad request. Then 'add_commit_status' tries to change the status of a dummy commit and 'get_commit_status' reads it to see if it was successful.

### Links
Use this link to access a list of all build logs: https://secretly-native-ant.ngrok-free.app/logs

Then, access the build log you want to read by inserting the ID of it in the url: https://secretly-native-ant.ngrok-free.app/logs/{id}

## Statement of contributions

### Kam Ting Hoi

I mainly worked on `clone_repo` and `setup_dependencies`, which were fundamental for the CI actions service (#10).

Besides, I facilitated our group's development velocity by:
- initializing the repository with basic file structures and function skeletons (#12, #14, #17).
- containerising the application using docker for easier setup and deployment (#6).
- adding basic utility functions for file operations (#9).

Finally, I was responsible for various bug fixes and integrating the application (#54, #57).

### Johan Nilsson

I worked on property 7 which was that the CI server keeps the history of the past builds and that it persists. I made each build accessible through its' own url with a main url which lists all builds. My work is located in src/modules/logs.py and tests are in tests/test_logs.py .I also reviewed some PRs.

### Marcello Krahforst

I mainly worked on the `syntax check` and `testing` functionality of the CI server. Besides that, I created the Makefile for a easier execution of important commands, set up the kth server as our CI server and wrote the Way of Working for this assignment.

### Arvid Hjort

I worked primarily on core CI feature #3 - notification. Meaning that I worked and coded in files src/modules/notifications.py and tests/test_notifications.py. I also set up a Github token to authenticate the program so it could communicate with github.

## Way of working

Considering that each memeber of our group was given tasks in the beginning of the project and was able to individually fulfill them, we would argue that we fulfill all the requirements for the "Seeded" and "Formed" state. This is further undermined by our regular meetings and discussions on Discord.
We would go further and consider ourselves as being in the "Collaborating" state since we are able to effectively work as one cohesive unit and are open and honest in our communication and code reviews. We trust each other to fulfill their tasks and reach out in case there are any difficulties.
Although our team consistently met commitments and is continuosly adapting to the changing context as well as achieving effective progress, we would argue that we are not yet at the "Performing" state. This is largely due to us not being able to fully prevent wasted work since we are still learning to have a common coding style that is accepted by all of us and we sometimes struggle to keep everyone up to date on the latest plans or changes which occasionally causes slight inefficacies.
