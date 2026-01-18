このリポジトリは、コーディング問題の作成・回答・テストをまとめるためのテンプレートです。

構成:
- `question/`: 問題文を Markdown で保存
- `anwer/`: 各問題の回答コードを保存
- `tests/`: 回答に対する pytest テストを保存

問題・回答・テストの形式:
- `question/question{n}.md`
- `anwer/question{n}.py`
- `tests/test_question{n}.py`

テスト実行:
```bash
uv run pytest
```
