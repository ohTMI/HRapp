def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """

    if len(data) == 0:
        return data
    
    new_data = []
    for v in data:
        if v.strip().isdigit():
            v = v.strip()
            new_data.append(int(v))
    return new_data 


def filter_outliers(data: list) -> list:
    
    if len(data) == 0:
        return data
    
    new_data = []
    for v in data:
        if v > 30 and v < 250:
            new_data.append(v)
    return new_data 
