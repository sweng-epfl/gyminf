import unittest
from hamcrest import assert_that, equal_to, contains_exactly, calling, raises
from functions import fibonacci, split_string, shuffle
from copy import copy


class TestFibo(unittest.TestCase):
    def test_postitive_fibo(self):
        assert_that(fibonacci(0), equal_to(1))
        assert_that(fibonacci(1), equal_to(1))
        assert_that(fibonacci(2), equal_to(2))
        assert_that(fibonacci(3), equal_to(3))
        assert_that(fibonacci(4), equal_to(5))

    def test_negative_fibo(self):
        assert_that(
            calling(fibonacci).with_args(-1),
            raises(ValueError)
        )


class TestSplitString(unittest.TestCase):
    def test_split(self):
        assert_that(split_string("aXb", "X"), equal_to(["a", "b"]))
        assert_that(split_string("aXb", "X"), contains_exactly("a", "b"))
        # assert_that(split_string("bla?bli", "?"), equal_to(["bla", "bli"]))


class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        ma_liste = [1, 2, 3, 4]
        originale = copy(ma_liste)
        shuffle(ma_liste)
        assert_that(len(ma_liste), equal_to(len(originale)))
        assert_that(sorted(ma_liste), equal_to(sorted(originale)))
