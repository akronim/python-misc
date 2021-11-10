def find_max(numbers):
    _max = 0
    for number in numbers:
        if number > _max:
            _max = number
    return _max


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


