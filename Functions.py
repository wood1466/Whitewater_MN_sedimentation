# ======================================================================================================================
# WHITEWATER RIVER VALLEY MINNESOTA, SEDIMENTATION SURVEY DATA ANALYSIS * ----------------------------------------------
# SECONDARY PROGRAM 1 OF 2 * -------------------------------------------------------------------------------------------
# ======================================================================================================================

# SIGNAL START ---------------------------------------------------------------------------------------------------------

# print('\n\033[1m' + 'START CROSS-SECTIONAL ANALYSES!!!' + '\033[0m', '\n...\n')  # Displays string. Makes font bold and
# adds new line(s).

# IMPORT MODULES -------------------------------------------------------------------------------------------------------

import time, os, sys  # Imports "Time and access conversions", "Miscellaneous operating system interfaces", and
# "System specific parameters and functions". Enables use of various time–related functions and operating system
# dependent functionality.
import pandas as pd, numpy as np, matplotlib.pyplot as plt, scipy as sc # Imports "Python data analysis library", a comprehensive
# mathematics library, and a plotting interface, with alias. Enables DataFrame array functionality.
import matplotlib.colors
from matplotlib.colors import LinearSegmentedColormap
import math
# ======================================================================================================================
# PART 1: DEFINE FUNCTIONS ---------------------------------------------------------------------------------------------
# ======================================================================================================================
location = ['upper left', 'upper right', 'lower left', 'lower right', 'upper center', 'lower center', 'center left', 'center right', 'center', 'best']  # Defines list. Complete list of matplotlib legend placements.
ibm = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']  # Defines list. Sets IBM colorblind friendly palette in color hex color codes for ultramarine, indigo, magenta, orange, and gold.
ibm_clr_hx = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']  # Defines list. Sets IBM colorblind friendly palette in color hex color codes for ultramarine, indigo, magenta, orange, and gold.
ibm_clr_rgb = [(100, 143, 255), (120, 94, 240), (220, 38, 127), (254, 97, 0), (255, 176, 0)]
# Sets muted Tol colorblind friendly palette in color hex color codes for indigo, cyan, teal, green, olive, sand, rose, wine, purple, and pale grey.
# 2008 = 0, 1994 = 3, 1978 = 2, 1975 = 4, 1964 = 5, 1939 = 6, 1850S = 7.
tol_vibrant = ['#0077BB', '#33BBEE', '#009988', '#EE7733', '#CC3311', '#EE3377', '#BBBBBB']  # Defines list. Sets
# vibrant Tol colorblind friendly palette in color hex color codes for blue, cyan, teal, orange, red, magenta, grey.
marker_mpltlib = ['.', ',', 'o', 'v', '^', '<', '>',
                          '1', '2', '3', '4', '8',
                          's', 'p', 'P', '*', 'h', 'H', '+', 'x', 'X', 'D', 'd',
                          '|', '_', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ' ']  # Defines list. Complete list of matplotlib plot markers.
tol_mtd = ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', '#CC6677', '#882255', '#AA4499', '#DDDDD']  # Defines list. Sets Paul Tol muted colorblind friendly palette via hex color codes.
lin_styls = ['solid', 'dotted', 'dashed', 'dashdot']
# TEMPORARY FUNCTION HOUSING ===========================================================================================

def create_folder(level, path):  # Defines function. For generating directory paths.
    if not os.path.exists(path):  # Checks if folder exists. Skips step if exists.
        os.mkdir(path)  # Creates folder if it does not exist.
        print('New directory level', level, '\033[0;32m' + path + '\033[0m', 'created')  # Displays objects.

def upload_csv(path, display_label, display):  # Defines function. For uploading .csv and converting to a DataFrame.
    csv_data = pd.read_csv(path)  # Uploads .csv file. Input data.
    df = pd.DataFrame(csv_data)  # Defines DataFrame. Converts from .csv. For Python manipulation.
    pd.set_option('display.max_columns', None)  # Adjusts DataFrame format. Displays all DataFrame columns.
    if display == 1:  # Conditional statement. For display.
        print('\033[1m' + 'UPLOADED .CSV DATA: ' + display_label + '\033[0m', '\n...\n', df, '\n')  # Displays objects.
    return df  # Ends function execution.

def forward_range(start, end, step, display_label, display):  # Defines function. For generating forward array between two numbers.
    end = end + 1  # Defines variable. Resets end of range so array includes final input value.
    end_label = end - 1  # Defines variable. For display.
    frwd_rng = np.arange(start, end, step)  # Defines function format.
    if display == 1:  # Conditional statement. For display.
        print(display_label + '\n  Limits: ' + str(start) + ' & ' + str(end_label) + ' --> List:', frwd_rng)  # Displays objects.
    return frwd_rng  # Ends function execution.

def reverse_range(start, end, step, display_label, display):  # Defines function. For generating reverse array between two numbers.
    end = end - 1  # Defines variable. Resets end of range so array includes final input value.
    end_label = end + 1  # Defines variable. For display.
    rev_rng = np.arange(start, end, step)  # Defines function format.
    if display == 1:  # Conditional statement. For display.
        print(display_label + '\n  Limits: ' + str(start) + ' & ' + str(end_label) + ' --> List:', rev_rng)  # Displays objects.
    return rev_rng  # Ends function execution.

def slice_DataFrame_rows(search_type, dataframe, column, value, display_label, display):  # Defines function. For DataFrame slicing by row value.
    if search_type == 'equals':  # Conditional statement. Sets function format.
        df_slc_r = dataframe[dataframe[column] == value]  # Defines function format.
    elif search_type == 'less than':  # Conditional statement. Sets function format.
        df_slc_r = dataframe[dataframe[column] < value]  # Defines function format.
    elif search_type == 'less than/equal':  # Conditional statement. Sets function format.
        df_slc_r = dataframe[dataframe[column] <= value]  # Defines function format.
    elif search_type == 'more than':  # Conditional statement. Sets function format.
        df_slc_r = dataframe[dataframe[column] > value]  # Defines function format.
    elif search_type == 'more than/equal':  # Conditional statement. Sets function format.
        df_slc_r = dataframe[dataframe[column] >= value]  # Defines function format.
    elif search_type == 'does not equal':  # Conditional statement. Sets function format.
        df_slc_r = dataframe[dataframe[column] != value]  # Defines function format.
    df_slc_r = df_slc_r.loc[:, ~df_slc_r.columns.str.match('Unnamed')]  # Redefines DataFrame. Searches for empty columns and deletes them.
    if display == 1:  # Conditional statement. For display.
        print('\033[1m' + display_label + ' ' + search_type.upper() + ' ' + str(value) + '\033[0m', '\n...\n', df_slc_r, '\n')  # Displays objects.
    return df_slc_r  # Ends function execution.

def slice_DataFrame_cell(dataframe, position, column, display_label, display):  # Defines function. For DataFrame slicing by row value and index.
    index = dataframe.index  # Defines object. Retrieves DataFrame index.
    df_slc_cl = dataframe.loc[index[position], column]  # Defines function format.
    if display == 1:  # Conditional statement. For display.
        print(display_label + ':', df_slc_cl, '\n')  # Displays objects.
    return df_slc_cl  # Ends function execution.

def slice_DataFrame_columns(dataframe, column, check_duplicates, display_label, display):  # Defines function. For DataFrame slicing by column.
    df_slc_c = dataframe[column]  # Defines function format.
    if check_duplicates == 1:  # Conditional statement.
        df_slc_c = df_slc_c.drop_duplicates(keep='first')  # Redefines DataFrame. Drops all duplicate values in
        # column.
    if display == 1:  # Conditional statement. For display.
        print('\033[1m' + display_label + '\033[0m', '\n...\n', df_slc_c, '\n')  # Displays objects.
    return df_slc_c  # Ends function execution.

def max_value_DataFrame(dataframe, display_label, display):  # Defines function. For retrieving maximum value of DataFrame column.
    mx = dataframe.max()  # Defines function format.
    if display == 1:  # Conditional statement. For display.
        print('Maximum column value: ' + display_label + ' ' + str(mx))  # Displays objects.
    return mx  # Ends function execution.

def min_value_DataFrame(dataframe, display_label, display):  # Defines function. For retrieving minimum value from DataFrame column.
    mn = dataframe.min()  # Defines function format.
    if display == 1:  # Conditional statement. For display.
        print('Minimum column value: ' + display_label + ' ' + str(mn))  # Displays objects.
    return mn  # Ends function execution.

def get_plot_feature_by_year(label, list, alternate):  # Defines function. For plot feature selection from input list.
    if label == '2008':  # Conditional statement.
        if alternate == 0:
            feature = list[0]  # Defines variable. Sets plot feature.
        elif alternate == 1:  # Conditional statement.
            feature = list[-3]  # Defines variable. Sets plot feature.
    elif label == '1994':  # Conditional statement.
        feature = list[3]  # Defines variable. Sets plot feature.
    elif label == '1978':  # Conditional statement.
        feature = list[2]  # Defines variable. Sets plot feature.
    elif label == '1975':  # Conditional statement.
        feature = list[4]  # Defines variable. Sets plot feature.
    elif label == '1964':  # Conditional statement.
        feature = list[5]  # Defines variable. Sets plot feature.
    elif label == '1939':  # Conditional statement.
        feature = list[6]  # Defines variable. Sets plot feature.
    elif label == '1850s':  # Conditional statement.
        feature = list[7]  # Defines variable. Sets plot feature.
    else:  # Conditional statement.
        feature = list[-1]  # Defines variable. Sets plot feature.
    return feature  # Ends function execution.

def plot_lines(lines, plot_number, figure_size, x, y, label, color, marker, marker_size, line_width, line_style, alpha, show_legend, location, marker_scale, frame_alpha, label_spacing,invert_x, fontsize_ticks, x_label, fontsize_axis, label_pad, y_label, title, pause, pause_length):  # Defines function. For line plotting.
    plt.figure(plot_number, figsize=figure_size)  # Creates plot window. Sets figure size.
    ax = plt.gca()  # Defines variable. Retrieves plot axes instance.
    if lines == 1:  # Conditional statement. Plots single line.
        ax.plot(x, y, label=label, c=color, marker=marker, markersize=marker_size, linewidth=line_width, linestyle=line_style,
                alpha=alpha)  # Creates line plot. Sets display format.
        if show_legend == 1:  # Conditional statement. Shows legend if desired for single line plotting.
            ax.legend(loc=location, markerscale=marker_scale, framealpha=frame_alpha, labelspacing=label_spacing)  # Creates legend. Through automatic label detection.
    if lines != 1:  # Conditional statement. Plots multiple lines.
        lines = lines + 1  # Defines variable. For establishing looped plotting framework.
        line_list = range(1, lines, 1)  # Defines list. Creates range of integers for looped plotting.
        for a in line_list:  # Begins loop through list elements. Loops through line numbers.
            index = line_list.index(a)  # Defines variable. Retrieves index of element in list. For format selection.
            ax.plot(x[index], y[index], label=label[index], c=color[index], marker=marker[index],
                    markersize=marker_size, linewidth=line_width, linestyle=line_style[index], alpha=alpha)  # Creates line plot. Sets display format.
        ax.legend(loc=location, markerscale=marker_scale, framealpha=frame_alpha,
                  labelspacing=label_spacing)  # Creates legend. Through automatic label detection.
    plt.xticks(fontsize=fontsize_ticks)  # Sets x-axis ticks. Sets format.

    plt.xlabel(x_label, fontsize=fontsize_axis, labelpad=label_pad)  # Creates x-axis label. Sets format.
    plt.ylabel(y_label, fontsize=fontsize_axis)  # Creates y-axis label. Sets format.
    plt.yticks(fontsize=fontsize_ticks)  # Sets y-axis ticks. Sets format.
    if invert_x == 1:
        ax.invert_xaxis()
    plt.title(title)  # Creates plot title.
    if pause == 1:  # Conditional statement. For display format.
        plt.pause(pause_length)  # Displays plot. For set interval of seconds and closes without clearing.
    elif pause == 0:  # Conditional statement. For display format.
        plt.show()  # Displays plot. Indefinite and cleared upon close.
    elif pause == 2:
        pass

def name_levels(directory_levels, folder_labels, output_folder, display_label,
                display):  # Defines function. For defining list of directory levels for looped creation.
    index = np.arange(0, directory_levels, 1)  # Defines array. Index values for looped naming.
    for a in index:  # Begins loop through array elements. Loops through indices.
        folder_name = folder_labels[a]  # Defines variable as array element. Selects name of folder.
        if a == 0:  # Conditional statement. Executes lines if element is first.
            level_a = output_folder + folder_name  # Defines string. Builds path directory from folder name.
            levels = [level_a]  # Defines list.
        elif a != 0:  # Conditional statement. Executes lines if element is not first.
            level_a = level_a + folder_name  # Defines string. Builds path directory from folder name.
            levels.append(level_a)  # Redefines list. Appends with new element.
        if display == 1:  # Conditional statement. For display.
            print(display_label, levels)  # Display objects.
    return levels  # Ends function execution.

def export_file(type, number, file_name, end_path, figure_extension, dataframe, truth_statement, display_label,
                display):  # Defines function. For file export.
    if type == 'figure':  # Conditional statement. Executes lines below if file is a figure.
        plt.figure(number)  # Calls figure. Makes it the active plot.
        plt.savefig(end_path + file_name, format=figure_extension)  # Saves figure to directory. Sets file format.
        plt.close()  # Closes active figure.
    elif type == 'table':  # Conditional statement. Executes lines below if file is a table.
        dataframe.to_csv(end_path + file_name, index=truth_statement)  # Saves file to directory. Sets file format.
    if display == 1:  # Conditional statementFor display.
        print(display_label, 'exported')  # Display objects.

def hydraulic_geometry(dataframe, column1, display_label1, display_label2, display_label3, units,
                       display_label4, column2, display_label5, display_label6, display_label7,
                       display_label8, display):  # Defines function. For hydraulic geometry calculation.
    # Channel width
    df_strm_offst = slice_DataFrame_columns(dataframe, column1, 0, display_label1, 0)  # Defines DataFrame.
    # Calls function. Slices DataFrame to yield stream channel survey offsets.
    offst1 = min_value_DataFrame(df_strm_offst, display_label2, 0)  # Defines variable. Slices DataFrame
    # to yield first offset for stream channel.
    offst2 = max_value_DataFrame(df_strm_offst, display_label2, 0)  # Defines variable. Slices DataFrame
    # to yield last offset for stream channel.
    if offst1 < offst2:  # Conditional statement. Sets order of channel width calculation.
        wdth = offst2 - offst1  # Defines variable. Calculates channel width.
    elif offst1 > offst2:  # Conditional statement. Sets error contingency.
        sys.exit('Error: No stream channel detected')  # Exits code and displays string.
    elif offst1 == offst2:  # Conditional statement. Sets error contingency.
        sys.exit('Error: No stream channel detected')  # Exits code and displays string.
    if display == 1:  # Conditional statement. For display.
        print(display_label3 + units + '\n  ' + display_label4 + '%.1f' % wdth)  # Displays objects.
    # Channel depth
    df_strm_elvtn = slice_DataFrame_columns(dataframe, column2, 0, display_label5, 0)  # Defines DataFrame.
    # Slices DataFrame to yield stream channel survey elevations.
    elvtn1 = min_value_DataFrame(df_strm_elvtn, display_label6, 0)  # Defines variable. Slices DataFrame
    # to yield lowest elevation for stream channel.
    elvtn2 = max_value_DataFrame(df_strm_elvtn, display_label6, 0)  # Defines variable. Slices DataFrame
    # to yield highest elevation for stream channel.
    if elvtn1 < elvtn2:  # Conditional statement. Sets order of channel depth calculation.
        dpth = elvtn2 - elvtn1  # Defines variable. Calculates channel depth.
    elif elvtn1 > elvtn2:  # Conditional statement. Sets error contingency.
        sys.exit('Error: No stream channel detected')  # Exits code and displays string.
    elif elvtn1 == elvtn2:  # Conditional statement. Sets error contingency.
        sys.exit('Error: No stream channel detected')  # Exits code and displays string.
    elif elvtn1 | elvtn2 <= 0:  # Conditional statement. Sets error contingency.
        sys.exit('Error: No stream channel detected')  # Exits code and displays string.
    if display == 1:  # Conditional statement. For display.
        print('  ' + display_label7 + '%.2f' % dpth)  # Displays objects.
    # Hydraulic radius
    hydro_rad = (wdth * dpth) / (wdth + 2 * dpth)  # Defines variable. Calculated hydraulic radius.
    if display == 1:  # Conditional statement. For display.
        print('  ' + display_label8 + '%.2f' % hydro_rad)  # Displays objects.
    return wdth, dpth, hydro_rad  # Ends function execution.

def create_appended_list(value, display_label1, new_list, display_label2, display):  # Defines function. For post calculation list collection.
    try:  # Checks program for object. Takes action based off existence.
        value  # Defines object to be searched for.
    except NameError:  # Executed if object does not exist.
        sys.exit('Error: ' + display_label1 + 'value undefined')  # Exits code and displays string.
    else:  # Executed if object does exist.
        new_list.append(value)  # Appends list.
    if display == 1:  # Conditional statement. For display.
        print(display_label2, new_list)  # Displays objects.
    return new_list  # Ends function execution.

def create_DataFrame(array1, array2, display_label, display):  # Defines function. For creating DataFrame from arrays or lists.
    df_new = pd.DataFrame(data=array1, columns=array2)  # Defines function format.
    if display == 1:  # Conditional statement. For display.
        print('\033[1m' + display_label + ' DATA' + '\033[0m', '\n...\n', df_new, '\n')  # Displays objects.
    return df_new  # Ends function execution.

def export_file_to_directory(export, type, directory_levels, folder_labels, output_folder, display_label1, file_name, number, figure_extension, dataframe,
                             truth_statement, display_label2, display):  # Defines function. For exporting files.
    if export == 1:  # Conditional statement. Exports file.
        lvls = name_levels(directory_levels, folder_labels, output_folder, display_label1, display)  # Defines list. Calls function. For looped folder creation.
        for a in lvls:  # Begins loop through array elements. Loops through levels.
            lvl = lvls.index(a) + 2  # Defines variable as integer. For correct display.
            create_folder(lvl, a)  # Creates folders. Calls function.
        export_file(type, number, file_name, lvls[-1], figure_extension, dataframe, truth_statement, display_label2,
                    display)  # Exports file. Calls function.

def interpolate_cross_section(type, x, y, start, end, interpolation_type, step,
                              decimal_place, display):  # Defines function. For interpolating cross-sections for comparison.
    f = sc.interpolate.interp1d(x, y, kind=interpolation_type)  # Sets interpolation format.
    if type == 'dataframe':  # Conditional statement.
        x_list = x.tolist()  # Defines list. Converts DataFrame to list.
        start = x_list[0]  # Defines variable. Selects first element of list.
        end = x_list[-1]  # Defines variable. Selects first element of list.
    elif type == 'list':  # Conditional statement.
        x_list = x  # Defines list.
        start = x_list[0]  # Defines variable. Selects first element of list.
        end = x_list[-1]  # Defines variable. Selects first element of list.
    elif type == 'limits':  # Conditional statement.
        pass  # Executes nothing. Moves on to next line.
    new_end = end + step  # Defines variable. Resets end of range so array includes final input value.
    x_interpolated = np.arange(start, new_end, step)  # Defines array. Creates x array to interpolate y
    # values.

    if x_interpolated[-1] > end:
        x_interpolated = x_interpolated[0:-1]
    if x_interpolated[-1] == end:
        pass

    x_interpolated = np.around(x_interpolated, decimals=decimal_place)  # Redefines array. Rounds
    # values.
    y_interpolated = f(x_interpolated)  # Sets function format.
    x_range_interpolated = x_interpolated[-1] - x_interpolated[0]  # Defines variable. Calculates x
    # range.
    number_samples = len(x_interpolated)  # Defines variable. Calclates number of measurements.
    if display == 1:  # Conditional Statement. For Display.
        print('Interpolated datasets' + '\n  Limits: ' + str(start) + '–' + str(end) + '\n  Number of measurements: '
              + str(number_samples))  # Displays objects.
    return x_interpolated, y_interpolated, x_range_interpolated, number_samples

def select_coincident_x_range(type, x1, x2, units,
                              display):  # Defines function. For selecting coincident x values for reinpterpolation.
    if type == 'dataframe':  # Conditional statement. Executes lines below when input object is DataFrame.
        x1_list = x1.tolist()  # Defines list. Converts DataFrame to list.
        x2_list = x2.tolist()  # Defines list. Converts DataFrame to list.
    elif type == 'list':  # Conditional statement. Executes lines below when input object is list.
        x1_list = x1  # Defines list.
        x2_list = x2  # Defines list.
    x_min1 = x1_list[0]  # Defines variable. Selects lowest x value in list.
    x_max1 = x1_list[-1]  # Defines variable. Selects largest x value in list.
    x_min2 = x2_list[0]  # Defines variable. Selects lowest x value in list.
    x_max2 = x2_list[-1]  # Defines variable. Selects largest x value in list.
    if x_min1 == x_min2:  # Conditional statement. Selects limits shared between datasets.
        start = x_min1  # Defines variable. Sets first shared x value.
        if x_max1 == x_max2 or x_max1 < x_max2:  # Conditional statement.  Selects limits shared between datasets.
            end = x_max1  # Defines variable. Sets last shared x value.
        elif x_max1 > x_max2:  # Conditional statement.  Selects limits shared between datasets.
            end = x_max2  # Defines variable. Sets last shared x value.
    elif x_min1 < x_min2:  # Conditional statement.  Selects limits shared between datasets.
        start = x_min2  # Defines variable. Sets first shared x value.
        if x_max1 == x_max2 or x_max1 < x_max2:  # Conditional statement.  Selects limits shared between datasets.
            end = x_max1  # Defines variable. Sets last shared x value.
        elif x_max1 > x_max2:  # Conditional statement.  Selects limits shared between datasets.
            end = x_max2  # Defines variable. Sets last shared x value.
    elif x_min1 > x_min2:  # Conditional statement.  Selects limits shared between datasets.
        start = x_min1  # Defines variable. Sets first shared x value.
        if x_max1 == x_max2 or x_max1 < x_max2:  # Conditional statement.  Selects limits shared between datasets.
            end = x_max1  # Defines variable. Sets last shared x value.
        elif x_max1 > x_max2:  # Conditional statement.  Selects limits shared between datasets.
            end = x_max2  # Defines variable. Sets last shared x value.
    coincident_range = end - start  # Defines variable. Calculates coincident range between datasets.
    if display == 1:  # Conditional statement. For display.
        print('Coincident x values ' + '\n  X min: ' + str(x_min1) + ' & ' + str(x_min2) +
              '\n  X max: ' + str(x_max1) + ' & ' + str(x_max2) + '\n  Range: ' + str(
            start) + '–' + str(end) + ' (' + str('%.2f' % coincident_range) + units + ')')  # Displays objects.
    return start, end, coincident_range  # Ends function execution.

def get_coordinate_pairs(type, value1, value2, x_list, y1_list, y2_list,
                         display):  # Defines function. For retrieving coordinate pairs from interpolated datasets for looped calculations.
    if type == 'depth':  # Conditional statement. Executes lines below if depth is to be calculated.
        x1 = x_list[value1]  # Defines variable. Selects list element by index.
        y1_top = y1_list[value1]  # Defines variable. Selects list element by index.
        y1_btm = y2_list[value1]  # Defines variable. Selects list element by index.
        if display == 1:  # Conditional statement. For display.
            print('Coordinates' + '\n  Top: ' + '(' + str(x1) + ', ' + str('%.2f' % y1_top) + ')' + '\n  Bottom: ' + '(' + str(
                x1) + ', ' + str('%.2f' % y1_btm) + ')')  # Displays objects.
        return x1, y1_top, y1_btm  # Ends function execution.
    if type == 'area':  # Conditional statement. Executes lines below if depth is to be calculated.
        x1 = x_list[value1]  # Defines variable. Selects list element by index.
        x2 = x_list[value2]  # Defines variable. Selects list element by index.
        y1_top = y1_list[value1]  # Defines variable. Selects list element by index.
        y1_btm = y2_list[value1]  # Defines variable. Selects list element by index.
        y2_top = y1_list[value2]  # Defines variable. Selects list element by index.
        y2_btm = y2_list[value2]  # Defines variable. Selects list element by index.
        if display == 1:  # Conditional statement. For display.
            print('Coordinates' + '\n  Top: ' + '(' + str(x1) + ', ' + str('%.2f' % y1_top) + ')' + ' & ' + '(' + str(
                x2) + ', ' + str('%.2f' % y2_top) + ')'
                  + '\n  Bottom: ' + '(' + str(x1) + ', ' + str('%.2f' % y1_btm) + ')' + ' & ' + '(' + str(x2) + ', ' + str(
                '%.2f' % y2_btm) + ')')  # Displays objects.
        return x1, x2, y1_top, y1_btm, y2_top, y2_btm  # Ends function execution.

def sediment_thickness(type, y1_top, y1_btm, survey_year1, survey_year2, y2_top, y2_btm, display_label1, display):  # Defines function. For calculating sediment thickness between cross-sections.
    if type == 'depth':  # Conditional statement.
        dpth1 = y1_top - y1_btm  # Defines variable. Calculates depth at a point.
        if dpth1 > 0:  # Conditional statement. Characterizes depth measurement by surface process.
            prcs1 = 'Deposition'  # Defines variable as string. Identifies depth measurement as depositional.
            prcs1_rt = 'Aggradation'
        elif dpth1 < 0:  # Conditional statement.
            prcs1 = 'Erosion'  # Defines variable as string.
            prcs1_rt = 'Degradation'
        else:  # Conditional statement.
            prcs1 = 'No net change'  # Defines variable as string.
            prcs1_rt = 'No net change'
        srvy_yr1_int = int(survey_year1)
        if survey_year2 == '1850s':
            srvy_yr2_int = 1854
        elif survey_year2 != '1850s':
            srvy_yr2_int = int(survey_year2)
        srvy_intrvl = srvy_yr1_int - srvy_yr2_int
        dpth1_rt = dpth1 / srvy_intrvl
        if display == 1:  # Conditional statement. For display.
            print(display_label1 + str(srvy_intrvl) + ' years' + '\n ' + prcs1 + ': ' + str('%.5f' % dpth1) + '\n ' + prcs1_rt + ': ' + str('%.5f' % dpth1_rt))  # Displays objects.
        return dpth1, prcs1, dpth1_rt, prcs1_rt, srvy_intrvl  # Ends function execution.
    if type == 'area':  # Conditional statement.
        dpth1 = y1_top - y1_btm  # Defines variable. Calculates depth at a point.
        if dpth1 > 0:  # Conditional statement. Characterizes depth measurement by surface process.
            prcs1 = 'Deposition'  # Defines variable as string. Identifies depth measurement as depositional.
        elif dpth1 < 0:  # Conditional statement.
            prcs1 = 'Erosion'  # Defines variable as string.
        elif dpth1 == 0:  # Conditional statement.
            prcs1 = 'No net change'  # Defines variable as string.
        dpth2 = y2_top - y2_btm  # Defines variable. Calculates depth at a point.
        if dpth2 > 0:  # Conditional statement.
            prcs2 = 'Deposition'  # Defines variable as string.
        elif dpth2 < 0:  # Conditional statement.
            prcs2 = 'Erosion'  # Defines variable as string.
        elif dpth2 == 0:  # Conditional statement.
            prcs2 = 'No net change'  # Defines variable as string.
        if display == 1:  # Conditional Statement. For display.
            print(display_label1 + '\n  x1: ' + str('%.5f' % dpth1) + ' (' + prcs1 + ')' + '\n  x2: ' + str('%.5f' % dpth2) + ' (' + prcs2 + ')')  # Displays objects.
        return dpth1, dpth2, prcs1, prcs2  # Ends function execution.

def plot_fill(number, zones, x, y1, y2, label, face_color, alpha, location, marker_scale, frame_alpha, label_spacing, pause, pause_length):
    plt.figure(number)  # Calls figure. Makes it the active plot.
    ax = plt.gca()  # Defines variable. Retrieves plot axes instance.
    if zones == 1:  # Conditional statement. For shading 1 area.
        ax.fill_between(x, y1, y2, label=label, facecolor=face_color, alpha=alpha)  # Fills area over x range between y values.
        ax.legend(loc=location, markerscale=marker_scale, framealpha=frame_alpha, labelspacing=label_spacing)  # Creates legend. Through automatic label detection.
    if zones != 1:  # Conditional statement. For shading multiple areas.
        zones = zones + 1  # Defines variable. For establishing looped plotting framework.
        zone_list = range(1, zones, 1)  # Defines list. Creates range of integers for looped plotting.
        for a in zone_list:  # Begins loop through list elements. Loops through line numbers.
            index = zone_list.index(a)  # Defines variable. Retrieves index of element in list. For format selection.
            ax.fill_between(x, y1[index], y2[index], label=label[index], facecolor=face_color[index], alpha=alpha)  # Fills area over x range between y values.
            ax.legend(loc=location, markerscale=marker_scale, framealpha=frame_alpha, labelspacing=label_spacing)  # Creates legend. Through automatic label detection.
    if pause == 1:  # Conditional statement. For display format.
        plt.pause(pause_length)  # Displays plot. For set interval of seconds and closes without clearing.
    elif pause == 0:  # Conditional statement. For display format.
        plt.show()  # Displays plot. Indefinite and cleared upon close.

#*****************************************************************************************************************************


def sediment_area_trpz(x1, x2, height_R, height_L, display_label, display):
    if x1 > x2:
        x_R = x1
        x_L = x2
    elif x1 < x2:
        x_L = x1
        x_R = x2
    delta_x = x_R - x_L
    trpz_area = ((height_R + height_L) / 2) * delta_x
    if trpz_area > 0:
        prcs = 'Deposition'
    if trpz_area < 0:
        prcs = 'Erosion'
    if trpz_area == 0:
        prcs = 'No net change'
    if display == 1:
        print(display_label + '%.10f' % trpz_area + ' (' + prcs + ')')
    return trpz_area, prcs

#$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%nother day
def check_for_empties(dataframe, display):
    result = dataframe.empty
    if display == 1:
        print('Empty = ', result)
    return result


def mean_plus_stdv(array, display_label1, display):
    avg = np.mean(array)
    stdv = np.std(array)
    strt = avg - stdv
    end = avg + stdv
    if display == 1:
        print(display_label1 + '\n  Mean: ' + str('%.2f' % avg) + '\n  Standard deviation: ' + str(
            '%.4f' % stdv) + '\n  Range: ' + str('%.2f' % strt) + '–' + str('%.2f' % end))
    return avg, stdv, strt, end

#^^^^^^^^^^^^^^^^^^^^^^^^^nother day
def find_intersection(x1, x2, y1_1, y1_2, y2_1, y2_2, display):
    slpe1 = (y1_2 - y1_1) / (x2 - x1)
    b1_a = y1_1 - slpe1 * x1
    b1_b = y1_2 - slpe1 * x2
    b1_a = round(b1_a, 5)
    b1_b = round(b1_b, 5)
    if bool(b1_a == b1_b) == True:
        b1 = b1_a
    elif bool(b1_a == b1_b) == False:
        sys.exit('Error: Intercepts do not coincide')
    slpe2 = (y2_2 - y2_1) / (x2 - x1)
    b2_a = y2_1 - slpe2 * x1
    b2_b = y2_2 - slpe2 * x2
    b2_a = round(b2_a, 5)
    b2_b = round(b2_b, 5)
    if bool(b2_a == b2_b) == True:
        b2 = b2_a
    elif bool(b2_a == b2_b) == False:
        print('\n', b2_a, b2_b)
        sys.exit('Error: Intercepts do not coincide')
    x_test = (b1 - b2) / (slpe2 - slpe1)
    if x1 <= x_test <= x2:
        y1_test = slpe1 * x_test + b1
        y2_test = slpe2 * x_test + b2
        y1_test = round(y1_test, 5)
        y2_test = round(y2_test, 5)
        if bool(y1_test == y2_test) == True:
            y_test = y1_test
            intrsctn = 'Exists'
            if display == 1:
                print('Intersection found' + '\n  Between: ' + str(x1) + '–' + str(x2) + '\n  At: ' + '(' + str(x_test) + ', ' + str(y_test) + ')')
        elif bool(y1_test == y2_test) == False:
            sys.exit('Error: No intersection found at shared point')
    elif x1 > x_test or x2 < x_test:
        # print('No intersection between ' + str(x1) + '–' + str(x2))
        x_test = None
        y_test = None
        intrsctn = None
    return x_test, y_test, intrsctn
#^^^^^^^^^^^^^^^^^^^^^***********nother day
def sediment_volume(type, area1, area2, area_prime, area_quad, separation, width1, width2, display_label, display):
    if type == 'Average end area':
        # average end area
        V = (area1 + area2) / 2 * separation
    elif type == 'Prismoidal':
        # prismoidal
        V = (area_prime / 3) * ((area1 + area2) / (width1 + width2)) + (area_quad / 3) * ((area1 / width1) + (area2 / width2))
    if V < 0:
        prcs = 'Erosion'
    elif V > 0:
        prcs = 'Deposition'
    elif V == 0:
        prcs = 'No net change'
    if display == 1:
        print(display_label + str('%.2f' % V) + ' (' + prcs + ')')
    return V, prcs
#%%%%%%%%%%%%%%
def coordinate_bearing(x1, x2, y1, y2, c1,c2, bearing_reference_direction, bearing_angle_direction, bearing_deg, bearing_functional, display_label, display):
    offset_meas=c2-c1
    offset_meas=offset_meas*1/3.281
    # bearing_functional=[*bearing_functional]

    if bearing_reference_direction =='N':
        if bearing_angle_direction =='E':
            if bearing_functional == 'NE':
                qdrnt_meas = 1
                deg_max = 90
                new_bearing_deg = deg_max-bearing_deg
            if bearing_functional == 'SW':
                qdrnt_meas = 3
                deg_max = 270
                new_bearing_deg = deg_max - bearing_deg
        if bearing_angle_direction=='W':
            if bearing_functional == 'NW':
                qdrnt_meas=2
                deg_min=90
                new_bearing_deg=deg_min+bearing_deg
            if bearing_functional == 'SE':
                qdrnt_meas = 4
                deg_min = 270
                new_bearing_deg = deg_min + bearing_deg
    if bearing_reference_direction=='S':
        if bearing_angle_direction=='W':
            if bearing_functional == 'SW':
                qdrnt_meas=3
                deg_max=270
                new_bearing_deg=deg_max-bearing_deg
            if bearing_functional == 'NE':
                qdrnt_meas = 1
                deg_max = 90
                new_bearing_deg = deg_max-bearing_deg
        if bearing_angle_direction=='E':
            if bearing_functional == 'SE':
                qdrnt_meas = 4
                deg_min = 270
                new_bearing_deg = deg_min + bearing_deg
            if bearing_functional == 'NW':
                qdrnt_meas = 2
                deg_min = 90
                new_bearing_deg = deg_min + bearing_deg

    meas_bearing_rad=new_bearing_deg*(np.pi/180)
    delta_x = x2 - x1
    delta_y = y2 - y1
    offset_clc = math.sqrt(delta_x ** 2 + delta_y ** 2)
    bearing_rad = abs(math.atan(delta_y / delta_x))
    clc_bearing_deg=bearing_rad*(180/np.pi)

    if delta_x > 1:
        if delta_y > 1:
            qdrnt_clc = 1
            rad_max = np.pi/2
            clc_bearing_rad = rad_max-bearing_rad
        if delta_y<1:
            qdrnt_clc=4
            rad_min = (3*np.pi)/2
            clc_bearing_rad =rad_min+bearing_rad
    if delta_x<1:
        if delta_y>1:
            qdrnt_clc=2
            rad_min=np.pi/2
            clc_bearing_rad=rad_min+bearing_rad
        if delta_y<1:
            qdrnt_clc=3
            rad_max=(3*np.pi)/2
            clc_bearing_rad=rad_max-bearing_rad
    cor_bearing_deg=clc_bearing_rad*(180/np.pi)
    bearing_diff=clc_bearing_rad-meas_bearing_rad
    bearing_diff_deg=bearing_diff*(180/np.pi)
    offset_diff=offset_clc-offset_meas

    # if qdrnt_clc != qdrnt_meas:
    #     sys.exit('Quadrants misaligned')
    sin = math.sin(meas_bearing_rad)  # Calculates sine of heading.
    cos = math.cos(meas_bearing_rad)  # Calculates cosine of heading.
    if display == 1:
        degree_sign=chr(176)
        if abs(bearing_diff) > 1*(np.pi/180):
            print('Directional data' + '\n Quadrant' + '\n  Measured: ' + str(qdrnt_meas) + '\n  Calculated: ' + str(qdrnt_clc) +
            '\n Bearings' + '\n  Field range: ' + bearing_reference_direction+str(bearing_deg) + degree_sign+bearing_angle_direction+ ' ('+str('%.1f'%new_bearing_deg)+degree_sign+')'+'\n  Azimuthal equivalent: ' + str('%.2f'%meas_bearing_rad) +' ('+str('%.1f'%new_bearing_deg)+degree_sign+')'+
                  '\n  Calculated: '+str('%.2f'%bearing_rad)+' ('+str('%.1f'%clc_bearing_deg)+degree_sign+')'+'\n  Corrected to azimuth: ' +str('%.2f'%clc_bearing_rad) +' ('+str('%.1f'%cor_bearing_deg)+degree_sign+')' +'\n  Difference: ' + '\033[0;31m'+str('%.2f'%bearing_diff) + ' ('+str('%.1f'%bearing_diff_deg)+degree_sign+')'+'\033[0m'
                  +'\n Trig. components' + '\n  Sine: ' + str('%.4f'%sin)+'\n  Cosine: '+str('%.4f'%cos))
        else:
            print('Directional data' + '\n Quadrant' + '\n  Measured: ' + str(qdrnt_meas) + '\n  Calculated: ' + str(
                qdrnt_clc) +
                  '\n Bearings' + '\n  Field range: ' + bearing_reference_direction + str(
                bearing_deg) + degree_sign + bearing_angle_direction + ' (' + str(
                '%.1f' % new_bearing_deg) + degree_sign + ')' + '\n  Azimuthal equivalent: ' + str(
                '%.2f' % meas_bearing_rad) + ' (' + str('%.1f' % new_bearing_deg) + degree_sign + ')' +
                  '\n  Calculated: ' + str('%.2f' % bearing_rad) + ' (' + str(
                '%.1f' % clc_bearing_deg) + degree_sign + ')' + '\n  Corrected to azimuth: ' + str(
                '%.2f' % clc_bearing_rad) + ' (' + str(
                '%.1f' % cor_bearing_deg) + degree_sign + ')' + '\n  Difference: ' + '\033[0;36m'+str(
                '%.2f' % bearing_diff) + ' (' + str('%.1f' % bearing_diff_deg) + degree_sign + ')'+'\033[0m'+'\n Trig. components' + '\n  Sine: ' + str('%.4f'%sin)+'\n  Cosine: '+str('%.4f'%cos))
        if abs(offset_diff) >= 1:
            print(' Coordinate offset'+ '\n  X: ' + str('%.2f'%delta_x) + '\n  Y: ' +str('%.2f'%delta_y)+'\n  Measured: '+str('%.1f'%offset_meas)+'\n  Calculated: '+str('%.1f'%offset_clc)+'\n  Difference: '+'\033[0;31m'+str('%.1f'%offset_diff) + '\033[0m')
        else:
            print(' Coordinate offset'+'\n  X: ' + str('%.2f'%delta_x) + '\n  Y: ' +str('%.2f'%delta_y)+'\n  Measured: '+str('%.1f'%offset_meas)+'\n  Calculated: '+str('%.1f'%offset_clc)+'\n  Difference: '+'\033[0;36m'+str('%.1f'%offset_diff) + '\033[0m')

    return meas_bearing_rad,sin,cos
# ibm = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']
#
# # convert hex to rgb
#
# x = np.arange(0, np.pi, 0.1)
# y = np.arange(0, 2 * np.pi, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = np.cos(X) * np.sin(Y) * 10
#
# clr1=matplotlib.colors.to_rgb('#648FFF')
# clr1=matplotlib.colors.to_rgb('#785EF0')
# clr2=matplotlib.colors.to_rgb('#FFB000')
# colors=[clr1,clr2]
# n_bins = [3, 6, 10, 100]
# cmap_name = 'my_list'
# fig, axs = plt.subplots(2, 2, figsize=(6, 9))
# fig.subplots_adjust(left=0.02, bottom=0.06, right=0.95, top=0.94, wspace=0.05)
# for n_bin, ax in zip(n_bins, axs.ravel()):
#
#     cm = LinearSegmentedColormap.from_list(
#         cmap_name, colors, N=n_bin)
#     im = ax.imshow(Z, interpolation='nearest', origin='lower', cmap=cm)
#     ax.set_title("N bins: %s" % n_bin)
#     fig.colorbar(im, ax=ax)

