#!/usr/bin/env python

from prod.prod import sum


def test_case1():
    assert sum(1, 1) == 2


def test_case2():
    assert sum(1, 1) == 2


def test_case3():
    assert sum(1, 5) == 6


def test_case4():
    assert sum(6, 2) == 8


def test_case5():
    assert sum(2, 5) == 7
