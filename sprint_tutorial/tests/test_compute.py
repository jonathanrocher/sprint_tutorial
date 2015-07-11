""" Tests for the compute module
"""
from nose.tools import assert_equal

from sprint_tutorial.compute import my_sum

#run nosetests

def test_my_sum1():
    assert_equal(my_sum(3, 5), 8)

def test_my_sum2():
    assert_equal(my_sum(5, 5), 10)
