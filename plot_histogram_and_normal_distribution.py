#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_histogram_and_normal_distribution(file_path, column_number):
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
    plt.hist(column_data, bins=30, density=True, color='blue', alpha=0.7, label='Histogram')

    # 正規分布のパラメータを計算
    mu, std = norm.fit(column_data)

    # 正規分布をプロット
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, color='green', label='Normal Distribution')

    # グラフのタイトルと軸ラベルを設定
    # plt.title('Histogram and Normal Distribution')
    plt.xlabel('Intensities')
    plt.ylabel('Frequency')

    # 凡例を表示
    plt.legend()

    # グラフを表示
    plt.show()

# パスを指定してプロット
plot_histogram_and_normal_distribution('/home/ryusei/analysis_of_reflection_intensity/data/intensities_data_wall.txt', 0)
