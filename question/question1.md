# 問題1: 設定差分

2つの設定辞書 `old` と `new` の差分を求める関数を作成してください。

## 要件
- `old` にのみ存在するキーは `removed` に入れる
- `new` にのみ存在するキーは `added` に入れる
- 両方に存在し、値が異なるキーは `changed` に入れる
- `changed` の値は `{"before": <oldの値>, "after": <newの値>}` とする
- 再帰的な比較は不要（値が辞書でもそのまま比較する）

## 関数シグネチャ
```python
def diff_config(old: dict[str, object], new: dict[str, object]) -> dict[str, object]:
    ...
```

## 期待する戻り値の形式
```python
{
    "added": { ... },
    "removed": { ... },
    "changed": {
        "some_key": {"before": ..., "after": ...},
        ...
    },
}
```

## 例
入力:
```python
old = {"host": "localhost", "port": 5432, "debug": False}
new = {"host": "localhost", "port": 5433, "debug": True, "timeout": 30}
```

出力:
```python
{
    "added": {"timeout": 30},
    "removed": {},
    "changed": {
        "port": {"before": 5432, "after": 5433},
        "debug": {"before": False, "after": True},
    },
}
```
