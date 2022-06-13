PROJECT=thepeak_spotify
PROJECT_APP=${PROJECT}_app_1

style: black flake8 isort pydocstyle mypy requirements
	@echo "🎉 style passed!"

black:
	black . --line-length=79
	@echo "✅ black done."

flake8:
	flake8
	@echo "✅ flake done."

isort:
	isort . --profile black
	@echo "✅ isort done."

pydocstyle:
	pydocstyle
	@echo "✅ pydocstyle done."

mypy:
	mypy
	@echo "✅ mypy done."

requirements:
	poetry export --without-hashes --output requirements.txt
	poetry export --dev --without-hashes --output requirements.dev.txt
	@echo "✅ requirements done."

clean:
	pyclean -v .
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .aws-sam
	@echo "♲ clean done."

build:
	docker-compose -p ${PROJECT} build
	@echo "📦 build complete."

up:
	docker-compose -p ${PROJECT} up -d
	docker container logs --follow ${PROJECT_APP}

down:
	docker-compose -p ${PROJECT} down
	@echo "✅ containers stopped."

shell:
	docker exec -it ${PROJECT_APP} sh
