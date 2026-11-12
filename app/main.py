from fastapi import FastAPI

from app import repository

app = FastAPI(title="Books API (demo1)")


@app.get("/books")
def list_books() -> list[dict]:
    return repository.list_books()


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict:
    return repository.get_book(book_id)
