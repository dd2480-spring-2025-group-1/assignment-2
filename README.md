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

### Testing

### Notification

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

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Arvid Hjort

I worked primarily on core CI feature #3 - notification. Meaning that I worked and coded in files src/modules/notifications.py and tests/test_notifications.py. I also set up a Github token to authenticate the program so it could communicate with github.

## Way of working

Considering that each memeber of our group was given tasks in the beginning of the project and was able to individually fulfill them, we would argue that we fulfill all the requirements for the "Seeded" and "Formed" state. This is further undermined by our regular meetings and discussions on Discord.
We would go further and consider ourselves as being in the "Collaborating" state since we are able to effectively work as one cohesive unit and are open and honest in our communication and code reviews. We trust each other to fulfill their tasks and reach out in case there are any difficulties.
Although our team consistently met commitments and is continuosly adapting to the changing context as well as achieving effective progress, we would argue that we are not yet at the "Performing" state. This is largely due to us not being able to fully prevent wasted work since we are still learning to have a common coding style that is accepted by all of us and we sometimes struggle to keep everyone up to date on the latest plans or changes which occasionally causes slight inefficacies.
