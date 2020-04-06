def frog_jump(x, y, j):
    """
    https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
    :param x: start position
    :param y: end position
    :param j: jump size
    :return:
    """
    return ((y - x) // j) + 1 if ((y - x) // j) < ((y - x) / j) else ((y - x) // j)
