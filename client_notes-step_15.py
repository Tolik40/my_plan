# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ClientNotes
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    if not records: return {}
    dates = sorted(set(r.get("date") for r in records))
    stats = {}
    current_date = None
    week_start = None
    for d in dates:
        if current_date is None or (d - current_date).days > 7:
            if current_date and week_start:
                duration_days = (current_date - week_start).days + 1
                stats[week_start] = {"count": len(records), "avg_duration_hours": round(sum(r.get("duration", 0) for r in records) / max(len(records), 1), 2)}
            current_date, week_start = d, d
        else:
            if not week_start: week_start = d
    if current_date and week_start:
        duration_days = (current_date - week_start).days + 1
        stats[week_start] = {"count": len(records), "avg_duration_hours": round(sum(r.get("duration", 0) for r in records) / max(len(records), 1), 2)}
    return stats
