````markdown
# 問題6: 重複削除（順序保持）

リストから重複する要素を削除し、最初に出現した順序を保ったまま返す関数を作成してください。

## 要件
- 各要素は最初に出現した位置のみ残す
- 元のリストの出現順序を維持する
- 空のリストを渡された場合は空のリストを返す
- 要素の型は整数または文字列とする

## 関数シグネチャ
```python
def unique_ordered(items: list[int | str]) -> list[int | str]:
    ...
```

## 例
入力:
```python
items = [1, 2, 3, 2, 1, 4, 3, 5]
```

出力:
```python
[1, 2, 3, 4, 5]
```

## 追加例

入力:
```python
items = ["apple", "banana", "apple", "cherry", "banana"]
```

出力:
```python
["apple", "banana", "cherry"]
```

入力:
```python
items = [1, 1, 1, 1]
```

出力:
```python
[1]
```

入力:
```python
items = []
```

出力:
```python
[]
```
````
