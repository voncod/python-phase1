# API Health Monitor

## Objective

This project was developed to practice Python automation by consuming an HTTP API, handling request errors, processing the API response, and generating a health report in JSON format.

The project simulates a simple API monitoring task, using Python to determine whether an API is responding successfully and to record basic information about its response.

## What the Script Does

- Reads API configuration from the `config.yaml` file.
- Retrieves the API URL and request timeout from the configuration.
- Sends a GET request to the configured API.
- Handles timeout, HTTP, and general request errors.
- Validates the HTTP response status.
- Processes the JSON response returned by the API.
- Determines whether the API is healthy or unhealthy.
- Records the HTTP status code.
- Counts the number of items returned by the API.
- Generates a structured health report.
- Saves the report to `health_report.json`.

## Technologies Used

- Python
- Requests
- YAML
- JSON
- HTTP / REST API
- File handling
- Exception handling
- Git & GitHub

## How to Use

1. Clone the repository:
```
git clone https://github.com/voncod/python-phase1/new/main/python-phase1/01_server_health_report.dir
cd python-phase1
```
2. Navigate to the project directory:
```
cd 02-api-health-monitor
```
3. Install the required dependencies:
```
pip install requests pyyaml
```
4. Run the script:
```
python api_monitor.py
```
5. The generated health report will be saved as:
```
health_report.json
```

## Example Output

```
{
    "url": "https://jsonplaceholder.typicode.com/posts",
    "status": "healthy",
    "http_status": 200,
    "items_received": 100
}
```

## Project Structure

```
├── config.yaml
├── api_monitor.py
└── health_report.json
```

## Learning Objectives

Practice consuming HTTP APIs with Python.
- Use the requests library to perform GET requests.
- Configure API settings using YAML.
- Process JSON responses.
- Handle HTTP and request-related exceptions.
- Use timeouts when making HTTP requests.
- Modify and generate structured dictionaries.
- Generate a simple health report from API data.
- Practice automation concepts relevant to Cloud and Infrastructure tasks.

## Notes

- This is a learning project focused on Python automation and basic API monitoring.
- The goal was to build a functional and understandable solution rather than a production-ready monitoring system.
- The project represents an early step in using Python to automate tasks related to Cloud, APIs, and Infrastructure.
