# DD2480 Spring 2025 Assignment 2 - Group 1

## What is this?

This repository serves as the code base of a CI/CD server.

For more information, please refer to the course [DD2480](https://www.kth.se/student/kurser/kurs/DD2480?startterm=20251&l=en).

## How to setup

The prerequisites:
- Python >=3.12
- Git
- Docker

As a developer, you should first run the following:
```bash
# activate venv to avoid package conflicts
python3.12 -m venv .venv
source .venv/bin/activate
# install required packages, and setup pre-commit hooks
pip install -r requirements-dev.txt 
pre-commit install
```

Optionally, you can find the VS code extensions for Black formatter and Flake8 linter [here](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) and [there](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8).

Despite the ability to run the application locally, it is highly recommended to use [Docker](https://www.docker.com/) for active development or service deployment:
```bash
# start development (with hot reload)
docker compose --profile dev up --watch
# production environment (automatic rebuild upon file changes)
docker compose --profile prod up --watch
# production environment (requires manual rebuilding)
docker compose --profile prod up
```
```bash
# alternatively, start development locally
uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload-exclude ./temp/** --reload
# you can only run unit tests locally
python -m unittest
```

Either way, after serving the application, you should now see the API docs available at http://localhost:8081.

## Project specifications

⚠️ Note that HTTPS is currently not supported.

## Statement of contributions

### Kam Ting Hoi

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Johan Nilsson

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Marcello Krahforst

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

### Arvid Hjort

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.

## Way of working

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec eros orci. Nunc euismod et nulla eu pretium. Aenean vitae nisl dictum, semper nunc vel, faucibus velit. Proin eu viverra ante. Cras maximus enim odio, at pretium enim fermentum at. Nulla non ligula enim. Nullam eget lacus eget ex lacinia tempor sit amet quis est. Praesent eleifend erat eget magna feugiat congue. Cras accumsan neque eget erat consequat gravida. Cras posuere metus eget est tristique imperdiet.
