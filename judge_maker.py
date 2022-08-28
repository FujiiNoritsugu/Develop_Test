def make_judge(grade, points):
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


if __name__ == '__main__':
    make_judge('A', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
