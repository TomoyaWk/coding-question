このリポジトリは、コーディング問題の作成・回答・テストをまとめるためのテンプレートです。

構成:
- `question/`: 問題文を Markdown で保存
- `anwer/`: 各問題の回答コードを保存
- `tests/`: 回答に対する pytest テストを保存

最初の問題:
- `question/question1.md`
- `anwer/question1.py`
- `tests/test_question1.py`

テスト実行:
```bash
uv run pytest
```
