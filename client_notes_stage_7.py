# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ClientNotes
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(rec):
        val = rec.get(key)
        if isinstance(val, str):
            try: int(val); return (0, val)
            except ValueError: return (1, val.lower())
        elif key == 'priority':
            p_map = {'high': 0, 'medium': 1, 'low': 2}
            return (p_map.get(val.lower(), 3), '')
        else: return (0, str(val))
    sorted_records = sorted(records, key=get_sort_key)
    if reverse and key == 'date':
        sorted_records.reverse()
    return sorted_records
