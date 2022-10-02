import pandas as pd
import numpy as np

def linear_interpolation(df:pd.DataFrame,
                          indices:list[int],
                          column:str) -> dict:
    """ This function takes a dataframe containing a column with missing values and fills the missing values with a linear interpolation of the nearest adjacent values. For each value in the data to be interpolated, if either of the adjecent values is empty, the cell is not filled with an interpolated value.

    Args:
        df:pd.DataFrame - The DataFrame containing, at a minimum, the column we are addressing and the index
        indices:list[int] - a list of the indices of the missing values
        column:str - the name of the column to be interpolated

    Returns:
        dict with following items:
            pd.DataFrame - the original DataFrame with previously empty cells filled by linear interpolation
            bool - True if all the values in indices were interpolated, false otherwise
    """
    df = df.copy()
    
    uninterpolated_indices = []

    # Fill missing values with linear interpolation of adjacent values
    for row in indices:

        # Check to see if adjacent rows are also empty
        if ((row - 1) in indices) or ((row + 1) in indices):
            uninterpolated_indices.append(row)
            continue

        prior_value = df.loc[row - 1, column]
        latter_value = df.loc[row + 1, column]

        df.loc[row, column] = \
            np.average([prior_value, latter_value])

    # Print the indices that were uninterpolatable, if any
    if len(uninterpolated_indices) > 0:
        print(f"The following rows were not interpolated:")
        print(uninterpolated_indices)
        return {"data":df, "complete": False}

    return {"data":df, "complete": True}