.PHONY: install test format run-flight run-telemetry run-ground analyze

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
