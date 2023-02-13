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
from Cross_section_analyzer import *  # Imports all functions from program.
# ======================================================================================================================
# PART 1: DEFINE FUNCTIONS ---------------------------------------------------------------------------------------------
# ======================================================================================================================
# location = ['upper left', 'upper right', 'lower left', 'lower right', 'upper center', 'lower center', 'center left', 'center right', 'center', 'best']  # Defines list. Complete list of matplotlib legend placements.
ibm = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']  # Defines list. Sets IBM colorblind friendly palette in color hex color codes for ultramarine, indigo, magenta, orange, and gold.
ibm_clr_hx = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']  # Defines list. Sets IBM colorblind friendly palette in color hex color codes for ultramarine, indigo, magenta, orange, and gold.
ibm_clr_rgb = [(100, 143, 255), (120, 94, 240), (220, 38, 127), (254, 97, 0), (255, 176, 0)]
# Sets muted Tol colorblind friendly palette in color hex color codes for indigo, cyan, teal, green, olive, sand, rose, wine, purple, and pale grey.
# 2008 = 0, 1994 = 3, 1978 = 2, 1975 = 4, 1964 = 5, 1939 = 6, 1850S = 7.
# tol_vibrant = ['#0077BB', '#33BBEE', '#009988', '#EE7733', '#CC3311', '#EE3377', '#BBBBBB']  # Defines list. Sets
# vibrant Tol colorblind friendly palette in color hex color codes for blue, cyan, teal, orange, red, magenta, grey.
# marker_mpltlib = ['.', ',', 'o', 'v', '^', '<', '>',
#                           '1', '2', '3', '4', '8',
#                           's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd',
#                           '|', '_', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ' ']  # Defines list. Complete list of matplotlib plot markers.


# initialization general
# FUNCTIONS FOR NOW
def plot_lines(lines, plot_number, figure_size, x, y, label, color, marker, marker_size,
               line_width, alpha, fontsize_ticks, x_label, fontsize_axis, label_pad, y_label,
               title, pause_length,
               pause, location, marker_scale, frame_alpha,
               label_spacing):  # Defines function. For single cross-section plotting.
    plt.figure(plot_number, figsize=figure_size)  # Creates plot window.
    ax = plt.gca()  # Defines variable. Retrieves plot axes instance.
    if lines == 1:
        ax.plot(x, y, label=label, c=color, marker=marker, markersize=marker_size,
                linewidth=line_width,
                alpha=alpha)  # Creates line plot of arrays from axes instance. Sets format.
    if lines != 1:
        lines = lines + 1
        line_list = range(1, lines, 1)
        print(*line_list)
        for i in line_list:
            index = line_list.index(i)
            ax.plot(x[index], y[index], label=label[index], c=color[index],
                    marker=marker[index], markersize=marker_size, linewidth=line_width,
                    alpha=alpha)  # Creates line plot of arrays from axes instance. Sets format.
        ax.legend(loc=location, markerscale=marker_scale, framealpha=frame_alpha,
                  labelspacing=label_spacing)  # Creates legend. Through automatic label detection.
    plt.xticks(fontsize=fontsize_ticks)  # Sets x-axis tick mark format.
    plt.xlabel(x_label, fontsize=fontsize_axis,
               labelpad=label_pad)  # Creates x-axis label. Sets format.
    plt.ylabel(y_label,
               fontsize=fontsize_axis)  # Creates x-axis label. Sets format.  # Creates y-axis label. Sets font size.
    plt.yticks(fontsize=fontsize_ticks)  # Sets y-axis tick mark format.
    plt.title(title)  # Creates plot title.

    if pause == 1:  # Conditional statement. For display.
        plt.pause(
            pause_length)  # Displays plot. For set interval of seconds and closes without clearing.
    elif pause == 0:  # Conditional statement. For display.
        plt.show()  # Displays plot. Indefinite and cleared upon close.

def create_folder(level, path):  # Defines function. For generating directory paths.
    if not os.path.exists(path):  # Checks if folder exists. Skips step if exists.
        os.mkdir(path)  # Creates folder if it does not exist.
        print('New directory level', level, '\033[0;32m' + path + '\033[0m', 'created')  # Displays objects.

def upload_csv(path, label, dsply):  # Defines function. For uploading .csv and conversion to DataFrame.
    csv_data = pd.read_csv(path)  # Uploads .csv file. Input data.
    df = pd.DataFrame(csv_data)  # Converts .csv file to DataFrame. For Python manipulation.
    pd.set_option('display.max_columns', None)  # Adjusts DataFrame format. Displays all DataFrame columns.
    if dsply == 1:  # Conditional statement. For display.
        print('\033[1m' + 'UPLOADED .CSV DATA FOR ' + label + '\033[0m', '\n...\n', df, '\n')  # Displays objects.
    return df  # Ends execution of function.

def forward_range(start, end, step, data_label, dsply):  # Defines function. For generating forward range array between two numbers.
    end = end + 1  # Defines variable. Sets end of range to include final input value.
    end_label = end - 1  # Defines variable. Sets label for display.
    frwd_rng = np.arange(start, end, step)  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print(data_label, start, '&', end_label, ':', frwd_rng)  # Displays objects.
    return frwd_rng  # Ends execution of function.

def reverse_range(start, end, step, data_label, dsply):  # Defines function. For generating forward range array between two numbers.
    end = end - 1  # Defines variable. Sets end of range to include final input value.
    end_label = end + 1  # Defines variable. Sets label for display.
    rev_rng = np.arange(start, end, step)  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print(data_label, start, '&', end_label, ':', rev_rng, '\n')  # Displays objects.
    return rev_rng  # Ends execution of function.

def slice_DataFrame_rows1(dataframe, column, row_value, label, dsply):  # Defines function. For DataFrame slicing by single row value.
    df_slc_r = dataframe[dataframe[column] == row_value]  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print('\033[1m' + label + ' ' + str(row_value) + ' DATA' + '\033[0m', '\n..\n', df_slc_r, '\n')  # Displays objects.
    return df_slc_r  # Ends execution of function.

def slice_DataFrame_rows2(dataframe, column1, row_value1, label1, row_value2, label2,
                          dsply):  # Defines function. For DataFrame slicing by row value.
    df_slc_r = dataframe[dataframe[column1] == row_value1]  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print('\033[1m' + label2 + ' ' + str(row_value2) + ' ' + label1 + ' ' + str(row_value1) + ' DATA' + '\033[0m',
              '\n..\n', df_slc_r, '\n')  # Displays objects.
    return df_slc_r  # Ends execution of function.

def slice_DataFrame_cell(dataframe, column, index, data_label,
                         dsply):  # Defines function. For DataFrame slicing by row value.
    df_slc_cl = dataframe.loc[index, column]  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print(data_label + ':', df_slc_cl, '\n')  # Displays objects.
    return df_slc_cl  # Ends execution of function.

def slice_DataFrame_columns1(dataframe, column, data_label,
                             dsply):  # Defines function. For DataFrame slicing by row value.
    df_slc_c = dataframe[column]  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print('\033[1m' + data_label + ' DATA' + '\033[0m', '\n..\n', df_slc_c, '\n')  # Displays objects.
    return df_slc_c  # Ends execution of function.

def max_value_column(dataframe, data_label, units,
                     dsply):  # Defines function. For retrieving maximum value from DataFrame column.
    max = dataframe.max()  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print('Maximum column value:', max, data_label, units)  # Displays objects.
    return max  # Ends execution of function.

def min_value_column(dataframe, data_label, units,
                     dsply):  # Defines function. For retrieving minimum value from DataFrame column.
    min = dataframe.min()  # Defines function format.
    if dsply == 1:  # Conditional statement. For display.
        print('Minimum column value:', min, data_label, units)  # Displays objects.
    return min  # Ends execution of function.


def hydraulic_geometry(dataframe, column1, data_label1, data_label2, units, data_label3, data_label4, column2,
                       data_label5, data_label6, data_label7, data_label8, dsply):
    df_strm_offst = slice_DataFrame_columns1(dataframe, column1, data_label1, 0)

    offst1 = min_value_column(df_strm_offst, data_label2, units, 0)
    offst2 = max_value_column(df_strm_offst, data_label2, units, 0)

    if offst1 < offst2:
        wdth = offst2 - offst1
    elif offst1 > offst2:
        sys.exit('No stream channel detected')
    elif offst1 == offst2:
        sys.exit('No stream channel detected')

    if dsply == 1:  # Conditional statement. For display.
        print(data_label3 + units + '\n  ' + data_label4 + '%.1f' % wdth)

    df_strm_elvtn = slice_DataFrame_columns1(dataframe, column2, data_label5, 0)
    elvtn1 = min_value_column(df_strm_elvtn, data_label6, units, 0)
    elvtn2 = max_value_column(df_strm_elvtn, data_label6, units, 0)

    if elvtn1 < elvtn2:
        dpth = elvtn2 - elvtn1
    elif elvtn1 > elvtn2:
        sys.exit('No stream channel detected')
    elif elvtn1 == elvtn2:
        sys.exit('No stream channel detected')
    elif elvtn1 | elvtn2 <= 0:
        sys.exit('Negative values')

    if dsply == 1:  # Conditional statement. For display.
        print('  ' + data_label7 + '%.2f' % dpth)

    hydro_rad = (wdth * dpth) / (wdth + 2 * dpth)

    if dsply == 1:  # Conditional statement. For display.
        print('  ' + data_label8 + '%.2f' % hydro_rad)

    return wdth, dpth, hydro_rad

def create_append_list(value, data_label1, new_list, chck):
    # create lists
    try:
        value
    except NameError:
        sys.exit(data_label1 + 'value undefined')
    else:
        new_list.append(value)
    if chck == 1:
        print(new_list)
    return new_list

def get_color(label):
    if label == '2008':  # Conditional statement. For display.
        color = tol_mtd[0]  # Defines variable. Sets plot color.
    elif label == '1994':  # Conditional statement. For display.
        color = tol_mtd[3]  # Defines variable. Sets plot color.
    elif label == '1978':  # Conditional statement. For display.
        color = tol_mtd[2]  # Defines variable. Sets plot color.
    elif label == '1975':  # Conditional statement. For display.
        color = tol_mtd[4]  # Defines variable. Sets plot color.
    elif label == '1964':  # Conditional statement. For display.
        color = tol_mtd[5]  # Defines variable. Sets plot color.
    elif label == '1939':  # Conditional statement. For display.
        color = tol_mtd[6]  # Defines variable. Sets plot color.
    elif label == '1850s':  # Conditional statement. For display.
        color = tol_mtd[7]  # Defines variable. Sets plot color.
    return color

def get_marker(label):
    if label == '2008':  # Conditional statement. For display.
        marker = mrkr_mpltlib[-1]  # Defines variable. Sets plot marker.
    elif label == '1994':  # Conditional statement. For display.
        marker = mrkr_mpltlib[0]  # Defines variable. Sets plot marker.
    elif label == '1978':  # Conditional statement. For display.
        marker = mrkr_mpltlib[8]  # Defines variable. Sets plot marker.
    elif label == '1975':  # Conditional statement. For display.
        label = mrkr_mpltlib[11]  # Defines variable. Sets plot marker.
    elif label == '1964':  # Conditional statement. For display.
        marker = mrkr_mpltlib[6]  # Defines variable. Sets plot marker.
    elif label == '1939':  # Conditional statement. For display.
        marker = mrkr_mpltlib[2]  # Defines variable. Sets plot marker.
    elif label == '1850s':  # Conditional statement. For display.
        marker = mrkr_mpltlib[-2]  # Defines variable. Sets plot marker.
    return marker