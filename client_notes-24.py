# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ClientNotes
def print_record(record):
    if not record:
        return
    print(f"ID: {record['id']}")
    print(f"Тип: {record.get('type', 'unknown')}")
    for key, value in record.items():
        if key not in ('id', 'type'):
            print(f"{key}: {value}")
