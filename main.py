import os
import re
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
パラメータ設定
"""
# グラフタイトル
GRAPH_TITLE = 'Surface Plot'
# 輝度 しきい値
THRESHOLD_VALUE = 0
# カラーバーの表示
IS_SHOW_COLOR_BAR = True
# グラフイメージの保存
IS_SAVE_GRAPH_IMAGE = True
# グラフイメージの保存パス
SAVE_PATH = 'dist/graph_image'


def createGraph(file_name):
    # 画像の取得
    print(file_name)
    image = Image.open(file_name)
    image = image.convert('L')
    width = image.width
    height = image.height

    # 輝度データ取得
    z = []
    for w in range(width):
        arr = []
        for h in range(height):
            value = image.getpixel((w, h))
            if value < THRESHOLD_VALUE:
                value = 0
            arr.append(value)

        z.append(arr)

    # データ生成
    X, Y = np.meshgrid(range(height), range(width))
    Z = np.array(z)

    # グラフ生成
    name = os.path.splitext(os.path.basename(file_name))[0]
    fig = plt.figure(figsize=(9, 6))
    fig.canvas.manager.set_window_title(name)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(GRAPH_TITLE)

    surf = ax.plot_surface(X, Y, Z, cmap='bwr', linewidth=10)
    if IS_SHOW_COLOR_BAR:
        fig.colorbar(surf)
    if IS_SAVE_GRAPH_IMAGE:
        name = os.path.splitext(os.path.basename(file_name))[0]
        plt.savefig("{0}/{1}_graph.png".format(SAVE_PATH, name))

    plt.show()


def checkDirectory():
    if IS_SAVE_GRAPH_IMAGE and not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)


def main():
    # check directory
    checkDirectory()

    # create graph
    path = 'images'
    pattern = re.compile('.+\.(jpg|jpeg|png|gif)')
    for f in os.listdir(path):
        res = pattern.match(f)
        if res:
            createGraph("{0}/{1}".format(path, f))


if __name__ == '__main__':
    main()
