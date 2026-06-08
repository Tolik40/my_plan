# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ClientNotes
import json
from datetime import datetime, timedelta

# --- Базовая структура данных (демонстрационные данные) ---
DEMO_DATA = {
    "contacts": [
        {"id": 1, "name": "Иван Петров", "phone": "+79001234567", "email": "ivan@example.com"},
        {"id": 2, "name": "Анна Сидорова", "phone": "+79007654321", "email": "anna@example.com"}
    ],
    "meetings": [
        {"id": 1, "contact_id": 1, "date": datetime.now().strftime("%Y-%m-%d"), "topic": "Обсуждение проекта X", "notes": "Нужно подготовить смету."}
    ],
    "tasks": [
        {"id": 1, "text": "Позвонить Ивану Петрову", "status": "pending"},
        {"id": 2, "text": "Отправить отчет по проекту Y", "status": "done"}
    ],
    "history": []
}

# --- Точка входа и запуск демонстрации ---
def main():
    # Инициализация данных (в реальном проекте здесь бы загружался файл)
    data = DEMO_DATA
    
    # Вывод текущего состояния для проверки
    print("=== Журнал ClientNotes ===")
    print(f"Контактов: {len(data['contacts'])}")
    print(f"Встреч сегодня: {len([m for m in data['meetings'] if m['date'] == datetime.now().strftime('%Y-%m-%d')])}")
    
    # Пример добавления записи в историю решений
    decision = {
        "timestamp": datetime.now(),
        "summary": "Решено: начать разработку модуля отчетности",
        "details": "Обсуждено с командой, приоритет высокий."
    }
    data["history"].append(decision)
    
    # Сохранение в файл (демонстрация работы с persistency)
    with open("client_notes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные сохранены в client_notes.json")

if __name__ == "__main__":
    main()
