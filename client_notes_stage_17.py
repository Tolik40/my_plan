# === Stage 17: Добавь группировку записей по категориям ===
# Project: ClientNotes
def group_records_by_category(records, categories=None):
    if not records: return {}
    if categories is None: categories = ['contacts', 'meetings', 'tasks', 'decisions']
    grouped = {cat: [] for cat in categories}
    for rec in records:
        key = rec.get('type') or rec.get('_category') or 'other'
        if key not in grouped: key = 'other'
        grouped[key].append(rec)
    return grouped
