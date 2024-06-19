lint:
	docker compose run --rm web sh -c "mypy . ; flake8 ."
test:
	docker compose run --rm web pytest
