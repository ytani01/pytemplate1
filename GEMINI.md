# プロジェクト概要

- プロジェクト名: pytemplate1
- 実行環境と開発環境を区別する。
- Pythonの独自ライブラリパッケージ。
- コマンドとしても使える。
- 機能: シンプルな四則演算
- samplesディレクトリに、ライブラリをつかったサンプルプログラムも作成

- プロジェクト初期化方法: 'uv init --lib'
- pyproject.tomlは丁寧書く
- author
  - name: Author Name
  - email: email@author.jp
- LICENCE: MIT

- コマンドライン解析: clickを使う

# README.md

以下の内容を含め、読みやすいドキュメントを作成

- 言語: 日本語
- インストール方法
- 開発方法
- コマンドとしての利用方法
- ライブラリとしての利用方法

# clickについて

- ``CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])``とする
- ヘルプオプション: '-h', '--help'
- デバッグオプション: '-d'と'--debug'

# デバッグログについて

- loggingを使う
- logger.pyというファイルをつくる

# 使用方法

## コマンドとして

'python -m'を書かなくていいようにする。

``` shell
source .venv/bin/activate

# 例
pytemplate1 add 1 2
pytemplate1 sub 5 2
pytemplate1 mul 5 2
pytemplate1 div 5 2
pytemplate1 interactive
```

## ライブラリとして

``` python
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

# サンプルプログラムについて

- samplesディレクトリに、ライブラリとして利用するシンプルなサンプルプログラムを作成
- サンプルプログラムも自動テストする

# 開発環境について

- 'pip'を直接使わず、'uv pip'を
- venvを使う
- 静的解析自動化
- コード整形自動化
- テスト自動化
- エディタ: Emacs
- gitリポジトリを作成

# gitリポジトリについて

- .gitignoreには、Emacs用の記述も追加
