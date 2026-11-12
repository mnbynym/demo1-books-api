from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_books_returns_all():
    res = client.get("/books")
    assert res.status_code == 200
    assert [b["id"] for b in res.json()] == [1, 2, 3]


def test_get_existing_book():
    res = client.get("/books/2")
    assert res.status_code == 200
    assert res.json()["title"] == "Refactoring"
