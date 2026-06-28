# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ClientNotes
def generate_summary():
    print("=== СВОДКА КЛИЕНТНОГО ЖУРНАЛА ===")
    if not contacts:
        print("Контактов нет.")
        return
    for c in sorted(contacts.values(), key=lambda x: x.get('last_contact', 0), reverse=True):
        name = c['name']
        phone = c.get('phone', 'N/A')
        last = c.get('last_contact', 'Никогда').split()[-1] if isinstance(c.get('last_contact'), str) else 'Нет'
        print(f"[{name}] {phone} — последняя связь: {last}")
    tasks_count = sum(1 for t in all_tasks.values() if not t['completed'])
    meetings_count = len(all_meetings)
    decisions_count = len(decisions_history)
    print(f"Активных задач: {tasks_count}, Встреч: {meetings_count}, Решений: {decisions_count}")
