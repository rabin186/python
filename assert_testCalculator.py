from calculator import square

def main():
    test_square()


def test_square():
    # if square(2) != 4:
    #     print("2 squared wasn't 4.")
    # if square(3) != 9:
    #     print("3 squared wasn't 9.")
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print("2 squared wasn't 4.")
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print("3 squared wasn't 9.")
    # try:
    #     assert square(-2) == 4
    # except AssertionError:
    #     print("-2 squared wasn't 4.")
    # try:
    #     assert square(-3) == 9
    # except AssertionError:
    #     print("-3 squared wasn't 9.")
    # try:
    #     assert square(0) == 0
    # except AssertionError:
    #     print("0 squared wasn't 0.")
    # try:
    #     assert square(1) == 1
    # except AssertionError:
    #     print("1 squared wasn't 1.")
    assert square(2) == 4
    assert square(-2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0




if __name__ == "__main__":
    main()
