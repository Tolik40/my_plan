# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ClientNotes
import datetime

def demo():
    print("=== ClientNotes Demo ===")
    today = datetime.date.today()
    now = datetime.datetime.now()

    contacts = [
        {"name": "Алексей", "phone": "+7 (900) 123-45-67", "company": "TechCorp"},
        {"name": "Мария", "phone": "+7 (900) 765-43-21", "company": "DesignStudio"},
        {"name": "Иван", "phone": "+7 (900) 111-22-33", "company": "BuildGroup"},
    ]
    for c in contacts:
        print(f"  Контакт: {c['name']} ({c['company']}) — {c['phone']}")

    meetings = [
        {"date": today, "time": "10:00", "client": "Алексей", "topic": "Обсуждение нового проекта", "notes": "Нужно подготовить ТЗ"},
        {"date": today, "time": "14:30", "client": "Мария", "topic": "Дизайн-обзор", "notes": "Согласовать цветовую схему"},
    ]
    for m in meetings:
        print(f"  Встреча: {m['client']} в {m['time']}, тема: {m['topic']}")

    tasks = [
        {"title": "Подготовить предложение", "priority": "high", "due": today + datetime.timedelta(days=3)},
        {"title": "Отправить договор", "priority": "medium", "due": today + datetime.timedelta(days=7)},
        {"title": "Вызвать мастера", "priority": "low", "due": today + datetime.timedelta(days=14)},
    ]
    for t in tasks:
        print(f"  Задача: [{t['priority'].upper()}] {t['title']} (до {t['due'].day}.{t['due'].month})")

    decisions = [
        {"date": today - datetime.timedelta(days=5), "summary": "Выбран TechCorp как основной подрядчик", "solution": "Предоставили скидку 5% за долгосрочное сотрудничество"},
    ]
    for d in decisions:
        print(f"  Решение: {d['summary']}")

    print(f"\n  Сегодня: {today}")
    print(f"  Время: {now.strftime('%H:%M:%S')}")
    print("\n=== Демо завершено ===")

if __name__ == "__main__":
    demo()
