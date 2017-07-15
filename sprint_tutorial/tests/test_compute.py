""" Tests for the compute module
"""
from nose.tools import assert_equal

from sprint_tutorial.compute import my_sum


def test_my_sum1():
    assert_equal(my_sum(0, 0), 0)


def test_my_sum2():
    assert_equal(my_sum(1, -1), 0)
