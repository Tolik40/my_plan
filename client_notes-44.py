# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ClientNotes
import json, shutil, os, datetime

def backup_notes(data_file, backup_dir=None):
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(os.path.abspath(data_file)), 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'notes_backup_{timestamp}.json')
    shutil.copy2(data_file, backup_path)
    print(f'Backup saved to {backup_path}')
    return backup_path
