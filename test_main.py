import os
import tempfile
import pytest
from main import analyze_data

def test_analyze_data():
    # Tworzymy tymczasowy plik z testową zawartością
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as tmp:
        tmp.write("Linia 1\nLinia 2\nLinia 3\nLinia 4\n")
        tmp_path = tmp.name

    try:
        count, first = analyze_data(tmp_path)
        assert count == 4
        assert first == ["Linia 1", "Linia 2", "Linia 3"]
    finally:
        os.unlink(tmp_path)

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        analyze_data("/nie/ma/takiego/pliku")