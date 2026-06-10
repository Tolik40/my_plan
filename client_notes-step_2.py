# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ClientNotes
class ValidationError(Exception):
    pass

def validate_contact(name: str, phone: str) -> tuple[bool, str]:
    if not name.strip():
        return False, "Имя клиента не может быть пустым."
    if not phone.strip():
        return False, "Номер телефона обязателен."
    if len(phone) < 10 or not phone.isdigit():
        return False, "Некорректный формат номера телефона."
    return True, ""

def validate_task(description: str, deadline: str) -> tuple[bool, str]:
    if not description.strip():
        return False, "Описание задачи не может быть пустым."
    try:
        from datetime import datetime
        today = datetime.now().date()
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
        if deadline_date < today:
            return False, "Срок выполнения задачи должен быть в будущем или сегодня."
    except ValueError:
        return False, "Некорректный формат даты (ожидалось YYYY-MM-DD)."
    return True, ""

def validate_meeting(title: str, location: str) -> tuple[bool, str]:
    if not title.strip():
        return False, "Название встречи не может быть пустым."
    if not location.strip():
        return False, "Место проведения встречи не может быть пустым."
    return True, ""
