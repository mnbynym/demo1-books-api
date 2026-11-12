"""インメモリの書籍リポジトリ。"""

BOOKS: dict[int, dict] = {
    1: {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    2: {"id": 2, "title": "Refactoring", "author": "Martin Fowler"},
    3: {"id": 3, "title": "Working Effectively with Legacy Code", "author": "Michael Feathers"},
}


def list_books() -> list[dict]:
    return list(BOOKS.values())


def get_book(book_id: int) -> dict:
    # NOTE: 存在しない ID の扱いが未実装（Issue #1）
    return BOOKS[book_id]
