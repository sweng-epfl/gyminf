import unittest
from hamcrest import assert_that, equal_to
from pizza import Pizza


class TestPizza(unittest.TestCase):
    def test_pizza_simple(self):
        pizza = Pizza("Margherite", False, ["fromage"])
        assert_that(str(pizza), equal_to("Pizza Margherite, fromage"))

    def test_calzone_simple(self):
        pizza = Pizza("Margherite", True, ["fromage"])
        assert_that(str(pizza), equal_to("Calzone Margherite, fromage"))
