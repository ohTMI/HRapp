import statistics as stat

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

    if len(data) == 0 or n == 0:
        return []
    for num in range(0, len(data), n):
        window = data[num:num + n]
        maximums.append(max(window))
        
    return maximums

def window_average(data: list, n: int) -> list:
    
    average = []

    if len(data) == 0 or n == 0:
        return []
    for avg in range(0, len(data), n):
        window2 = data[avg:avg + n]
        calc = sum(window2) / len(window2)
        math = round(calc, 2)
        average.append(math)
    return average   

def window_stddev(data: list, n: int) -> list:
    
    stddev = []

    if len(data) == 0 or n == 0:
        return []
    for out in range(0, len(data), n):
        window3 = data[out:out + n]
        if len(window3) > 1:
            stan = stat.stdev(window3)
            math2 = round(stan, 2)
            stddev.append(math2) 
            
    return stddev
