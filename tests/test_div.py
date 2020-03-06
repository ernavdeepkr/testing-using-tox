#!/usr/bin/env python

from prod.prod import div


def test_case1():
    assert div(1, 1) == 1


def test_case2():
    assert div(1, 1) == 1


def test_case3():
    assert div(1, 5) == 0.2


def test_case4():
    assert div(6, 2) == 3


def test_case5():
    assert div(2, 5) == 0.4
