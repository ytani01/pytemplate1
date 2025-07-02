# プロジェクト

プロジェクト名: pytemplate1

## 概要
Python 独自ライブラリパッケージのテンプレート。
外部プログラムから、importして利用可能。
コマンドラインとしても実行可能。

## プロジェクト初期化方法

``` shell
uv init --lib
```

## 仮想環境

- venv
- プロジェクト名をそのままコマンド名として使用可能

## 参考にするコード

@https://github.com/ytani01/Templates/tree/master/pkg2

- ``click``を使ってコマンドラインを解析
- デバッグオプションとヘルプオプションを追加
- ``CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])``を使って、'-h'もヘルプオプションとして認識
- '-d'もデバッグオプションとする


## pyproject.tomlについて

- なるべく丁寧に記述
- 実行環境と開発を区別
- author
  - name: Author Name
  - email: email@author.jp 
- LINT, 整形、テストを自動化

## README.mdについて

- コマンドラインでの利用方法
- ライブラリとしての利用法
- 開発方法の説明
  - 自動テストの方法なども追記

## gitについて

- デフォルトのブランチ名: master
- .gitignoreには、Emacs用の記述も追加

## テストについて

- ライブラリの動作を自動テスト
- コマンドラインの動作を自動テスト

## サンプルプログラムに土江

- ``samples``ディレクトリを作成し、ライブラリとしてつかうサンプルプログラムを作成
- サンプルプログラムも自動テスト

## ライセンスについて

- MITライセンス
- pyproject.tomlに追記
- README.mdに追記
