# Default commit message
COMMIT_MSG ?= "updated description file, added terraform files, and updated Makefile"

# Lint Scripts Locally
lint:
	ruff check ./backend

# Run Tests Locally
test: lint
	pytest ./tests -v

# Clear Uncommitted Files
clear_pycache:
	find . -type d -name '__pycache__' -exec rm -rf {} +

clear_ruff: clear_pycache
	find . -type d -name '.ruff_cache' -exec rm -rf {} +

clear_pytest: clear_ruff
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

clear: clear_pytest

# Target to add changes to staging
add:
	   git add .

# Target to commit with a message
commit: add
	    git commit -m $(COMMIT_MSG)

# Target to push to the default branch
push: commit
	     git push

# Run all targets
all: push