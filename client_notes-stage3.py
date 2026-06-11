# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ClientNotes
class ClientNotes:
    def __init__(self):
        self.records = []
    
    def add_contact(self, name, phone):
        record = {"type": "contact", "data": {"name": name, "phone": phone}, "timestamp": time.time()}
        self.records.append(record)
        return record
    
    def add_meeting(self, client_name, date, topic):
        record = {"type": "meeting", "data": {"client": client_name, "date": date, "topic": topic}, "timestamp": time.time()}
        self.records.append(record)
        return record
    
    def add_task(self, description, deadline=None):
        record = {"type": "task", "data": {"description": description, "deadline": deadline or None}, "timestamp": time.time()}
        self.records.append(record)
        return record
