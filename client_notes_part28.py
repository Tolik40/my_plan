# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ClientNotes
def project_metrics():
    return {
        "total_clients": len(client_notes),
        "meeting_count": sum(1 for c in client_notes if getattr(c, 'meetings', [])),
        "active_tasks": sum(1 for t in tasks.values() if getattr(t, 'status', '') == 'active'),
    }
