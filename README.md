# Image Brightness Acquisition
画像の輝度を取得して3Dグラフを生成するプログラムです。

## Set Up
1. プログラムをローカルにクローンもしくはダウンロード
2. Pythonの実行環境を準備

## How to Use
1. `images`フォルダに輝度を取得したい画像を配置

2. Terminalやコマンドプロンプトを開いて、プログラムがあるディレクトリまで移動
```
$ cd .../image-brightness-acquisition
```

3. `main.py`ファイルを実行する
```
$ python main.py
```

4. グラフが表示されます。グラフイメージの保存を有効にしている場合は`dest/graph_image/`直下にグラフイメージが保存されます。

<br>

※ グラフは画像の左上が原点となるように描画されます。<br>
※ プログラムを実行すると`images`フォルダに配置した全ての画像のグラフが順番に生成されます。

### 最遊的なディレクトリ構成

プログラムを実行すると以下のようなディレクトリ構成になります。

```
root/
 ├─ dist/（自動生成）
 ├   └─ graph_image/ （自動生成）
 ├       └─ sample_twilight_graph.png （生成したグラフの画像）
 ├─ images/
 ├   └─ sample_twilight.jpg
 ├─ main.py
 ├─ README.md
 └─ .gitignore
```


## Parameter Settings

`main.py`上部にあるパラメータを変更することで、プログラムをカスタマイズすることができます。

|#|パラメータ|説明|
|:--:|:--:|:--|
|1|`GRAPH_TITLE`|グラフのタイトルを設定します。|
|2|`THRESHOLD_VALUE`|グラフに表示する輝度のしきい値を設定します。<br>設定した値より輝度が小さい場合は0として表示します。|
|3|`IS_SHOW_COLOR_BAR`|グラフにカラーバーを表示するかを設定します。<br>`True` -> 表示する　`False` -> 表示しない|
|4|`IS_SAVE_GRAPH_IMAGE`|グラフイメージを保存するかを設定します。<br>`True` -> 保存する　`False` -> 保存しない|
|5|`SAVE_PATH`|グラフイメージを保存するパスを指定します。<br>基本的に変更する必要はありません。|

## Sample

`images`フォルダにあるサンプル画像です。プログラムを実行すると、下のグラフが生成されます。

![sample_twilight](https://user-images.githubusercontent.com/21216852/134778940-be50de78-8e20-45c2-9a43-3c8e9199f073.jpg)

![sample_twilight_graph](https://user-images.githubusercontent.com/21216852/134778880-017ed4bf-c9df-444c-b032-1970a7cbc262.png)
