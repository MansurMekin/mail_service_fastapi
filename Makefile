up-dev:
	docker-compose -f docker-compose-dev.yaml up --build

down-dev:
	docker-compose -f docker-compose-dev.yaml down -v

up-tests:
	docker-compose -f docker-compose-test.yaml up --build

down-tests:
	docker-compose -f docker-compose-test.yaml down -v

up-prod:
	docker-compose -f docker-compose-prod.yaml up --build

down-prod:
	docker-compose -f docker-compose-prod.yaml down -v

lint:
	poetry run pre-commit run --all-files
