# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ClientNotes
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags is not None:
            rec_tags = set(record.get('tags', []))
            if tags and not any(t in rec_tags for t in tags):
                continue
        filtered.append(record)
    return filtered

def search_records(query=None, status=None, category=None, tags=None):
    query_lower = query.lower() if query else ''
    results = filter_records(status=status, category=category, tags=tags)
    if not query:
        return results
    def matches(record):
        text = f"{record.get('name', '')} {record.get('notes', '')}".lower()
        return query_lower in text or any(query_lower in str(t).lower() for t in record.get('tags', []))
    return [r for r in results if matches(r)]
