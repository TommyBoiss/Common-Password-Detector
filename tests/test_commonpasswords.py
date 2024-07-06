import commonpasswords
def test_detect():
    assert commonpasswords.detect("password", reason=True) == [-1, ['Only 1 type of Character']]
    assert commonpasswords.detect("1923", reason=True) == [-3, ['Password is lower than 8 characters', 'Only 1 type of Character', 'Possibily contains a date']]
    assert commonpasswords.detect("1") == -2
    assert commonpasswords.detect("qwerty") == [-3, ['Contains common combination', 'Password is lower than 8 characters', 'Only 1 type of Character']]
    
