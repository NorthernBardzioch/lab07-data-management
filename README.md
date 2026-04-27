# Lab07 – Data Management with .env and gdown

## Konfiguracja środowiska

1. Skopiuj szablon zmiennych:
   ```
   cp .env.example .env
   ```
2. Wprowadź w `.env` poprawny `GDRIVE_FILE_ID` (identyfikator pliku z Google Drive).
3. Zainstaluj zależności:
   ```
   pip install -r requirements.txt   # lub uv sync
   ```
4. Pobierz dane:
   ```
   python download_test_data.py
   ```
5. Uruchom program:
   ```
   python main.py
   ```

## Struktura projektu

- `.env.example` – szablon zmiennych konfiguracyjnych
- `download_test_data.py` – pobiera dane z Google Drive do katalogu `data/`
- `main.py` – przykładowa aplikacja korzystająca z pobranych danych
- `data/` – katalog z danymi (ignorowany przez git)
```