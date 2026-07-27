# === Stage 32: Добавь журнал действий пользователя ===
# Project: ClientNotes
class ActionLog:
    def __init__(self):
        self._entries = []

    @property
    def entries(self):
        return list(self._entries)

    def add(self, user, action_type, detail=""):
        entry = {
            "user": user,
            "type": action_type,
            "detail": detail,
            "timestamp": datetime.now().isoformat(),
        }
        self._entries.append(entry)
