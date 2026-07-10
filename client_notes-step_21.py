# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ClientNotes
import datetime

def add_reminder(contacts, note_id):
    contact = contacts[note_id]
    if not contact.get('reminders'):
        contact['reminders'] = []
    while True:
        text = input("Введите текст напоминания (или 'done' для завершения): ").strip()
        if text.lower() == 'done':
            break
        date_str = input("Дата напоминания (YYYY-MM-DD) или 'now' для сегодняшнего дня: ").strip().lower()
        if date_str != 'now':
            try:
                dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                print("Неверный формат даты. Попробуйте снова.")
                continue
        else:
            dt = datetime.datetime.now()
        hour = int(input(f"Время напоминания ({dt.strftime('%H:%M')}): ").strip())
        reminder = {'text': text, 'date': dt.date(), 'time': dt.time(), 'done': False}
        contact['reminders'].append(reminder)

def check_reminders(contacts):
    today = datetime.date.today()
    for nid, c in contacts.items():
        if not c.get('reminders'):
            continue
        done_count = 0
        total = len(c['reminders'])
        for r in c['reminders']:
            if r['done']:
                done_count += 1
            elif r['date'] <= today and r['time'] < datetime.datetime.now().time():
                print(f"⚠️ Напоминание: {r['text']}")
        if total > 0:
            pct = round(done_count / total * 100)
            print(f"[{nid}] Напоминаний: {done_count}/{total} ({pct}%)")
