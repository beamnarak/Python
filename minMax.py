def min(*args, **kwargs):
    req = list(args[0]) if len(args) == 1 else list(args)
    key = kwargs.get("key", None)
    for a in range(len(req)):
        key = key if key else type(req[a]*1)
        if a == 0:
            minkey = key
            min = req[a]
        elif key(req[a]) < minkey(min):
            minkey = key
            min = req[a]

    return min


def max(*args, **kwargs):
    req = list(args[0]) if len(args) == 1 else list(args)
    key = kwargs.get("key", None)
    for a in range(len(req)):
        key = key if key else type(req[a]*1)
        if a == 0:
            maxkey = key
            max = req[a]
        elif key(req[a]) > maxkey(max):
            maxkey = key
            max = req[a]

    return max

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"