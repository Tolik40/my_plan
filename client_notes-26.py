# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ClientNotes
def demo_mode(db):
    print("=== ClientNotes Demo ===")
    for i in range(3):
        c = db.add_client(f"Client {i+1}", f"{i+1}@demo.com", "+79000000{i+1}")
        m = db.add_note(c, "Demo note", "2025-01-01")
        db.add_task(c, "Follow up", done=False)
    print("Done")
