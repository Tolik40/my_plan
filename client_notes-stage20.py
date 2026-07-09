# === Stage 20: Добавь восстановление записей из архива ===
# Project: ClientNotes
import json, os
ARCHIVE_FILE = "archive.json"

def restore_records():
    if not os.path.exists(ARCHIVE_FILE):
        return None
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            records = json.load(f)
        for r in records:
            _append_record(r)
        print(f"Восстановлено {len(records)} записей из архива.")
        return len(records)
    except Exception:
        return 0

def _append_record(rec):
    with open(ARCHIVE_FILE, 'w', encoding='utf-8') as f:
        json.dump([rec] + [], f)
