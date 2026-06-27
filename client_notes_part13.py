# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ClientNotes
def search_notes(query, fields=None):
    if not query:
        return []
    query = query.lower().strip()
    if fields is None:
        fields = ['name', 'phone', 'email', 'notes']
    results = []
    for note in notes_db:
        match_found = False
        for field_name in fields:
            value = getattr(note, field_name, '')
            if query in str(value).lower():
                match_found = True
                break
        if match_found:
            results.append(note)
    return results
