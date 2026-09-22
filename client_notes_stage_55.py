# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: ClientNotes
def check_duplicate_notes(notes, note_id):
    """Check if a note with the same ID already exists."""
    for note in notes:
        if note['id'] == note_id:
            print(f"Note with ID {note_id} already exists.")
            return False
    return True

def check_duplicate_contacts(contacts, contact_id):
    """Check if a contact with the same ID already exists."""
    for contact in contacts:
        if contact['id'] == contact_id:
            print(f"Contact with ID {contact_id} already exists.")
            return False
    return True

def check_duplicate_meetings(meetings, meeting_id):
    """Check if a meeting with the same ID already exists."""
    for meeting in meetings:
        if meeting['id'] == meeting_id:
            print(f"Meeting with ID {meeting_id} already exists.")
            return False
    return True

def check_duplicate_tasks(tasks, task_id):
    """Check if a task with the same ID already exists."""
    for task in tasks:
        if task['id'] == task_id:
            print(f"Task with ID {task_id} already exists.")
            return False
    return True
