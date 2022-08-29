from judge_maker import make_judge


def test_make_judge_no1():
    """マトリックスNo1
    10点より下の点数がある場合
    """
    result = make_judge('A', [9, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 3


def test_make_judge_no2():
    """マトリックスNo2
    30点以下の点数が3回以上ある場合
    """
    result = make_judge('B', [30, 30, 30, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 2


def test_make_judge_no3_1():
    """マトリックスNo3
    成績がAの場合
    """
    result = make_judge('A', [100, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 1


def test_make_judge_no3_2():
    """マトリックスNo3
    成績がBの場合
    """
    result = make_judge('B', [100, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 1


def test_make_judge_no3_3():
    """マトリックスNo3
    成績がCの場合
    """
    result = make_judge('C', [100, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 1


def test_make_judge_no4():
    """マトリックスNo4
    成績がDの場合
    """
    result = make_judge('D', [100, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 2


def test_make_judge_no5():
    """マトリックスNo5
    成績がEの場合
    """
    result = make_judge('E', [100, 100, 100, 100, 100,
                        100, 100, 100, 100, 100])
    assert result == 3


def test_make_judge_e1():
    """異常系１
    gradeがA～Eの文字以外であった場合
    """
    try:
        make_judge('F', [100, 100, 100, 100, 100,
                         100, 100, 100, 100, 100])
        assert False
    except Exception as e:
        assert e.args[0] == 'gradeがA～Eの文字でありません'


def test_make_judge_e2():
    """異常系２
    pointsが整数値0～100の10個のリストでなかった場合
    """
    try:
        make_judge('A', ['X', 'Y', 'Z'])
        assert False
    except Exception as e:
        assert e.args[0] == 'pointsが整数値0～100のリストでありません'
