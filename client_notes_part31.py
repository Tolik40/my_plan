# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ClientNotes
def switch_profile(self, profile_id):
        profiles = self._profiles or []
        target = next((p for p in profiles if p.id == profile_id), None)
        if not target:
            raise ValueError(f"Профиль с id={profile_id} не найден")
        current = self.active_profile
        if current and current != target:
            current.is_active = False
            target.is_active = True
            self.active_profile = target
