# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ClientNotes
class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size

    def get_page(self, page):
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def total_pages(self):
        return (len(self.items) + self.page_size - 1) // self.page_size

    def has_next(self, page):
        return page < self.total_pages()

    def has_prev(self, page):
        return page > 1
