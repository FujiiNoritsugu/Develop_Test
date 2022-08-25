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

        # 各生徒の教科毎の順位を算出する
        rank_dic = _make_rank_dic(average_dic)

        # 通知簿の出力を行う
        _output_report_card(student_dic, average_dic, rank_dic)

    except Exception:
        print('エラーが発生しました。')
        print(traceback.format_exc())


def _output_report_card(student_dic, average_dic, rank_dic):
    """通知簿の出力を行う

    Args:
        student_dic (_type_): 生徒/教科と点数のリスト
        average_dic (_type_): 生徒/教科と平均点
        rank_dic (_type_): 生徒/教科と順位
    """
    REPORT_CARD_HEADER = '教科,平均点,順位,成績,判定\n'
    SUBJECT_DIC = {'1': '国語', '2': '数学', '3': '理科', '4': '社会', '5': '英語'}

    for student_no, point_data in student_dic.items():
        average_data = average_dic[student_no]
        rank_data = rank_dic[student_no]
        with open(f"生徒{student_no}.csv", mode="w", encoding="shift_jis") as f:
            # ヘッダの書き込み
            f.write(REPORT_CARD_HEADER)
            # 教科毎のデータの取得・出力
            for index in range(1, 6):
                subject = str(index)
                subject_str = SUBJECT_DIC[subject]
                subject_point = point_data[subject]
                subject_average = average_data[subject]
                subject_rank = rank_data[subject]
                subject_grade = _make_grade(subject_rank)
                subject_judge = _make_judge(subject_grade, subject_point)
                f.write(
                    f'{subject_str},{subject_average},{subject_rank},{subject_grade},{subject_judge}\n')


def _make_judge(grade, points):
    """判定文字列を作成する

    Args:
        rank (_type_): _description_
    """
    result = None
    # 点数に10点より下の点数が一つでもあるか判定
    is_failure = any((data < 10 for data in points))
    # 点数に30点以下の点数が三回以上あるか判定
    is_retest = True if sum((data <= 30 for data in points)) >= 3 else False

    if is_failure or grade == 'E':
        result = '不合格'
    elif is_retest or grade == 'D':
        result = '再テスト'
    elif grade in ('A', 'B', 'C'):
        result = '合格'

    return result


def _make_grade(rank):
    """成績を付ける

    Args:
        rank (_type_): 順位
    """
    # 順位の数値にする
    rank = int(rank)
    result = None
    if rank == 1:
        result = 'A'
    elif rank == 2 or rank == 3:
        result = 'B'
    elif 4 <= rank <= 7:
        result = 'C'
    elif rank == 8 or rank == 9:
        result = 'D'
    elif rank == 10:
        result = 'E'

    return result


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

    # 再度、キーが生徒、値が（キーが教科、値が教科毎の順位のディクショナリ)に変換する
    rank_dic = _convert_rank(rank_dic)

    return rank_dic


def _convert_rank(rank_dic):

    result_dic = {}
    for subject, data_list in rank_dic.items():
        for data in data_list:
            student = data['student']
            rank = data['rank']
            if student not in result_dic:
                result_dic[student] = {}
            result_dic[student][subject] = rank

    return result_dic


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
        rank_dic[subject] = average_list
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
