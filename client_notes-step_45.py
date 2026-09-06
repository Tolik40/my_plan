# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ClientNotes
def restore_from_backup(backup_path):
    """Restore ClientNotes state from a JSON backup file."""
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Резервная копия успешно восстановлена из {backup_path}")
        return True
    except FileNotFoundError:
        print(f"Файл резервной копии не найден: {backup_path}")
        return False
    except json.JSONDecodeError:
        print("Ошибка: файл резервной копии содержит некорректный JSON")
        return False
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
