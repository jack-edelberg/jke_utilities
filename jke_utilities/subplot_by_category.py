import pandas as pd
import matplotlib.pyplot as plt
import seaborn

def subplot_by_category(df:pd.DataFrame, category:str,
                        x_var:str, y_var:str, hue_var:str,
                        x_lim:tuple[float], y_lim:tuple[float]) \
                             -> plt.Figure:
    """ This function creates a figure containing stacked lineplots with each lineplot corresponding to one value of the category column in the passed df.

    Args:
        df:pd.DataFrame - The dataframe containing the data to plot
        category:str - The name of the column containing the categories that will determine what is plotted on each individual chart (ie: "year")
        x_var:str - The name of the column containing the x data
        y_var:str - The name of the column containing the y_data
        hue_var:str - The name of the column containing a variable designating different data to be plotted on each axis. Pass an empty string if there is only one line per axis.
        x_lim:tuple[float] - The x limits to be used on each axis
        y_lim:tuple[float] - The y limits to be used on each axis

    Returns:
        plt.Figure - a figure object containing a list of the axes contained in the figure
    """

    # Determine the number of plots and initialize the figure
    categories = list(df.loc[:, category].unique())
    num_plots = len(categories)
    plt.subplots(num_plots, 1, figsize = (10, 3 * num_plots))
    plt.tight_layout()


    cur_subplot = 0
    for cur_cat in categories:
        # Select the next subplot
        cur_subplot += 1
        plt.subplot(num_plots, 1, cur_subplot)

        # Pull the data for this subplot        
        cur_cat_df = \
            df.loc[df.loc[:, category] == cur_cat, :]
        
        # Draw the plot, using a hue variable if passed
        if hue_var == "":
            ax = sns.lineplot(data = cur_cat_df, 
                              x = x_var, y = y_var)
        else:
            ax = sns.lineplot(data = cur_cat_df, 
                              x = x_var, y = y_var, hue = hue_var)

        # Standardized formatting of the plot
        ax.set_xlim(x_lim[0], x_lim[1])
        ax.set_ylim(y_lim[0], y_lim[1])
        ax.set_title(cur_cat,
                     fontdict = fontdict_plot_title,
                     y = 0.1, x = 0.05)

    return plt.gcf()