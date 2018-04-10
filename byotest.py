def test_between_limits(a, b, c):
    assert a > b and a < c, "{0} is not between limits {1} and {2}".format(a, b, c) 
 
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Dit not expect {0}, but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
