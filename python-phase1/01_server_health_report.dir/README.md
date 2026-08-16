# Server Health Report

## Objective

This project was developed to practice Python fundamentals by processing structured server data and generating a health report in JSON format.

The project simulates a simple infrastructure inventory/reporting task, using Python to analyze server status and environments.

## What the Script Does

- Reads server data from a `servers.json` file.
- Counts the total number of servers.
- Counts online and offline servers.
- Groups servers by environment (`prod`, `dev`, etc.).
- Creates a list of online servers with their name and environment.
- Creates an attention list for offline servers.
- Generates a structured health report.
- Saves the final report to `report.json`.

## Technologies Used

- Python
- JSON
- File handling
- Lists and dictionaries
- Git & GitHub

## How to Use

1. Clone the repository:
```
git clone https://github.com/voncod/python-phase1/new/main/python-phase1/01_server_health_report.dir
cd python-phase1
```
2. Navigate to the project directory:
```
cd 01_server_health_report.dir
```
3. Run the script:
```
python server_report.py
```
4. The generated report will be saved as:
```
report.json
```
## Example Output
```
{
    "total_servers": 6,
    "online_servers": 4,
    "offline_servers": 2,
    "by_environment": {
        "prod": 4,
        "dev": 2
    },
    "online_servers_list": [
        {
            "name": "web-01",
            "environment": "prod"
        },
        {
            "name": "db-01",
            "environment": "prod"
        }
    ],
    "attention_required_list": [
        {
            "name": "web-02",
            "reason": "offline"
        }
    ]
}
```
## Project Structure
```
├── servers.json
├── server_report.py
└── report.json
```

## Learning Objectives

- Practice Python fundamentals.
- Work with lists and dictionaries.
- Process structured JSON data.
- Read and write JSON files.
- Build nested data structures.
- Use loops and conditional logic to analyze data.
- Generate structured reports from processed data.
- Practice basic automation concepts related to infrastructure data.

## Notes

- This is a learning project focused on Python fundamentals and automation.
- The goal was to build a functional and understandable solution rather than an optimized production system.
- The project represents an early step in using Python as an automation tool for Cloud and Infrastructure tasks.
