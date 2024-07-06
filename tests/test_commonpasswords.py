import commonpasswords
def test_detect():
    assert commonpasswords.detect("password", reason=True) == [-2, ['Contains common words', 'Only 1 type of Character']]
