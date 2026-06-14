# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ClientNotes
def delete_record(record_id: int) -> bool:
    if record_id not in _records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    deleted_type = None
    for rec_type, records in _records.items():
        if record_id in records:
            del records[record_id]
            deleted_type = rec_type
            break
            
    if not deleted_type:
        print("Ошибка: удаление не выполнено.")
        return False
        
    history_entry = {
        "action": f"delete_{deleted_type}",
        "id": record_id,
        "timestamp": datetime.now().isoformat(),
        "details": f"Удалена запись типа '{deleted_type}'."
    }
    _history.append(history_entry)
    print(f"Запись {record_id} успешно удалена.")
    return True
