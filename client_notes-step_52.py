# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: ClientNotes
def export_report(catalog, contacts, meetings, tasks, decisions):
    """Экспорт краткого отчёта в текстовом формате."""
    lines = ["=== ClientNotes Отчёт ===", f"Дата: {datetime.now().strftime('%Y-%m-%d')}", ""]
    lines.append(f"Контактов: {len(contacts)}")
    lines.append(f"Встреч: {len(meetings)}")
    lines.append(f"Задач: {len(tasks)}")
    lines.append(f"Решений: {len(decisions)}")
    lines.append("")
    for c in contacts:
        lines.append(f"  Контакт: {c['name']} ({c['phone']})")
    for m in meetings:
        lines.append(f"  Встреча: {m['title']} ({m['date']})")
    for t in tasks:
        lines.append(f"  Задача: {t['title']} [{t['status']}]")
    for d in decisions:
        lines.append(f"  Решение: {d['title']} ({d['date']})")
    return "\n".join(lines)
