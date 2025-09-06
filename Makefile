.PHONY: exec init up down restart logs status clean

init:
	@docker compose up airflow-init

up: init
	@docker-compose up -d --build

down:
	@docker-compose down

restart: down up

logs:
	@docker-compose logs -f

status:
	@docker-compose ps

stop:
	@docker-compose stop

clean: stop
	@docker-compose rm -a -f
	@docker volume prune -a -f
	@docker system prune -a -f

# Lint Scripts Locally
lint:
	@ruff check ./backend

test: lint
	pytest ./tests -v

clear_pycache:
	@find . -type d -name '__pycache__' -exec rm -rf {} +

clear_ruff: clear_pycache
	@find . -type d -name '.ruff_cache' -exec rm -rf {} +

clear_pytest: clear_ruff
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +

clear: clear_pytest

add:
	   git add .

commit: add
	    git commit -m $(COMMIT_MSG)

push: commit
	     git push

all: add commit push