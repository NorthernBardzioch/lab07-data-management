import os
import gdown
from dotenv import load_dotenv

load_dotenv()  # wczytuje zmienne z .env

DATA_DIR = os.getenv("DATA_DIR", "data")
os.makedirs(DATA_DIR, exist_ok=True)

file_id = os.getenv("GDRIVE_FILE_ID")
if not file_id or file_id == "XXXXXXXXXXXXXXXXXXXXXXXXX":
    print("Ustaw poprawny GDRIVE_FILE_ID w pliku .env")
    exit(1)

output_path = os.path.join(DATA_DIR, "dane.txt")
gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)
print(f"Plik zapisany w {output_path}")
