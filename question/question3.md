# 問題3: タイムライン圧縮

同じ文字が連続している文字列を、連続数と文字に圧縮する関数を作成してください。

## 要件
- 入力文字列は ASCII の英字のみとする
- 連続数は正の整数として出力する
- 1回だけ出現する場合も数を付ける
- 出力は `"<連続数><文字>"` の連結とする

## 関数シグネチャ
```python
def compress_runs(text: str) -> str:
    ...
```

## 例
入力:
```python
text = "aaabccccdde"
```

出力:
```python
"3a1b4c2d1e"
```

## 追加例
入力:
```python
text = "ABBBCCDAA"
```

出力:
```python
"1A3B2C1D2A"
```
