# File Automation

## Objective

This project was developed to practice Python automation by organizing files in a directory according to their file extensions.

The project simulates a simple filesystem automation task, using Python to identify file types, create category directories, and move files automatically.

## What the Script Does

- Scans the `downloads` directory.
- Ignores directories.
- Identifies file extensions.
- Converts extensions to lowercase for consistent processing.
- Categorizes known file types using a dictionary.
- Creates category directories when necessary.
- Moves files to their corresponding category directories.
- Moves unsupported file types to the `others` directory.
- Keeps the original file names when moving files.

## Technologies Used

- Python
- `pathlib`
- File system automation
- Dictionaries
- Loops and conditional logic
- Git & GitHub

## How to Use

1. Clone the repository:
```
git clone https://github.com/voncod/python-phase1/new/main/python-phase1/01_server_health_report.dir
cd python-phase1
```
2. Navigate to the project directory:
```
cd 03_file_automation.dir
```
3. Place the files you want to organize inside the downloads directory.

4. Run the script:
```
python file_organizer.py
```
5. The script will automatically create the required category directories and move the files.

## Example Output

Before running the script:
```
downloads/
├── foto.jpg
├── documento.pdf
├── script.py
├── dados.json
├── notas.txt
└── musica.mp3
```
After running the script:
```
downloads/
├── images/
│   └── foto.jpg
├── documents/
│   ├── documento.pdf
│   └── notas.txt
├── python/
│   └── script.py
├── json/
│   └── dados.json
└── others/
    └── musica.mp3
```
## Project Structure
```
03_file_automation.dir/
├── file_organizer.py
└── downloads/
    ├── images/
    ├── documents/
    ├── python/
    ├── json/
    └── others/
```
## Learning Objectives

- Practice Python filesystem automation.
- Use pathlib to work with files and directories.
- Iterate through directory contents.
- Check whether a path represents a file.
- Extract and normalize file extensions.
- Use dictionaries to map file extensions to categories.
- Create directories programmatically.
- Move files using Python.
- Practice automation concepts relevant to Cloud and Infrastructure tasks.

## Notes

- This is a learning project focused on Python automation and filesystem manipulation.
- The goal was to build a functional and understandable solution rather than a production-ready file management system.
- The project represents an early step in using Python as an automation tool for Cloud and Infrastructure tasks.
