# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ClientNotes
class TagManager:
    def __init__(self, db):
        self.db = db
        self.TAGS_TABLE = "tags"
        self.ITEM_TAGS_TABLE = f"{db.table_prefix}item_tags" if hasattr(db, 'table_prefix') else "item_tags"

    def add_tag(self, name):
        with self.db.cursor() as cursor:
            cursor.execute(f"SELECT id FROM {self.TAGS_TABLE} WHERE name=%s", (name,))
            row = cursor.fetchone()
            if row:
                return row[0]
            cursor.execute(f"INSERT INTO {self.TAGS_TABLE} (name) VALUES (%s)", (name,))
            self.db.commit()
            return cursor.lastrowid

    def remove_tag(self, tag_id):
        with self.db.cursor() as cursor:
            cursor.execute(f"DELETE FROM {self.ITEM_TAGS_TABLE} WHERE tag_id=%s", (tag_id,))
            if cursor.rowcount == 0:
                cursor.execute(f"DELETE FROM {self.TAGS_TABLE} WHERE id=%s", (tag_id,))
            self.db.commit()

    def add_item_tag(self, item_id, tag_id):
        with self.db.cursor() as cursor:
            try:
                cursor.execute(
                    f"INSERT INTO {self.ITEM_TAGS_TABLE} (item_id, tag_id) VALUES (%s, %s)",
                    (item_id, tag_id)
                )
                return True
            except IntegrityError:
                pass
        return False

    def get_item_tags(self, item_id):
        with self.db.cursor() as cursor:
            cursor.execute(f"SELECT t.name FROM {self.ITEM_TAGS_TABLE} it JOIN {self.TAGS_TABLE} t ON it.tag_id=t.id WHERE it.item_id=%s", (item_id,))
            return [row[0] for row in cursor.fetchall()]

    def remove_item_tag(self, item_id, tag_name):
        with self.db.cursor() as cursor:
            cursor.execute(f"SELECT id FROM {self.TAGS_TABLE} WHERE name=%s", (tag_name,))
            tag_row = cursor.fetchone()
            if not tag_row:
                return False
            tag_id = tag_row[0]
            cursor.execute(f"DELETE FROM {self.ITEM_TAGS_TABLE} WHERE item_id=%s AND tag_id=%s", (item_id, tag_id))
            self.db.commit()
            return True
