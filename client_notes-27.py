# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ClientNotes
def reset_demo_data(client_db, tasks_db, meetings_db):
    """Заполнить базы данных демо-данными для быстрого старта."""
    contacts = [
        {"id": 101, "name": "Алексей Иванов", "phone": "+7(900)123-45-67", "email": "alex@example.com"},
        {"id": 102, "name": "Мария Петрова", "phone": "+7(900)234-56-78", "email": "maria@example.com"},
    ]
    for c in contacts:
        client_db.insert(c)

    tasks = [
        {"id": 201, "title": "Подготовить отчет Q1", "description": "Собрать данные и составить сводный отчёт.", "status": "in_progress", "owner_id": 101},
        {"id": 202, "title": "Обновить сайт", "description": "Добавить новые разделы на главной странице.", "status": "todo", "owner_id": 102},
    ]
    for t in tasks:
        tasks_db.insert(t)

    meetings = [
        {"id": 301, "title": "Встреча с Алексеем Ивановым", "date": "2025-06-15T14:00", "location": "Офис", "notes": "Обсудить новый проект."},
        {"id": 302, "title": "Звонок Марии Петровой", "date": "2025-07-01T10:00", "location": "Телефонный звонок", "notes": "Договорились о дедлайне."},
    ]
    for m in meetings:
        meetings_db.insert(m)


def clear_all_state(client_db, tasks_db, meetings_db):
    """Полностью очистить все базы данных."""
    client_db.clear()
    tasks_db.clear()
    meetings_db.clear()
