from pathlib import Path

folder = Path("downloads")

categories = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".py": "python",
    ".json": "json"
}

for file in folder.iterdir():

    if not file.is_file():
        continue

    extension = file.suffix.lower()

    if extension in categories:
        category = categories[extension]
    else:
        category = "others"

    destination = folder / category

    destination.mkdir(exist_ok=True)

    file.rename(destination / file.name)

