# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ClientNotes
def calculate_monthly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'contacts': 0, 'meetings': 0, 'tasks': 0, 'decisions': 0})
    for r in records:
        date_str = r.get('date', '')
        if not date_str or len(date_str) < 7: continue
        try:
            year_month = (int(date_str[:4]), int(date_str[5:7]))
        except ValueError:
            continue
        key = f"{year_month[0]:02d}-{year_month[1]:02d}"
        if r.get('type') == 'contact': stats[key]['contacts'] += 1
        elif r.get('type') == 'meeting': stats[key]['meetings'] += 1
        elif r.get('type') == 'task': stats[key]['tasks'] += 1
        elif r.get('type') == 'decision': stats[key]['decisions'] += 1
    return dict(sorted(stats.items()))
