import os
from dotenv import load_dotenv

def analyze_data(filepath):
    """Wczytuje plik i zwraca liczbę linii oraz pierwsze 3 linie."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Brak pliku {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines), [line.rstrip() for line in lines[:3]]

def main():
    load_dotenv()
    DATA_DIR = os.getenv("DATA_DIR", "data")
    dane_path = os.path.join(DATA_DIR, "dane.txt")

    try:
        num_lines, first_lines = analyze_data(dane_path)
    except FileNotFoundError as e:
        print(e)
        print("Uruchom najpierw: python download_test_data.py")
        exit(1)

    print(f"Liczba linii: {num_lines}")
    print("Pierwsze 3 linie:")
    for line in first_lines:
        print(f"  {line}")

if __name__ == "__main__":
    main()