# 問題2: FizzBuzz カスタム

FizzBuzz の拡張版を作成してください。任意の数値と文字列のペアを指定でき、条件に一致した場合にその文字列を出力します。

## 要件
- 1 から `n` までの数値に対して結果をリストで返す
- `rules` は `[(除数, 文字列), ...]` の形式で与えられる
- `rules` のルール数は任意（0個、1個、2個、3個以上など何個でも可）
- 数値が複数の除数で割り切れる場合は、`rules` の順番で文字列を連結する
- どの条件にも一致しない場合は数値を文字列に変換して返す

## 関数シグネチャ
```python
def fizzbuzz_custom(n: int, rules: list[tuple[int, str]]) -> list[str]:
    ...
```

## 例
入力:
```python
n = 15
rules = [(3, "Fizz"), (5, "Buzz")]
```

出力:
```python
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```

## 追加例
入力:
```python
n = 10
rules = [(2, "Even"), (3, "Triple")]
```

出力:
```python
["1", "Even", "Triple", "Even", "5", "EvenTriple", "7", "Even", "Triple", "Even"]
```
