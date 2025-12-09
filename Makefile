.PHONY: install test format run-flight run-telemetry run-ground analyze run-dashboard docker-up docker-down

install:
	pip install -r requirements.txt

test:
	python -m unittest discover tests

format:
	black .
	isort .

run-flight:
	python src/simulation/rocket_flight.py

run-telemetry:
	python src/telemetry/sender_sim.py

run-ground:
	python src/telemetry/receiver_sim.py

analyze:
	python src/analysis/plot_data.py

run-dashboard:
	streamlit run src/dashboard/dashboard.py

docker-up:
	docker-compose up --build

docker-down:
	docker-compose down
