# pytemplate1

## 概要
Pythonの独自ライブラリパッケージです。コマンドラインツールとしても、他のPythonプログラムからライブラリとしても利用できます。

このプロジェクトは、Gemini CLIと一緒に作りました。

``GEMINI.md``だけをコピーして、Gemini CLI に簡単な指示をするだけで、似たようなプロジェクトを作成することもできます。(後述)

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

### 自動テストの実行

プロジェクトのルートディレクトリで以下のコマンドを実行すると、すべてのテストが実行されます。

```bash
source .venv/bin/activate
pytest
```

### コードの整形とリンティング

`ruff` を使用してコードの整形とリンティングを行います。以下のコマンドを実行してください。

```bash
source .venv/bin/activate
ruff format .
ruff check .
```


## プロジェクト構造

プロジェクトの主要なディレクトリとファイルは以下の通りです。

```
. # プロジェクトルート
├── pytemplate1/          # Pythonパッケージのソースコード
│   ├── __init__.py     # パッケージの初期化ファイル
│   ├── __main__.py     # コマンドラインエントリポイント
│   ├── calculator.py   # 四則演算ロジック
│   └── logger.py       # ロギング設定
├── samples/              # サンプルプログラム
│   ├── sample.py         # ライブラリ利用のサンプル
│   └── interactive_sample.py # インタラクティブモードのサンプル
├── tests/                # テストコード
│   ├── test_calculator.py # Calculatorのテスト
│   ├── test_cli.py        # CLIコマンドのテスト
│   └── test_sample.py     # サンプルプログラムのテスト
├── .gitignore            # Gitの無視リスト
├── pyproject.toml        # プロジェクト設定ファイル (依存関係、ビルド、ツール設定)
├── README.md             # このドキュメント
└── LICENSE               # プロジェクトのライセンス情報
```

## GEMINI.mdについて

`GEMINI.md` は、このプロジェクトの設計図であり、開発規約、使用ツール、テスト方法などを定義しています。このファイルをテンプレートとして利用することで、同様のPythonプロジェクトを効率的にセットアップできます。

※ 全く同じにはなりません。対話しながら修正が必要です。


新しいプロジェクトを作成する際は、Gemini CLIに以下の指示をしてください。

```
GEMINI.md を参考にして、新しいPythonプロジェクトをセットアップしてください。プロジェクト名は <新しいプロジェクト名>、作者は <あなたの名前> <<あなたのメールアドレス>> です。
```

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

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。
