#!/usr/bin/env python


def main():
    print("Multi: {}".format(multi(2, 5)))
    print("Sum: {}".format(sum(2, 5)))
    print("Sub: {}".format(sub(2, 5)))
    print("Div: {}".format(div(2, 5)))


def multi(a, b):
    return a * b


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    if b == 0:
        raise ValueError("You can not divide by zero!")
    return a / b


if __name__ == "__main__":
    main()
