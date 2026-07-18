# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ClientNotes
def parse_date(s):
    """Parse date strings like '2024-12-25', 'Dec 25, 2024', or relative forms."""
    if not s:
        return None
    import re
    today = datetime.date.today()
    # Relative helpers
    rel_map = {'tomorrow': (today + timedelta(days=1)).isoformat(),
               'yesterday': (today - timedelta(days=1)).isoformat()}
    for k, v in rel_map.items():
        if s.lower().strip() == k:
            return datetime.date.fromisoformat(v)
    # Absolute ISO or US form
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s.strip())
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return datetime.date(y, mo, d)
    m = re.match(r'(\w+)\s+(\d+),?\s*(\d{4})', s.strip(), re.IGNORECASE)
    if m:
        try:
            from datetime import datetime as dt
            dt.strptime(s.strip(), '%B %d, %Y')
        except ValueError:
            return None
    return None
