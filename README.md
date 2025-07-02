# pytemplate1

## 概要
Pythonの独自ライブラリパッケージです。コマンドラインツールとしても、他のPythonプログラムからライブラリとしても利用できます。

## インストール方法

```bash
pip install pytemplate1
```

## 開発方法

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/your_username/pytemplate1.git
   cd pytemplate1
   ```
2. 仮想環境を作成し、アクティベートします。
   ```bash
   uv venv
   source .venv/bin/activate
   ```
3. 依存関係をインストールします。
   ```bash
   uv pip install -e .
   ```
4. 開発を開始します。

## コマンドとしての利用方法

仮想環境をアクティベートした後、以下のコマンドで利用できます。

```bash
source .venv/bin/activate

# 例
python -m pytemplate1 add 1 2
python -m pytemplate1 sub 5 2
python -m pytemplate1 mul 5 2
python -m pytemplate1 div 5 2
```

## ライブラリとしての利用方法

```python
from pytemplate1 import Calculator

calc = Calculator()

# 足し算
result = calc.add(1, 2)
print(result)

# 引き算
result = calc.sub(3, 1)
print(result)

# 掛け算
result = calc.mul(2, 3)
print(result)

# 割り算
result = calc.div(6, 2)
print(result)
```
