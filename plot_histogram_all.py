#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def plot_comparing_histograms(file_paths, column_number):
    # 新しい図を作成し、横幅を指定
    plt.figure(figsize=(15, 7))

    # 色のリスト
    colors = ['red', 'blue', 'green']
    
    # 凡例のラベル
    legend_labels = ['The reflection intensity of the wall', 'The reflection intensity of retroreflective tape', 'The reflection intensity of foyer']

    # ファイルごとにデータを読み込み、プロット
    for i, file_path in enumerate(file_paths):
        with open(file_path, 'r') as file:
            # 行ごとにデータを読み込む
            lines = file.readlines()

            # 各行のデータをリストに変換
            data_list = [list(map(float, line.strip().split())) for line in lines]

        # データをNumPy配列に変換
        data = np.array(data_list)

        # 指定された列のデータを取得
        column_data = data[:, column_number]

        # ヒストグラムをプロット
        plt.hist(column_data, bins=30, alpha=0.7, color=colors[i], label=f'Histogram - {file_path.split("/")[-1].split(".")[0]}', align='mid')  # alignの値を指定

    # グラフのタイトルと軸ラベルを設定
    plt.xlabel('Intensities')
    plt.ylabel('Frequency')

    # 凡例を表示（labelsにラベルを渡す）
    plt.legend(labels=legend_labels)

    # グラフを表示
    plt.show()

# パスを指定してプロット
file_paths = [
    '/home/ryusei/analysis_of_reflection_intensity/data/intensities_data_wall.txt',
    '/home/ryusei/analysis_of_reflection_intensity/data/intensities_data_tape.txt',
    '/home/ryusei/analysis_of_reflection_intensity/data/intensities_data_foyer.txt'
]
plot_comparing_histograms(file_paths, 0)
