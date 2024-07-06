def test_detect():
    assert commonpasswords.detect("password", reason=True) == [8, ['test', 'Only 1 type of Character']]
