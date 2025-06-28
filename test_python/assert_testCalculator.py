import pytest
from calculator import square

def main():
    test_square()


def test_square():

##Here, We are mannualy using if statement to check the result.
    # if square(2) != 4:
    #     print("2 squared wasn't 4.")
    # if square(3) != 9:
    #     print("3 squared wasn't 9.")

##Here we are using try and expect and assert() (i.e a function used for checking a function in python) 
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


##Here we are only using assert function and then we use pytest a third party module to check correctness of a function
    assert square(2) == 4
    assert square(-2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0




if __name__ == "__main__":
    main()
