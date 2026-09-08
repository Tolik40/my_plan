# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ClientNotes
def get_schema_version():
    """Возвращает текущую версию схемы данных."""
    return 46

def migrate_to_v46(data: dict) -> dict:
    """Миграция: добавляем поле is_active в Contact и Note,
    а также поле priority в Task.
    Возвращает обновлённый data."""
    if "schema_version" not in data:
        data["schema_version"] = 46

    for contact in data.get("contacts", []):
        contact.setdefault("is_active", True)

    for note in data.get("notes", []):
        note.setdefault("is_active", True)

    for task in data.get("tasks", []):
        task.setdefault("priority", "medium")

    return data
