# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: ClientNotes
def get_client_summary(client_id):
    """
    Возвращает краткое резюме по клиенту:
    имя, статус, активные задачи, ближайшие встречи.
    """
    client = find_client_by_id(client_id)
    if not client:
        return None

    active_tasks = [t for t in get_tasks() if t['client_id'] == client_id and t['status'] == 'active']
    upcoming_meetings = [m for m in get_meetings() if m['client_id'] == client_id and m['date'] >= today()]

    return {
        'name': client['name'],
        'status': client['status'],
        'active_tasks_count': len(active_tasks),
        'upcoming_meetings_count': len(upcoming_meetings),
        'next_meeting': upcoming_meetings[0]['date'] if upcoming_meetings else None,
    }
