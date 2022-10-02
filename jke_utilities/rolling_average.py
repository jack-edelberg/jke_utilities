import pandas as pd
import numpy as np

def rolling_average(data:pd.Series, window:int) -> pd.Series:
    """ Performs a rolling average of data points *window* cells behind the current index. See example for limit cases.
    
    Args:
        data:pd.Series - the series of numbers over which a rolling average should be calculated
        window:int - the number of cells preceding the current cell that should be considered in the rolling average

    Returns:
        pd.Series - a series of the same size as the input containing the rolling average
    
    Ex: 
        data = pd.Series([0, 1, 2, 3, 4, 5]), window = 2
        output[0] = data[0, 1].mean()
        output[1] = data[0, 2].mean()
        output[2] = data[1, 3].mean()
        output[3] = data[2, 4].mean()
        output[4] = data[3, 5].mean()
        output[5] = data[4, 6].mean()

        output = pd.Series[0, 0.5, 1.5, 2.5, 3.5, 4.5]

    """
    data = pd.Series(data.reset_index(drop = True))
    num_items = data.shape[0]
    output = pd.Series(np.nan, index = range(num_items))

    # Catch the edge case at the beginning of the series
    output[0] = data[0]

    for item in range(1, num_items):
        sum_start = (item - window) + 1
        sum_end = item + 1

        # Correct out-of-bounds indices
        if sum_start < 0:
            sum_start = 0
        elif sum_end > num_items:
            sum_end = num_items


        if sum_end == sum_start:
            output[item] = data[sum_start]
            continue

        output[item] = data[sum_start:sum_end].mean()
        continue

    return output