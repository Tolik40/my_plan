# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ClientNotes
TEMPLATE_REGISTRY = {
    "meeting": {"title": "{name} — встреча", "body": "Дата: {date}\nОписание: \nРезультат:\nСледующие шаги:"},
    "task": {"title": "Задача: {description}", "body": "Клиент: {client_name}\nПриоритет: {priority}\nОписание: \nДедлайн: {deadline}"},
    "decision": {"title": "Решение по {topic}", "body": "Тема: {topic}\nДата решения:\nОбоснование:\nИсполнитель:"},
}

def apply_template(template_name, **kwargs):
    if template_name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Неизвестный шаблон: {template_name}. Доступные: {list(TEMPLATE_REGISTRY)}")
    t = TEMPLATE_REGISTRY[template_name]
    return {"title": t["title"].format(**kwargs), "body": t["body"].format(**kwargs)}

def add_note_from_template(template_name, **fields):
    note_data = apply_template(template_name, **fields)
    note_id = str(uuid.uuid4())[:8]
    now_iso = datetime.now().isoformat() + "+03:00"
    return {
        "id": note_id,
        "created_at": now_iso,
        "updated_at": now_iso,
        "type": template_name,
        **note_data
    }
