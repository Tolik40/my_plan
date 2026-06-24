# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ClientNotes
import json, os

DATA_FILE = 'client_notes.json'

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {'contacts': [], 'meetings': [], 'tasks': [], 'decisions_history': []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Ошибка чтения файла данных. Начиная с чистого листа.")
        return {'contacts': [], 'meetings': [], 'tasks': [], 'decisions_history': []}

def get_data():
    data = load_data()
    save_data(data)  # Синхронизация после загрузки, если данные изменились в памяти (опционально)
    return data
