"""
2022-7-11
by JerryQiu
"""

def text(*args, end=""):
    for i in args:
        print(i, end="")
    if end == "\n":
        print()
    else:
        ...
    return


text("Hello World")
