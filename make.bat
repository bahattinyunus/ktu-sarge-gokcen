@echo off

if "%1" == "" goto help

if "%1" == "install" (
    pip install -r requirements.txt
    goto :eof
)

if "%1" == "test" (
    python -m unittest discover tests
    goto :eof
)

if "%1" == "format" (
    black .
    isort .
    goto :eof
)

if "%1" == "run-flight" (
    python src\simulation\rocket_flight.py
    goto :eof
)

if "%1" == "run-telemetry" (
    python src\telemetry\sender_sim.py
    goto :eof
)

if "%1" == "run-ground" (
    python src\telemetry\receiver_sim.py
    goto :eof
)

if "%1" == "analyze" (
    python src\analysis\plot_data.py
    goto :eof
)

if "%1" == "report" (
    python src\analysis\generate_report.py
    goto :eof
)

if "%1" == "run-dashboard" (
    streamlit run src\dashboard\dashboard.py
    goto :eof
)

if "%1" == "docker-up" (
    docker-compose up --build
    goto :eof
)

if "%1" == "docker-down" (
    docker-compose down
    goto :eof
)

:help
echo Usage: make.bat [command]
echo Commands:
echo   install       Install dependencies
echo   test          Run tests
echo   format        Format code
echo   run-flight    Run flight simulation
echo   run-telemetry Run telemetry simulation
echo   run-ground    Run ground station receiver
echo   analyze       Analyze flight data (generate plot)
echo   run-dashboard Run mission control dashboard (Streamlit)
echo   docker-up     Run entire system in Docker
echo   docker-down   Stop Docker containers
goto :eof
