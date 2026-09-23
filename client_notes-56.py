# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: ClientNotes
def bulk_update_records(self, records: list[dict]) -> None:
    """Массовое обновление выбранных записей."""
    for rec in records:
        if rec["id"] in self.records:
            self.records[rec["id"]] = {**self.records[rec["id"]], **rec}
    self._notify()
