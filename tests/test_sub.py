#!/usr/bin/env python

from prod.prod import sub


def test_case1():
    assert sub(1, 1) == 0


def test_case2():
    assert sub(1, 1) == 0


def test_case3():
    assert sub(1, 5) == -4


def test_case4():
    assert sub(6, 2) == 4


def test_case5():
    assert sub(2, 5) == -3
