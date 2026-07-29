# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ClientNotes
def undo_last_action():
    """Откат последнего действия: если последняя операция была добавление, удаляет запись."""
    if not client_notes_history:
        return
    last = client_notes_history[-1]
    kind = last.get("kind")
    if kind == "add_contact":
        client_notes_history.pop()
        contacts.remove(last["contact"])
    elif kind == "update_contact":
        client_notes_history.pop()
        update_contact(last["old"], last["new"])
    elif kind == "delete_contact":
        client_notes_history.pop()
        add_contact(contacts[-1], last.get("last_name", ""))
    elif kind == "add_meeting":
        client_notes_history.pop()
        meetings.remove(last["meeting"])
    elif kind == "update_meeting":
        client_notes_history.pop()
        update_meeting(last["old"], last["new"])
    elif kind == "delete_meeting":
        client_notes_history.pop()
        add_meeting(meetings[-1], {"date": "", "topic": ""})
    elif kind == "add_task":
        client_notes_history.pop()
        tasks.remove(last["task"])
    elif kind == "update_task":
        client_notes_history.pop()
        update_task(last["old"], last["new"])
    elif kind == "delete_task":
        client_notes_history.pop()
        add_task(tasks[-1], {"description": "", "due_date": None, "priority": 3})
    elif kind == "add_solution":
        client_notes_history.pop()
        solutions.remove(last["solution"])
