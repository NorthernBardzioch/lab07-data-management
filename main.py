import os
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
dane_path = os.path.join(DATA_DIR, "dane.txt")

if not os.path.exists(dane_path):
    print(f"Brak pliku {dane_path}. Uruchom najpierw: python download_test_data.py")
    exit(1)

with open(dane_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Liczba linii: {len(lines)}")
print(f"Pierwsze 3 linie:")
for line in lines[:3]:
    print(f"  {line.rstrip()}")
