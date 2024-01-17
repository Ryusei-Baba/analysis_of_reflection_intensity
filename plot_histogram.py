#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(file_path, column_number):
    # 新しい図を作成し、横幅を指定
    # plt.figure(figsize=(10, 5))

    # テキストファイルからデータを読み込む
    with open(file_path, 'r') as file:
        # 行ごとにデータを読み込む
        lines = file.readlines()

        # 各行のデータをリストに変換
        data_list = [list(map(float, line.strip().split())) for line in lines]

    # データをNumPy配列に変換
    data = np.array(data_list)

    # 指定された列のデータを取得
    column_data = data[:, column_number]

    # ヒストグラムをプロット（density=Trueで正規化）
    plt.hist(column_data, bins=30, density=False, color='blue', alpha=0.7, label='Histogram')

    # グラフのタイトルと軸ラベルを設定
    # plt.title('Histogram')
    plt.xlabel('Intensities')
    plt.ylabel('Frequency')

    # 凡例を表示
    plt.legend()

    # グラフを表示
    plt.show()

# パスを指定してプロット
plot_histogram('/home/ryusei/analysis_of_reflection_intensity/data/intensities_data_foyer.txt', 0)
