# KakikomiPlus
KakikomiPlusは元の絵を極力保ったままAIによって描きこみを生成するソフトです。<br>
![1](https://github.com/tori29umai0123/KakikomiPlus/assets/72191117/0ef66472-2d35-4815-9c12-46e63d4ea41e)

# Install
①以下のColabのリンクをクリックしてください<br>
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tori29umai0123/KakikomiPlus/blob/main/KakikomiPuls.ipynb)

②Colabのメニューから、『ランタイム』→『ランタイムのタイプを変更』→以下のように設定<br>
![2](https://github.com/tori29umai0123/KakikomiPlus/assets/72191117/4730137b-23ab-4c6c-aa4d-1d9fab92e1a1)<br>

②Colabのメニューから、『すべてのセルを実行』（5分位かかります）<br>
![3](https://github.com/tori29umai0123/KakikomiPlus/assets/72191117/79d39d84-9f24-4914-a29f-d18a3d16c74a)<br>

④一番下のセルのpublic URLをクリック

# Local Install
Python3.10.Xがインストールされている環境前提です。（Python 3.10.8で起動確認済み）<br>
①適当なディレクトリでリポジトリをgit clone<br>
```
cd C:/
git clone https://github.com/tori29umai0123/KakikomiPlus.git<br>
```
②install.ps1を右クリック→PowerShellで実行（5分位かかります）<br>
③KakikomiPlus_run.batをダブルクリックすると自動でブラウザが立ち上がる。<br>

# Local Upadate
ソフトの更新はKakikomiPlus_update.batをダブルクリックする。<br>
更新の有無を聞かれたら『y』と入力。（5分位かかります）<br>
モデルの更新はKakikomiPlus_update_model.batをダブルクリックする。<br>
モデルのアップデートを聞かれたら『y』と入力。（5分位かかります）。<br>

# Local Uninstall
フォルダごと削除してください

# Usage
PreImage：元画像を設定<br>
max_size：画像の長辺の最大サイズを入力（大きければ大きいほどPCスペックが必要です）<br>
strength:AIの影響度<br>
prompt：画像の内容のタグ<br>
PromptGenerate：タグの自動分析<br>
（Inpaintタブの場合）<br>
MaskImage：マスク画像を設定<br>
MaskGenerate：マスクの自動生成<br>
ImageGenerate：画像生成ボタン
