# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ClientNotes
def check_overdue_reminders():
    """Выводит список просроченных напоминаний."""
    now = datetime.now()
    overdue = []
    for note in client_notes:
        if note.get("type") == "reminder":
            due = datetime.fromisoformat(note["due"])
            if now > due and note not in overdue:
                overdue.append(note)
    return overdue
