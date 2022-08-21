import random
from numpy.random import normal, randint
import pandas as pd

def main():
    # points = randint(0, 100, 500)
    # print(points)
    for file_suffix in (16, 23, 3, 25, 12, 6, 19, 15, 18, 28, 5, 8, 20):
        # 平均値50 標準偏差18の正規分布を500データ作成する
        points = normal(50, 18, 500)
        # 100より大きい点数は100に0より小さい点数は0にする
        points = [data if data > 0 else 0 for data in [int(data) if data < 100 else 100 for data in points]]
        file_name = f'input_{file_suffix}.csv'
        with open(file_name, mode='w') as f:
            for name_index, name in enumerate(range(1, 11)):
                for subject_index, subject in enumerate(range(1, 6)):
                    for count_index, count in enumerate(range(1, 11)):
                        point = points[50*name_index + 10*subject_index + count_index]
                        f.write(f'{name},{subject},{point}\n')
        # 一旦Pandasに読み込む
        df = pd.read_csv(file_name, header=None)
        # シャッフルして再度CSVに出力する
        df.sample(frac=1).to_csv(file_name, header=False, index=False)


if __name__ == '__main__':
    main()
