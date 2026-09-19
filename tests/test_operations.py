from src.math_operations import add,multiply

def test_ad() :
    assert add(2,3)==5
    assert add(5,2)==7

def mult_ad() :
    assert multiply(2,3)==6
    assert multiply(5,2)==10
    assert multiply(2,9020223)==18040446



