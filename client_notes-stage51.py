# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: ClientNotes
class DataChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, entity_type, entity_id, action, details=None):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action": action,
            "details": details or {}
        }
        self.entries.append(entry)
        return entry

    def get_history(self, entity_type=None, entity_id=None):
        if entity_type and entity_id:
            return [e for e in self.entries if e["entity_type"] == entity_type and e["entity_id"] == entity_id]
        if entity_type:
            return [e for e in self.entries if e["entity_type"] == entity_type]
        return list(self.entries)
