# Run CI server with uvicorn
uvicorn:
	uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload-exclude ./temp/** --reload

# Run unittests
test:
	python -m unittest

# Start docker development (with hot reload)
docker_dev:
	docker compose --profile dev up --watch --build

# Docker production environment (automatic rebuild upon file changes)
docker_prod:
	docker compose --profile prod up --watch --build

# Docker production environment (requires manual rebuilding)
docker_man:
	docker compose --profile prod up --build

# Start ngrok forwarding
ngrok:
	ngrok http --url=secretly-native-ant.ngrok-free.app 8001

# Help message to describe all targets
help:
	@echo "Makefile Help:"
	@echo ""
	@echo "Available targets:"
	@echo "  uvicorn        - Run CI server with uvicorn (hosted at 0.0.0.0:8001)"
	@echo "  test           - Run unit tests with unittest"
	@echo "  docker_dev     - Start Docker development environment with hot reload"
	@echo "  docker_prod    - Start Docker production environment with automatic rebuild"
	@echo "  docker_man     - Start Docker production environment (requires manual rebuild)"
	@echo "  ngrok          - Start ngrok forwarding"
	@echo ""
	@echo "Usage:"
	@echo "  make <target>    - Run the specified target"
	@echo "  make help        - Display this help message"
