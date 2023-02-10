# ======================================================================================================================
# WHITEWATER RIVER VALLEY MINNESOTA, SEDIMENTATION SURVEY DATA ANALYSIS * ----------------------------------------------
# SECONDARY PROGRAM 1 OF 2 * -------------------------------------------------------------------------------------------
# ======================================================================================================================

# SIGNAL START ---------------------------------------------------------------------------------------------------------

# print('\n\033[1m' + 'START CROSS-SECTIONAL ANALYSES!!!' + '\033[0m', '\n...\n')  # Displays string. Makes font bold and
# adds new line(s).

# IMPORT MODULES -------------------------------------------------------------------------------------------------------

import time, os  # Imports "Time and access conversions" and "Miscellaneous operating system interfaces". Enables use
# of various time–related functions and operating system dependent functionality.
import pandas as pd, numpy as np, matplotlib.pyplot as plt  # Imports "Python data analysis library", a module for working
# with arrays, and "Visualization with Python", with aliases. Enables DataFrame array functionality, using arrays and plotting tools.

# ======================================================================================================================
# PART 1: DEFINE FUNCTIONS ---------------------------------------------------------------------------------------------
# ======================================================================================================================
# location = ['upper left', 'upper right', 'lower left', 'lower right', 'upper center', 'lower center', 'center left', 'center right', 'center', 'best']  # Defines list. Complete list of matplotlib legend placements.
ibm = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']  # Defines list. Sets IBM colorblind friendly palette in color hex color codes for ultramarine, indigo, magenta, orange, and gold.
# Sets muted Tol colorblind friendly palette in color hex color codes for indigo, cyan, teal, green, olive, sand, rose, wine, purple, and pale grey.
# 2008 = 0, 1994 = 3, 1978 = 2, 1975 = 4, 1964 = 5, 1939 = 6, 1850S = 7.
# tol_vibrant = ['#0077BB', '#33BBEE', '#009988', '#EE7733', '#CC3311', '#EE3377', '#BBBBBB']  # Defines list. Sets
# vibrant Tol colorblind friendly palette in color hex color codes for blue, cyan, teal, orange, red, magenta, grey.
# marker_mpltlib = ['.', ',', 'o', 'v', '^', '<', '>',
#                           '1', '2', '3', '4', '8',
#                           's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd',
#                           '|', '_', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ' ']  # Defines list. Complete list of matplotlib plot markers.


# initialization general
def slice_DataFrame_rows2(dataframe, column1, slice1, label1, column2, slice2, label2):
    df_slc_r2=dataframe[(dataframe[column1] ==slice1) & (dataframe[column2] ==slice2)]
    print('\033[1m'+ label1 + ' ' + str(slice1) +' '+ label2 +' '+str(slice2)+ ' DATA'+'\033[0m','\n..\n', df_slc_r2,'\n')
    return df_slc_r2

def slice_DataFrame_column1(dataframe, column1, label1):
    df_slc_c1=dataframe[column1]
    print('\033[1m'+ label1 + ' DATA'+ '\033[0m','\n..\n', df_slc_c1,'\n')
    return df_slc_c1

def plot_line(number, figure_size, x, y, label, color, marker, alpha, xlabel, fontsize_axis, ylabel, title,pause):
    plt.figure(number, figsize=figure_size)
    ax=plt.gca()
    ax.plot(x, y, label=label, c=color, marker=marker, alpha=alpha)  # Creates line
    # plot of arrays from axes instance. Sets label, color, marker type, and transparency.
    # ax.legend()  # Creates legend through automatic label detection.
    # plt.xlabel(xlabel, fontsize=fontsize_axis)  # Creates x-axis label. Sets font size.
    # plt.ylabel(ylabel, fontsize=fontsize_axis)  # Creates y-axis label. Sets font size.
    # plt.title(title)  # Creates plot title.
    if pause == 1:
        plt.pause(2)  # Displays and updates active figure before pausing for interval seconds.
    elif pause == 0:
        plt.show()

def slice_DataFrame_rows2(dataframe, column1, rows1, label1, column2, rows2,
                          label2):  # Defines function. For slicing DataFrame with row value selection in two columns.
    df_slc_r2 = dataframe[
        (dataframe[column1] == rows1) & (dataframe[column2] == rows2)]  # Defines format of function.
    if chck == 1:  # Conditional statement.
        print('\033[1m' + label1 + ' ' + str(rows1) + ' ' + label2 + ' ' + str(rows2) + ' DATA' + '\033[0m',
              '\n..\n', df_slc_r2, '\n')  # Displays objects.
    return df_slc_r2  # Ends execution of function.