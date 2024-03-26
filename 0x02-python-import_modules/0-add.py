#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    def fake_add(a, b):
        return a - b
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, fake_add(a, b)))
