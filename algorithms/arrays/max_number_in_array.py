def get_max():
    size = int(input("List size: "))
    _list = []
    for i in range(1, size + 1):
        num = int(input(f"Enter {i}. number: "))
        _list.append(num)

    _max = _list[0]
    for i in range(1, size):
        n = _list[i]
        if n > _max:
            _max = n
    return _max


ans = get_max()
print("Largest in given array is", ans)
