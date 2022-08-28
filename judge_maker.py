def make_judge(grade, points):
    """判定文字列を作成する

    Args:
        rank (_type_): _description_
    """
    # gradeがA～Eの文字以外であった場合、例外を発生させる
    if grade not in ('A', 'B', 'C', 'D', 'E'):
        raise Exception('gradeがA～Eの文字でありません')
    # pointsが0～100の数値の10個のリストでなかった場合、例外を発生させる
    if not (isinstance(points, list) and len(list) == 10 and all(
            [isinstance(a, int) and 0 <= a <= 100 for a in points])):
        raise Exception('pointsが整数値0～100のリストでありません')
    result = None
    # 点数に10点より下の点数が一つでもあるか判定
    is_failure = any((data < 10 for data in points))
    # 点数に30点以下の点数が三回以上あるか判定
    is_retest = True if sum((data <= 30 for data in points)) >= 3 else False

    if is_failure or grade == 'E':
        result = 3
    elif is_retest or grade == 'D':
        result = 2
    elif grade in ('A', 'B', 'C'):
        result = 1

    return result
