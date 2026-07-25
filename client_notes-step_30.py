# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ClientNotes
class ProfileStore:
    def __init__(self):
        self.profiles = {}
        self.current_profile_name = None

    def add(self, name, password=None):
        if not name or name in self.profiles:
            return False
        self.profiles[name] = {"password": password, "history": []}
        self.current_profile_name = name
        return True

    def switch(self, name):
        if name and name in self.profiles:
            self.current_profile_name = name
            return True
        return False

    def login(self, name, password=None):
        profile = self.profiles.get(name)
        if not profile or (password is not None and profile["password"] != password):
            return False
        self.current_profile_name = name
        return True

    @property
    def current(self):
        if self.current_profile_name:
            return self.profiles[self.current_profile_name]
        return {"history": []}
