# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ClientNotes
def edit_note(note_id: int, updates: dict) -> Optional[dict]:
    notes_lock.acquire()
    try:
        for i, note in enumerate(notes):
            if note['id'] == note_id:
                if 'content' not in updates or updates.get('content') is None:
                    del note['history']
                    note.update(updates)
                else:
                    old_content = note.pop('content', '')
                    new_history_entry = {
                        'timestamp': datetime.now(),
                        'action': 'edit',
                        'old_value': old_content,
                        'new_value': updates.get('content') or ''
                    }
                    if not note['history']:
                        note['history'] = []
                    note['history'].insert(0, new_history_entry)
                return note.copy()
        raise ValueError(f"Note with id {note_id} not found")
    finally:
        notes_lock.release()
