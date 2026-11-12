<!-- GitHub Issue にそのまま貼り付ける本文。タイトル: GET /books/{id} が存在しない ID で 500 を返す -->

## 現象

`GET /books/999` のように存在しない ID を指定すると、`KeyError` で 500 Internal Server Error になる。

```
$ curl -i http://localhost:8000/books/999
HTTP/1.1 500 Internal Server Error
```

## 期待する動作

- 存在しない ID の場合は **404 Not Found** を返す
- レスポンスボディは `{"detail": "Book 999 not found"}` の形式

## 受け入れ条件

- [ ] `GET /books/{id}` が未知の ID に対して 404 を返す
- [ ] 既存のテスト (`tests/test_books.py`) がすべて通る
- [ ] 404 ケースのテストが追加されている
- [ ] 既存の 200 ケースの挙動は変わらない
