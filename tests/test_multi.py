#!/usr/bin/env python

from prod.prod import multi


def test_case1():
    assert multi(1, 1) == 1


def test_case2():
    assert multi(1, 1) == 1


def test_case3():
    assert multi(1, 5) == 5


def test_case4():
    assert multi(6, 2) == 12


def test_case5():
    assert multi(2, 5) == 10
