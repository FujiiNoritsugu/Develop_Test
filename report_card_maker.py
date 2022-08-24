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
        # print(average_dic)
        # 各生徒の教科毎の順位を算出する
        rank_dic = _make_rank_dic(average_dic)
        print(rank_dic)

    except Exception:
        print('エラーが発生しました。')
        print(traceback.format_exc())


def _make_rank_dic(average_dic):
    """各生徒の教科毎の順位を算出する

    Args:
        average_dic (_type_): _description_
    """
    # キーを教科、値をキーが生徒、値が平均値のディクショナリのリストに変換する
    rank_dic = {}
    for student, subject_dic in average_dic.items():
        for subject, average in subject_dic.items():
            if subject not in rank_dic:
                rank_dic[subject] = []
            rank_dic[subject].append({'student': student, 'average': average})

    # 教科毎に平均値で並べ替える
    rank_dic = _sort_rank_dic(rank_dic)

    return rank_dic


def _sort_rank_dic(rank_dic):
    """教科毎に平均値で並べ替える

    Args:
        rank_dic (_type_): _description_
    """
    for subject, average_list in rank_dic.items():
        average_list = sorted(
            average_list,
            key=lambda x: x['average'],
            reverse=True)

        # average_listに「rank」項目を追加する
        for index, average_dic in enumerate(average_list):
            average_dic['rank'] = index + 1

    return rank_dic


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