def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []

    return maximums
    window_size = n


def window_average(data: list, n: int) -> list:
    res = []
    mosm = sum(data[:n])
    res.append(mosm / n)
    for blnk in range[len(data) - n]:
        mosm += (data[blnk + n] - data[blnk])
        res.append(mosm / n)
    return res


def window_stddev(data: list, n: int) -> list:
    pass
