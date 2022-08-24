'''
通知簿作成プログラム
'''
import sys
import traceback


def main(input_csv):
    try:
        # 入力ファイルを読み込んでリストを作成する
        with open(input_csv) as f:
            # 末尾の改行を削除しておく
            lines = [s.strip() for s in f.readlines()]
        # 入力ファイルを読み込んでキー：生徒番号、値：(キー：教科　値：点数のリスト)にして返却する
        student_dic = _make_student_dic(lines)
        # 各生徒の教科毎の平均点を算出する
        average_dic = _make_average_dic(student_dic)
        print(average_dic)
    except Exception:
        print('エラーが発生しました。')
        print(traceback.format_exc())


def _make_average_dic(student_dic):
    """各生徒の教科毎の平均点を算出する

    Returns:
        _type_: _description_
    """
    average_dic = {}
    for student, subject_dic in student_dic.items():
        # キーがなければ初期化しておく
        if student not in average_dic:
            average_dic[student] = {}
        for subject, point_list in subject_dic.items():
            average_dic[student][subject] = sum(
                point_list) / len(point_list)
    return average_dic


def _make_student_dic(lines):
    """入力ファイルを読み込んでキー：生徒番号、値：(キー：教科　値：点数のリスト)にして返却する

    Args:
        lines (_type_): _description_

    Returns:
        _type_: _description_
    """
    student_dic = {}
    for line in lines:
        temp_list = line.split(',')
        student = temp_list[0]
        subject = temp_list[1]
        point = temp_list[2]
        # 生徒番号をキーにするディクショナリが存在しなければ生徒ディクショナリとして初期化しておく
        if student not in student_dic:
            student_dic[student] = {}
        subject_dic = student_dic[student]
        # 教科をキーにするディクショナリが存在しなければ教科リストとして初期化しておく
        if subject not in subject_dic:
            subject_dic[subject] = []
        point_list = subject_dic[subject]
        # 点数を教科リストに追加しておく
        point_list.append(int(point))

    return student_dic


if __name__ == '__main__':
    # プログラムの最初の引数を入力CSV名とする
    main(sys.argv[1])
