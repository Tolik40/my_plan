# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ClientNotes
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "version": 1,
        "exported_at": datetime.now().isoformat(),
        "contacts": list(contacts.values()),
        "meetings": list(meetings.values()),
        "tasks": list(tasks.values()),
        "decisions": decisions_list.copy() if hasattr(decisions, 'copy') else []
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
