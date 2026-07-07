# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ClientNotes
def archive_completed_records(records, threshold_days=365):
    """Archive records older than threshold_days or with completed status."""
    import datetime
    cutoff = datetime.datetime.now() - datetime.timedelta(days=threshold_days)
    archived = []
    active = []
    for r in records:
        if (r.get("status") == "completed" and datetime.datetime.fromisoformat(r["created_at"]) < cutoff) or \
           datetime.datetime.fromisoformat(r["created_at"]) < cutoff:
            r["archived"] = True
            archived.append(r)
        else:
            r["archived"] = False
            active.append(r)
    return {"active": active, "archived": archived}
