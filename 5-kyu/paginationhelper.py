class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if self.items_per_page <= 0 or len(self.collection) == 0:
            return 0

        return (len(self.collection) + self.items_per_page - 1) // self.items_per_page

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1

        total = len(self.collection)
        start = page_index * self.items_per_page
        end = min(start + self.items_per_page, total)
        return end - start

    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1

        return item_index // self.items_per_page
