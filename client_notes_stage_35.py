# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ClientNotes
def next_action_suggestions(app):
    """Return priority-ranked suggested actions based on the current state."""
    suggestions = []

    # 1) Overdue tasks first
    now = datetime.now()
    overdue = [t for t in app.tasks if t['due'] and t['due'] < now and not t.get('resolved')]
    if overdue:
        suggestions.append({"action": "review_overdue_tasks", text: f"{len(overdue)} task(s) are past due. Review them.", priority: 1})

    # 2) Tasks due today
    due_today = [t for t in app.tasks if t['due'] and t['due'].date() == now.date() and not t.get('resolved')]
    if due_today:
        suggestions.append({"action": "focus_on_due_tasks", text: f"{len(due_today)} task(s) are due today. Focus on them.", priority: 2})

    # 3) Upcoming meetings in next 7 days
    upcoming = [m for m in app.meetings if m['date'] and m['date'] >= now and (m['date'] - now).days <= 7]
    if upcoming:
        suggestions.append({"action": "prepare_for_meetings", text: f"{len(upcoming)} meeting(s) in the next week. Prepare notes.", priority: 3})

    # 4) Contacts without any activity for a long time
    inactive = [c for c in app.contacts if not any(
        rec['date'] and (now - datetime.fromisoformat(rec['date'])).days < 90
        for rec in c.get('notes', [])
    )]
    if inactive:
        suggestions.append({"action": "reach_out_to_contacts", text: f"{len(inactive)} contact(s) have no recent activity. Consider reaching out.", priority: 4})

    # 5) Tasks without assigned client (orphan tasks)
    orphaned = [t for t in app.tasks if not t.get('client_id')]
    if orphaned:
        suggestions.append({"action": "assign_orphan_tasks", text: f"{len(orphaned)} task(s) have no client. Assign them.", priority: 5})

    # Sort by priority and return top 3
    return sorted(suggestions, key=lambda x: x['priority'])[:3] or [{"action": "all_clear", text: "Everything looks up to date!", priority: 0}]
