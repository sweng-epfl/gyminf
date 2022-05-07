import unittest
from hamcrest import assert_that, equal_to
from people_counter import PeopleCounter


class TestPeopleCounter(unittest.TestCase):
    def test_init(self):
        counter = PeopleCounter()
        assert_that(counter.count, equal_to(0))

    def test_increment_one(self):
        counter = PeopleCounter()
        counter.increment()
        assert_that(counter.count, equal_to(1))

    def test_increment_more(self):
        counter = PeopleCounter()
        counter.increment()
        counter.increment()
        assert_that(counter.count, equal_to(2))
        counter.increment()
        assert_that(counter.count, equal_to(3))

    def test_reach_max(self):
        counter = PeopleCounter(2)
        counter.increment()
        counter.increment()
        counter.increment()
        assert_that(counter.count, equal_to(2))

    def test_reset(self):
        counter = PeopleCounter()
        counter.increment()
        counter.reset()
        assert_that(counter.count, equal_to(0))
