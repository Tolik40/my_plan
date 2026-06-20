# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ClientNotes
import json, os, uuid, datetime as dt

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
    
    now = dt.datetime.now()
    if "contacts" not in data or isinstance(data["contacts"], list):
        contacts = [c for c in data.get("contacts", [])]
    else:
        contacts = []

    if "meetings" not in data or isinstance(data["meetings"], list):
        meetings = [m | {"createdAt": now.isoformat()} for m in data.get("meetings", [])]
    else:
        meetings = []

    if "tasks" not in data or isinstance(data["tasks"], list):
        tasks = [t | {"status": "pending"} for t in data.get("tasks", [])]
    else:
        tasks = []

    history_entries = data.get("history", [])
    
    return {
        "contacts": contacts,
        "meetings": meetings,
        "tasks": tasks,
        "history": history_entries,
        "_meta": {"lastImportedAt": now.isoformat(), "version": 1}
    }

def save_to_file(data: dict, filename: str = "client_notes.json") -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except IOError as e:
        print(f"Ошибка записи файла: {e}")

if __name__ == "__main__":
    initial_json = '''
{
  "contacts": [
    {"id": "c1", "name": "Иван Петров", "phone": "+79001234567"},
    {"id": "c2", "name": "Анна Сидорова", "email": "anna@example.com"}
  ],
  "meetings": [
    {"title": "Обсуждение проекта", "client_id": "c1", "date": "2023-10-25T14:00:00Z", "notes": "Подготовить смету"}
  ],
  "tasks": [
    {"title": "Вызвать Ивана Петрова", "client_id": "c1", "priority": "high"},
    {"title": "Отправить договор Анне Сидоровой", "client_id": "c2", "priority": "medium"}
  ],
  "history": [
    {"action": "created_contact", "entity_id": "c1", "timestamp": "2023-10-24T10:00:00Z"},
    {"action": "scheduled_meeting", "meeting_id": "m1", "timestamp": "2023-10-25T09:00:00Z"}
  ]
}'''

    loaded
