# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: ClientNotes
class FavoritesManager:
    _favorites = {}

    @staticmethod
    def add_favorite(record_id, title=""):
        FavoritesManager._favorites[record_id] = title

    @staticmethod
    def remove_favorite(record_id):
        FavoritesManager._favorites.pop(record_id, None)

    @staticmethod
    def is_favorite(record_id):
        return record_id in FavoritesManager._favorites

    @staticmethod
    def get_favorites():
        return FavoritesManager._favorites
