# demo1 — 同じ Issue を CLI 型とクラウド型に投げる

研修1章「ツールの3分類」のデモ。受け入れ条件が明確な Issue を
**クラウド型**（GitHub 上の Copilot / Codex / Claude cloud agent）と
**CLI 型**（手元の Claude Code）に同時に渡し、到達点は同じでも
介入ポイントとレビュー単位が違うことを見せる。

## セットアップ

```bash
uv sync
uv run pytest -q          # 2 passed
uv run uvicorn app.main:app --reload
curl -i localhost:8000/books/999   # 500 になることを確認
```

## 事前準備（研修前日まで）

1. このディレクトリを GitHub リポジトリとして push する
2. `ISSUE.md` の内容で Issue #1 を作成する
3. リポジトリで cloud agent（Copilot coding agent / Agent HQ）を有効化し、使うエージェントを選んでおく
4. 保険として、cloud agent に一度解かせた PR を `backup/cloud-agent-result` ブランチに残しておく（ネットワーク不調時に見せる）
5. `git reset --hard` で main を元の壊れた状態に戻しておく

## 本番手順（10 分）

| 時間 | やること | 見せるポイント |
|---|---|---|
| 1分 | Issue #1 を画面に出す | 受け入れ条件が明確＝クラウド型向きのタスク |
| 1分 | Issue を cloud agent にアサイン | 以後はバックグラウンド。「閉じても進む」 |
| 5分 | ターミナルで `claude` を起動し、Issue 本文を貼って依頼 | 探索→修正→`pytest`→自己修正。承認プロンプトが出た所で「ここが自律度の調整点」と説明 |
| 2分 | GitHub に戻り Draft PR を確認 | 差分・テスト結果・PR 説明を手元の結果と並べる |
| 1分 | まとめ | 到達点は同じ。介入ポイント（ターン vs PR）が違う |

### Claude Code に渡すプロンプト例

```
Issue #1 を解決して。内容は以下。
（ISSUE.md の本文を貼る）
修正後に uv run pytest を実行して全部通ることを確認して。
```

## 想定される修正

`app/repository.py` で `KeyError` を捕捉して `None` を返すか専用例外を投げ、
`app/main.py` で `HTTPException(status_code=404, detail=f"Book {book_id} not found")` に変換。
`tests/test_books.py` に `test_get_missing_book_returns_404` が追加される。
